import re
import json

def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_idx = -1
    for i, line in enumerate(lines):
        if 'id="tiles-bottom-left"' in line:
            start_idx = i
            break

    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if 'id="patch-tile"' in lines[i]:
            end_idx = i
            break

    shadow_indices = []
    for i in range(start_idx, end_idx):
        if 'opacity="0.55"' in lines[i] and 'filter=' in lines[i]:
            shadow_indices.append(i)

    tiles = []
    for idx, shadow_line in enumerate(shadow_indices):
        next_shadow = shadow_indices[idx + 1] if idx + 1 < len(shadow_indices) else end_idx
        tile_content = ''.join(lines[shadow_line:next_shadow])

        clip_match = re.search(r'clip-path="url\(#([^"]+)\)"', tile_content)
        clip_id = clip_match.group(1) if clip_match else "none"
        
        path_match = re.search(r'<path d="([^"]{30})', tile_content[tile_content.find('clip-path'):] if 'clip-path' in tile_content else tile_content)
        fingerprint = path_match.group(1) if path_match else "no-path"

        # Check colors
        colors = re.findall(r'fill="([^"]+)"', tile_content)
        colors = [c for c in colors if c not in ('#474747', '#D7D7D7', 'white', '#777777', '#111111')]
        
        tiles.append({
            "index": idx,
            "start_line": shadow_line,
            "end_line": next_shadow,
            "clip_id": clip_id,
            "fingerprint": fingerprint,
            "colors": list(set(colors))
        })
        
    for t in tiles:
        print(f"Tile {t['index']}: clip={t['clip_id']}, colors={t['colors']}")
        
    # Check for duplicates side by side
    print("\nPotential side-by-side duplicates:")
    for i in range(len(tiles) - 1):
        if tiles[i]['clip_id'] != 'none' and tiles[i]['clip_id'] == tiles[i+1]['clip_id']:
            print(f"Tile {i} and {i+1} share clip {tiles[i]['clip_id']}")
        elif tiles[i]['fingerprint'] != 'no-path' and tiles[i]['fingerprint'] == tiles[i+1]['fingerprint']:
            print(f"Tile {i} and {i+1} share fingerprint {tiles[i]['fingerprint']}")

if __name__ == "__main__":
    run()
