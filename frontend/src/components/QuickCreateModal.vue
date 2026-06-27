<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6" role="dialog" aria-modal="true">
    
    <!-- Backdrop -->
    <div class="fixed inset-0 bg-gray-900/40 backdrop-blur-sm transition-opacity" @click="close"></div>

    <!-- Modal Panel -->
    <div class="relative w-[840px] h-[500px] overflow-hidden rounded-xl bg-white dark:bg-zinc-900 text-left shadow-2xl transition-all flex flex-col">
      
      <!-- Close Button -->
      <button @click="close" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors z-10">
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- Header -->
      <div class="px-8 pt-6 pb-2">
        <h3 class="text-2xl font-bold text-gray-900 dark:text-white mb-1">Add Content</h3>
        <p class="text-gray-500 dark:text-gray-400 text-sm">Choose a method to add content to your Brain Vault.</p>
      </div>

      <!-- Main Content (Scrollable) -->
      <div class="flex-1 overflow-y-auto px-8 pb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <!-- Left Column: Write a Memory & Ingest Webpage -->
          <div class="flex flex-col gap-6">
            <!-- Card 1: Write a Memory -->
            <div class="border border-gray-200 dark:border-zinc-800 bg-gray-50/50 dark:bg-zinc-900/20 rounded-xl p-5 flex flex-col justify-between h-[168px] hover:border-gray-300 dark:hover:border-zinc-700 transition-colors">
              <div class="flex gap-4">
                <div class="p-2.5 h-10 w-10 shrink-0 rounded-lg bg-gray-100 dark:bg-zinc-800 text-gray-700 dark:text-gray-300 flex items-center justify-center">
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                </div>
                <div>
                  <h4 class="text-sm font-semibold text-gray-900 dark:text-white">Write a Memory</h4>
                  <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Create a new memory in the editor with full formatting support.</p>
                </div>
              </div>
              <button @click="navigateToEditor" class="w-full py-2 bg-[#D97757] hover:bg-[#C4654A] text-white rounded-lg transition-colors font-medium text-xs shadow-sm">
                Open Editor
              </button>
            </div>

            <!-- Card 2: Ingest Webpage -->
            <div class="border border-gray-200 dark:border-zinc-800 bg-gray-50/50 dark:bg-zinc-900/20 rounded-xl p-5 flex flex-col justify-between h-[168px] hover:border-gray-300 dark:hover:border-zinc-700 transition-colors">
              <div class="flex gap-4">
                <div class="p-2.5 h-10 w-10 shrink-0 rounded-lg bg-gray-100 dark:bg-zinc-800 text-gray-700 dark:text-gray-300 flex items-center justify-center">
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="text-sm font-semibold text-gray-900 dark:text-white">Ingest Webpage</h4>
                  <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Extract and save articles, links, or documentation pages.</p>
                </div>
              </div>
              
              <!-- URL Input Box with Action Button -->
              <div class="flex gap-2 mt-2">
                <div class="relative flex-grow">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a2 2 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <input 
                    v-model="urlInput" 
                    type="url" 
                    class="block w-full pl-9 pr-3 py-2 border border-gray-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-1 focus:ring-[#D97757] dark:bg-zinc-800 dark:text-white text-xs" 
                    placeholder="https://example.com/article"
                    @keyup.enter="ingest"
                    @input="handleWebpageUrlChange"
                  />
                </div>
                <button
                  @click="ingest"
                  :disabled="!urlInput || uploading"
                  class="px-4 py-2 text-xs font-semibold bg-[#D97757] hover:bg-[#C4654A] text-white rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed shrink-0 shadow-sm flex items-center gap-1.5"
                >
                  <svg v-if="uploading && urlInput" class="animate-spin h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ uploading && urlInput ? 'Ingesting...' : 'Ingest' }}
                </button>
              </div>

              <!-- Ingestion status -->
              <div class="h-4 mt-1 flex items-center justify-between">
                <p v-if="webpagePreview.loading" class="text-[10px] text-blue-600 dark:text-blue-400 font-medium animate-pulse">
                  Fetching page info...
                </p>
                <p v-else-if="webpagePreview.url" class="text-[10px] text-green-600 dark:text-green-400 font-medium truncate max-w-[280px]">
                  Ready: {{ webpagePreview.title }}
                </p>
                <p v-else class="text-[10px] text-gray-400">
                  Enter URL and click Ingest to process.
                </p>
              </div>
            </div>
          </div>

          <!-- Right Column: Document Upload Zone -->
          <div class="flex flex-col h-[360px]">
            <div 
              @dragover.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @drop.prevent="handleDrop"
              :class="[
                'h-full border-2 border-dashed rounded-xl p-6 flex flex-col items-center justify-center transition-colors cursor-pointer',
                isDragging 
                  ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/10' 
                  : 'border-gray-200 dark:border-zinc-800 hover:border-gray-300 dark:hover:border-zinc-700 bg-gray-50/30 dark:bg-zinc-900/20'
              ]"
              @click="triggerFileInput"
            >
              <input type="file" ref="fileInput" @change="handleFileChange" class="hidden" />
              
              <!-- Default state -->
              <template v-if="!selectedFile && !uploadSuccess">
                <div class="p-3 rounded-full bg-gray-100 dark:bg-zinc-800 text-gray-500 dark:text-gray-400 mb-4">
                  <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                </div>
                <p class="text-sm text-gray-700 dark:text-gray-200 font-semibold text-center">Upload Files</p>
                <p class="text-xs text-gray-400 mt-2 text-center">Drag & drop files here, or click to browse</p>
                <p class="text-[10px] text-gray-400 mt-1">PDF, DOCX, TXT, MD (Max 10MB)</p>
              </template>

              <!-- Uploading State -->
              <div v-else-if="uploading && selectedFile" class="flex flex-col items-center w-full max-w-xs text-center">
                <LoadingLogo size="md" />
                <span class="text-xs text-gray-600 dark:text-gray-300 mt-3 animate-pulse">Uploading file...</span>
              </div>

              <!-- File preview / uploaded state -->
              <div v-else-if="selectedFile || uploadSuccess" class="w-full px-2" @click.stop>
                <div class="bg-gray-100 dark:bg-zinc-800 border border-gray-200 dark:border-zinc-700 rounded-lg p-3 flex items-center justify-between">
                  <div class="flex items-center gap-3 overflow-hidden">
                    <div class="p-2 rounded bg-white dark:bg-zinc-700 text-gray-500 shrink-0">
                      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                    </div>
                    <div class="min-w-0 flex-grow text-left">
                      <p class="text-xs font-semibold text-gray-900 dark:text-white truncate">
                        {{ selectedFile ? selectedFile.name : 'document.pdf' }}
                      </p>
                      <p class="text-[10px] text-gray-500 dark:text-gray-400 mt-0.5">
                        {{ selectedFile ? formatSize(selectedFile.size) : 'Ready' }}
                      </p>
                    </div>
                  </div>
                  <button 
                    v-if="!uploadSuccess"
                    @click="clearFile" 
                    class="text-gray-400 hover:text-red-500 p-1"
                    title="Remove File"
                  >
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                  </button>
                  <div v-else class="text-green-500 p-1">
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </div>
                
                <p v-if="uploadSuccess" class="text-xs text-green-600 dark:text-green-400 mt-3 text-center font-medium">
                  File processed and added successfully!
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';
import { useToast } from 'vue-toastification';
import { useProjectStore } from '../stores/project';
import LoadingLogo from '@/components/common/LoadingLogo.vue';

const props = defineProps({
  isOpen: Boolean,
  initialTab: {
    type: String,
    default: 'documents',
  },
});

const emit = defineEmits(['close']);
const router = useRouter();
const toast = useToast();
const projectStore = useProjectStore();

const isDragging = ref(false);
const fileInput = ref(null);
const selectedFile = ref(null);
const uploading = ref(false);
const uploadSuccess = ref(false);

const navigateToEditor = () => {
    close();
    router.push('/editor/new');
}

const close = () => {
    emit('close');
    setTimeout(reset, 300);
};

const reset = () => {
    selectedFile.value = null;
    uploadSuccess.value = false;
    urlInput.value = '';
    webpagePreview.value = { url: null, domain: null, favicon: null, title: null, loading: false };
};

const triggerFileInput = () => {
    fileInput.value.click();
};

const handleFileChange = (e) => {
    const files = e.target.files;
    if (files.length) {
        processFile(files[0]);
        ingest();
    }
};

const handleDrop = (e) => {
    isDragging.value = false;
    const files = e.dataTransfer.files;
    if (files.length) {
        processFile(files[0]);
        ingest();
    }
};

const processFile = (file) => {
    selectedFile.value = file;
};

const clearFile = () => {
    selectedFile.value = null;
    uploadSuccess.value = false;
    if (fileInput.value) fileInput.value.value = '';
};

const formatSize = (bytes) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
};

const urlInput = ref('');

const webpagePreview = ref({
    url: null,
    domain: null,
    favicon: null,
    title: null,
    loading: false
});

let urlDebounceTimer = null;

const extractYouTubeId = (url) => {
    if (!url) return null;
    const patterns = [
        /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/,
        /youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})/
    ];
    for (const pattern of patterns) {
        const match = url.match(pattern);
        if (match) return match[1];
    }
    return null;
};

const handleWebpageUrlChange = () => {
    clearTimeout(urlDebounceTimer);
    
    const url = urlInput.value.trim();
    if (!url || !url.startsWith('http')) {
        webpagePreview.value = { url: null, domain: null, favicon: null, title: null, loading: false };
        return;
    }
    
    const isYouTube = url.includes('youtube.com') || url.includes('youtu.be');
    if (isYouTube) {
        const videoId = extractYouTubeId(url);
        if (videoId) {
            webpagePreview.value = {
                url: url,
                domain: 'youtube.com',
                favicon: `https://www.google.com/s2/favicons?sz=64&domain=youtube.com`,
                title: 'YouTube Video Link',
                loading: false
            };
        }
        return;
    }

    urlDebounceTimer = setTimeout(() => {
        try {
            const urlObj = new URL(url);
            const domain = urlObj.hostname;
            webpagePreview.value = {
                url: url,
                domain: domain,
                favicon: `https://www.google.com/s2/favicons?sz=64&domain=${domain}`,
                title: domain,
                loading: false
            };
        } catch (e) {
            webpagePreview.value = { url: null, domain: null, favicon: null, title: null, loading: false };
        }
    }, 300);
};

const ingest = async () => {
    uploading.value = true;

    try {
        if (selectedFile.value) {
            const formData = new FormData();
            formData.append('file', selectedFile.value);

            const params = {};
            if (projectStore.currentProjectId) {
                params.project_id = projectStore.currentProjectId;
            }

            await api.post('/documents/upload', formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
                params
            });
            
            uploadSuccess.value = true;
            toast.success('Document uploaded successfully');
        } 
        else if (urlInput.value) {
             if (!urlInput.value || !urlInput.value.startsWith('http')) {
                 toast.error("Please enter a valid URL");
                 uploading.value = false;
                 return;
             }
             
             const isYouTube = urlInput.value.includes('youtube.com') || urlInput.value.includes('youtu.be');
             const payload = { 
                 url: urlInput.value
             };
             if (projectStore.currentProjectId) {
                 payload.project_id = projectStore.currentProjectId;
             }
             
             if (isYouTube) {
                 await api.post('/documents/upload-youtube', payload);
                 toast.success('Video transcript queued for ingestion');
             } else {
                 payload.tags = ['web-import'];
                 await api.post('/ingest/url', payload);
                 toast.success('Webpage queued for ingestion');
             }
             
             uploadSuccess.value = true;
        }

        setTimeout(() => {
            close();
            router.go(0); 
        }, 1000);

    } catch (error) {
        console.error(error);
        const status = error.response?.status;
        if (status !== 403 && status !== 413) {
            toast.error('Operation failed: ' + (error.response?.data?.detail || error.message));
        }
    } finally {
        uploading.value = false;
    }
};

watch(
  () => props.isOpen,
  (isOpen) => {
    if (isOpen) reset();
  },
);
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.3s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

.animate-slide-up { animation: slideUp 0.4s ease-out; }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
</style>
