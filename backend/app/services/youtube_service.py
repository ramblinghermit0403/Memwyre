from typing import Optional
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.proxies import GenericProxyConfig
    HAVE_YOUTUBE_API = True
except ImportError:
    YouTubeTranscriptApi = None
    GenericProxyConfig = None
    HAVE_YOUTUBE_API = False
from urllib.parse import urlparse, parse_qs
import httpx
from bs4 import BeautifulSoup
import re

from app.core.config import settings

class YouTubeService:
    def __init__(self):
        """Initialize with optional proxy support for cloud deployments."""
        self._ytt_api = None

    @property
    def ytt_api(self) -> YouTubeTranscriptApi:
        """Lazily initialize YouTubeTranscriptApi with proxy if configured."""
        if self._ytt_api is None:
            proxy_url = settings.YOUTUBE_PROXY_URL
            if proxy_url:
                print(f"YouTube Proxy configured: {proxy_url[:20]}...")
                self._ytt_api = YouTubeTranscriptApi(
                    proxy_config=GenericProxyConfig(
                        http_url=proxy_url,
                        https_url=proxy_url,
                    )
                )
            else:
                self._ytt_api = YouTubeTranscriptApi()
        return self._ytt_api

    def get_video_id(self, url: str) -> Optional[str]:
        """
        Extracts the video ID from a YouTube URL.
        Supports:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/shorts/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        """
        # Regex is more robust for these variations
        patterns = [
            r'(?:v=|\/)([\w-]{11})(?:\?|&|$)',
            r'(?:embed\/|shorts\/|youtu\.be\/)([\w-]{11})',
            r'^([\w-]{11})$'  # Raw ID
        ]
        
        for p in patterns:
            match = re.search(p, url)
            if match:
                return match.group(1)

        # Fallback to parsing
        parsed = urlparse(url)
        if parsed.hostname == 'youtu.be':
            return parsed.path[1:]
        if parsed.path.startswith('/shorts/'):
            return parsed.path.split('/')[2]
            
        return None

    def _get_page_content(self, url: str) -> Optional[str]:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = httpx.get(url, headers=headers, follow_redirects=True)
            if response.status_code != 200:
                return None
            return response.text
        except:
            return None

    def get_video_title(self, url: str) -> str:
        """
        Fetches the video title from the YouTube page.
        """
        html = self._get_page_content(url)
        if not html:
            return f"YouTube Video ({self.get_video_id(url)})"
            
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else ""
            
            # Clean up "- YouTube" suffix
            if title.endswith(" - YouTube"):
                title = title[:-10]
                
            return title.strip() or f"YouTube Video ({self.get_video_id(url)})"
        except Exception as e:
            print(f"Error fetching title: {e}")
            return f"YouTube Video ({self.get_video_id(url)})"

    def get_video_description(self, url: str) -> str:
        """
        Fetches description from meta tags.
        """
        html = self._get_page_content(url)
        if not html:
            return ""
            
        try:
            soup = BeautifulSoup(html, 'html.parser')
            meta_desc = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
            if meta_desc:
                return meta_desc.get("content", "").strip()
            return ""
        except:
            return ""

    def extract_transcript(self, url: str) -> Optional[str]:
        """
        Extracts the transcript using youtube-transcript-api v1.x.
        Returns None if failed (instead of raising), so we can fallback to description.
        """
        video_id = self.get_video_id(url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")

        # Method 1: youtube_transcript_api v1.x (Fast)
        try:
            transcript_list = self.ytt_api.list(video_id)
            final_transcript = None
            
            # Try manually created transcript first
            try:
                final_transcript = transcript_list.find_manually_created_transcript(['en', 'en-US', 'en-GB'])
            except:
                pass
            
            # Then try auto-generated
            if not final_transcript:
                try:
                    final_transcript = transcript_list.find_generated_transcript(['en', 'en-US', 'en-GB'])
                except:
                    pass
            
            # Fallback: any available transcript, translate if possible
            if not final_transcript:
                try:
                    for t in transcript_list:
                        final_transcript = t
                        break
                    if final_transcript and final_transcript.is_translatable:
                        final_transcript = final_transcript.translate('en')
                except:
                    pass

            if final_transcript:
                fetched = final_transcript.fetch()
                # v1.x returns FetchedTranscript with snippet objects
                return " ".join([snippet.text for snippet in fetched]).strip()

        except Exception as e:
            print(f"Primary Transcript Method Failed for {video_id}: {e}")
            pass  # Fallthrough to Method 2

        # Method 2: yt-dlp (Robust fallback)
        print("Fallback: Attempting yt-dlp extraction...")
        try:
            import yt_dlp
            
            ydl_opts = {
                'skip_download': True,
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': ['en.*', 'en'],
                'quiet': True,
                'no_warnings': True,
            }

            # Add proxy to yt-dlp if configured
            proxy_url = settings.YOUTUBE_PROXY_URL
            if proxy_url:
                ydl_opts['proxy'] = proxy_url
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Check for subtitles
                subs = info.get('subtitles') or {}
                auto_subs = info.get('automatic_captions') or {}
                
                # Merge logic (manual subs override auto)
                all_subs = {**auto_subs, **subs}
                
                # Find English
                selected_sub = None
                for lang in all_subs:
                    if lang.startswith('en'):
                        selected_sub = all_subs[lang]
                        break
                
                if not selected_sub and all_subs:
                    # Pick first available
                    selected_sub = list(all_subs.values())[0]
                    
                if selected_sub:
                    # Prefer JSON3 format for easy parsing
                    sub_url = None
                    for fmt in selected_sub:
                        if fmt.get('ext') == 'json3':
                            sub_url = fmt['url']
                            break
                    
                    if not sub_url:
                        # Fallback to any url
                        sub_url = selected_sub[0]['url']
                        
                    # Fetch content
                    try:
                        import httpx
                        r = httpx.get(sub_url, timeout=10.0)
                        if 'json3' in sub_url or sub_url.endswith('json3'):
                            import json
                            data = r.json()
                            # Parse JSON3
                            events = data.get('events', [])
                            text_parts = []
                            for event in events:
                                segs = event.get('segs', [])
                                for seg in segs:
                                    t = seg.get('utf8', '').strip()
                                    if t and t != '\n':
                                        text_parts.append(t)
                            return " ".join(text_parts)
                        else:
                            # Fallback generic tag/time stripper (e.g., for .vtt or .srv1 or .xml)
                            import re
                            text = r.text
                            # 1. Remove XML/HTML tags
                            text = re.sub(r'<[^>]+>', '', text)
                            # 2. Remove timestamps
                            text = re.sub(r'\d{2}:\d{2}:\d{2}[\.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[\.,]\d{3}', '', text)
                            # 3. Clean up VTT headers
                            text = text.replace("WEBVTT\n", "").replace("Kind: captions\n", "").replace("Language: en\n", "")
                            # 4. Remove empty lines and normalize whitespace
                            lines = [line.strip() for line in text.split('\n') if line.strip() and not line.strip().isdigit()]
                            
                            cleaned_transcript = " ".join(lines)
                            cleaned_transcript = re.sub(r'\s+', ' ', cleaned_transcript).strip()
                            
                            if cleaned_transcript:
                                return cleaned_transcript
                            else:
                                print("Regex fallback returned empty string.")
                                return None
                                
                    except Exception as inner_e:
                        print(f"yt-dlp sub fetch error: {inner_e}")
                        
        except Exception as e:
            print(f"yt-dlp Fallback Failed: {e}")
            
        print("Transcript extraction failed completely.")
        return None

youtube_service = YouTubeService()
