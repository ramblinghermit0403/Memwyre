<template>
  <div class="h-full flex flex-col">
    <div class="p-6 border-b border-gray-100 dark:border-gray-700 flex items-center justify-between gap-4">
      <div>
        <h3 class="text-lg font-bold text-gray-900 dark:text-white">Recent AI Work</h3>
        <p class="text-xs text-gray-400 mt-1">Your interaction timeline across AI tools.</p>
      </div>
      <div class="flex items-center gap-2">
        <div class="relative source-selector">
          <button
            @click.stop="toggleSourceMenu"
            ref="sourceButtonRef"
            class="inline-flex items-center justify-between gap-1.5 min-w-[132px] text-xs border border-gray-200 dark:border-gray-700 rounded-md px-2.5 py-1.5 bg-white dark:bg-surface hover:bg-gray-50 dark:hover:bg-gray-800"
          >
            <span>{{ activeSourceLabel }}</span>
            <svg class="w-3 h-3 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>
        </div>
        <button @click="fetchTimeline" class="text-xs px-2 py-1 rounded-md border border-gray-200 dark:border-gray-700">Refresh</button>
      </div>
    </div>

    <div v-if="loading" class="flex-1 flex items-center justify-center text-sm text-gray-400">Loading timeline...</div>

    <div v-else class="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-8">
      <div v-if="Object.keys(groupedItems).length === 0" class="text-sm text-gray-500">
        No AI interactions yet. Save your first interaction to start building your timeline.
      </div>

      <div v-for="(dayItems, dayKey) in groupedItems" :key="dayKey" class="space-y-3">
        <h4 class="text-xs uppercase tracking-wider text-gray-500 font-bold">{{ dayLabel(dayKey) }}</h4>

        <ul class="divide-y divide-gray-200 dark:divide-gray-700 border-t border-b border-gray-200 dark:border-gray-700">
          <li v-for="item in dayItems" :key="item.id" class="py-4">
            <div class="flex items-start justify-between gap-3 px-1">
              <div class="min-w-0 flex-1">
                <div class="flex items-start gap-3">
                  <div class="w-6 h-6 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden mt-0.5">
                    <template v-if="getTimelineIcon(item).type === 'svg'">
                      <div
                        v-html="getTimelineIcon(item).content"
                        :class="['w-full h-full', isOpenAIItem(item) ? 'dark:invert dark:brightness-0' : '']"
                      ></div>
                    </template>
                    <template v-else-if="getTimelineIcon(item).type === 'img'">
                      <img
                        :src="getTimelineIcon(item).content"
                        alt="Source Icon"
                        :class="['w-full h-full object-cover rounded-sm', isOpenAIItem(item) ? 'dark:invert dark:brightness-0' : '']"
                        @error="handleImageError($event)"
                      />
                    </template>
                  </div>

                  <div class="min-w-0">
                    <p class="text-sm font-semibold text-gray-900 dark:text-white truncate">{{ item.title || 'Untitled AI Interaction' }}</p>
                    <p class="text-xs text-gray-500 mt-1">
                      {{ displaySource(item.source_app) }} | {{ item.interaction_type || 'conversation' }} | {{ formatTime(item.created_at) }}
                    </p>
                    <p class="text-sm text-gray-600 dark:text-gray-300 mt-2 line-clamp-2">{{ item.content }}</p>
                    <div class="mt-2 flex items-center gap-2">
                      <div class="relative project-selector">
                        <button
                          @click.stop="toggleProjectMenu(item)"
                          :ref="(el) => setProjectButtonRef(item.id, el)"
                          class="inline-flex items-center justify-between gap-1.5 min-w-[120px] text-[10px] px-2 py-1 rounded-md border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface hover:bg-gray-50 dark:hover:bg-gray-800"
                        >
                          <span>{{ projectLabel(item) }}</span>
                          <svg class="w-2.5 h-2.5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 shrink-0">
                <button @click="$emit('open-item', item)" class="inline-flex items-center gap-1.5 text-xs px-2.5 py-1.5 rounded-md border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-800">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 3h7m0 0v7m0-7L10 14"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 7v12h12"></path>
                  </svg>
                  <span>Open</span>
                </button>
                <details class="relative">
                  <summary class="list-none cursor-pointer inline-flex items-center gap-1.5 text-xs px-2.5 py-1.5 rounded-md border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-800">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3l1.6 3.4L17 8l-3.4 1.6L12 13l-1.6-3.4L7 8l3.4-1.6L12 3z"></path>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 16l.9 1.9L8 19l-2.1 1L5 22l-.9-2L2 19l2.1-1.1L5 16z"></path>
                    </svg>
                    <span>Use in AI</span>
                    <svg class="w-3 h-3 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                  </summary>
                  <div class="absolute right-0 mt-1 w-52 rounded-md border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface shadow-lg z-20 p-1">
                    <button @click="handoff(item, 'chatgpt')" class="w-full text-left text-xs px-2 py-1.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded flex items-center gap-2">
                      <img :src="openaiIcon" alt="ChatGPT" class="w-4 h-4 dark:invert dark:brightness-0" />
                      Continue in ChatGPT
                    </button>
                    <button @click="handoff(item, 'claude')" class="w-full text-left text-xs px-2 py-1.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded flex items-center gap-2">
                      <img :src="claudeIcon" alt="Claude" class="w-4 h-4" />
                      Continue in Claude
                    </button>
                    <button @click="handoff(item, 'gemini')" class="w-full text-left text-xs px-2 py-1.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded flex items-center gap-2">
                      <img :src="geminiIcon" alt="Gemini" class="w-4 h-4" />
                      Continue in Gemini
                    </button>
                    <button @click="copyOnly(item)" class="w-full text-left text-xs px-2 py-1.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded flex items-center gap-2">
                      <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H7a2 2 0 01-2-2V5a2 2 0 012-2h9a2 2 0 012 2v1"></path>
                        <rect x="9" y="9" width="10" height="12" rx="2" ry="2" stroke-width="2"></rect>
                      </svg>
                      Copy Context
                    </button>
                  </div>
                </details>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <Teleport to="body">
      <div
        v-if="sourceMenuOpen"
        class="source-selector-menu overflow-y-auto custom-scrollbar rounded-md border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface shadow-lg z-[1100] p-1"
        :style="sourceMenuStyle"
        @click.stop
      >
        <button
          v-for="option in sourceOptions"
          :key="option.value"
          @click="selectSource(option.value)"
          :class="[
            'w-full text-left px-2.5 py-1.5 text-xs rounded-md transition-colors',
            activeSource === option.value
              ? 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'
              : 'hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300'
          ]"
        >
          {{ option.label }}
        </button>
      </div>
    </Teleport>

    <Teleport to="body">
      <div
        v-if="projectMenuForId !== null && activeProjectItem"
        class="project-selector-menu overflow-y-auto custom-scrollbar rounded-md border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface shadow-lg z-[1100] p-1"
        :style="projectMenuStyle"
        @click.stop
      >
        <button
          @click="selectProject(activeProjectItem, '')"
          :class="[
            'w-full text-left px-2.5 py-1.5 text-xs rounded-md transition-colors',
            !activeProjectItem.project_id
              ? 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'
              : 'hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300'
          ]"
        >
          Unassigned
        </button>
        <button
          v-for="project in projects"
          :key="project.id"
          @click="selectProject(activeProjectItem, project.id)"
          :class="[
            'w-full text-left px-2.5 py-1.5 text-xs rounded-md transition-colors',
            Number(activeProjectItem.project_id) === Number(project.id)
              ? 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'
              : 'hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300'
          ]"
        >
          {{ project.name }}
        </button>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from 'vue';
import { useToast } from 'vue-toastification';
import api from '../services/api';
import { composeContext } from '../services/context';
import { listProjects } from '../services/projects';
import { getIconForSource } from '../utils/iconResolver';
import openaiIcon from '../assets/openai.svg';
import claudeIcon from '../assets/claude-color.svg';
import geminiIcon from '../assets/gemini-color.svg';

const props = defineProps({
  projectId: { type: [Number, String], default: null },
  focusToday: { type: Boolean, default: false },
});

const emit = defineEmits(['open-item']);
const toast = useToast();
const loading = ref(false);
const items = ref([]);
const activeSource = ref('');
const projects = ref([]);
const sourceMenuOpen = ref(false);
const projectMenuForId = ref(null);
const sourceButtonRef = ref(null);
const sourceMenuStyle = ref({});
const projectMenuStyle = ref({});
const projectButtonRefs = new Map();

const sourceOptions = [
  { value: '', label: 'All Sources' },
  { value: 'chatgpt', label: 'ChatGPT' },
  { value: 'claude', label: 'Claude' },
  { value: 'gemini', label: 'Gemini' },
  { value: 'web', label: 'Web' },
];

const activeSourceLabel = computed(() => sourceOptions.find((x) => x.value === activeSource.value)?.label || 'All Sources');
const activeProjectItem = computed(() => items.value.find((item) => item.id === projectMenuForId.value) || null);

const formatDateKey = (dateLike) => {
  const d = new Date(dateLike);
  if (Number.isNaN(d.getTime())) return 'Unknown';
  return d.toISOString().slice(0, 10);
};

const groupedItems = computed(() => {
  const filtered = props.focusToday
    ? items.value.filter((item) => formatDateKey(item.created_at) === formatDateKey(new Date()))
    : items.value;

  return filtered.reduce((acc, item) => {
    const key = item.timeline_group || formatDateKey(item.created_at);
    if (!acc[key]) acc[key] = [];
    acc[key].push(item);
    return acc;
  }, {});
});

const dayLabel = (key) => {
  const today = formatDateKey(new Date());
  const yesterday = formatDateKey(new Date(Date.now() - 86400000));
  if (key === today) return 'Today';
  if (key === yesterday) return 'Yesterday';
  return new Date(key).toLocaleDateString();
};

const formatTime = (dt) => {
  const d = new Date(dt);
  return Number.isNaN(d.getTime()) ? '' : d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};

const displaySource = (source) => {
  const normalized = (source || '').toLowerCase();
  if (normalized.includes('chatgpt') || normalized.includes('openai')) return 'ChatGPT';
  if (normalized.includes('claude')) return 'Claude';
  if (normalized.includes('gemini')) return 'Gemini';
  if (normalized.includes('web')) return 'Web';
  return source || 'AI Tool';
};

const getTimelineIcon = (item) => getIconForSource({
  source: item.source_app || item.source || '',
  tags: item.tags || [],
});

const handleImageError = (e) => {
  e.target.style.display = 'none';
};

const isOpenAIItem = (item) => {
  const src = String(item?.source_app || item?.source || '').toLowerCase();
  return src.includes('chatgpt') || src.includes('openai');
};

const projectLabel = (item) => {
  if (item?.project_name) return item.project_name;
  if (item?.project_id) {
    const match = projects.value.find((p) => Number(p.id) === Number(item.project_id));
    return match?.name || 'Project';
  }
  return 'Unassigned';
};

const setProjectButtonRef = (id, el) => {
  const key = String(id);
  if (el) {
    projectButtonRefs.set(key, el);
    return;
  }
  projectButtonRefs.delete(key);
};

const buildPopoverStyle = (anchorEl, options = {}) => {
  if (!anchorEl) return {};

  const rect = anchorEl.getBoundingClientRect();
  const edgePadding = 8;
  const spacing = 6;
  const viewportW = window.innerWidth;
  const viewportH = window.innerHeight;
  const estimatedHeight = options.estimatedHeight || 220;

  const width = options.matchButtonWidth
    ? Math.max(options.minWidth || 0, rect.width)
    : Math.max(options.minWidth || 176, Math.min(options.maxWidth || 260, Math.max(rect.width, options.minWidth || 176)));

  let left = options.align === 'right' ? rect.right - width : rect.left;
  left = Math.max(edgePadding, Math.min(left, viewportW - width - edgePadding));

  const openBelow = rect.bottom + spacing + estimatedHeight <= viewportH - edgePadding;
  const top = openBelow
    ? rect.bottom + spacing
    : Math.max(edgePadding, rect.top - estimatedHeight - spacing);

  const availableHeight = openBelow
    ? Math.max(120, viewportH - top - edgePadding)
    : Math.max(120, rect.top - edgePadding - spacing);

  return {
    position: 'fixed',
    left: `${Math.round(left)}px`,
    top: `${Math.round(top)}px`,
    width: `${Math.round(width)}px`,
    maxHeight: `${Math.round(Math.min(estimatedHeight, availableHeight))}px`,
  };
};

const updateSourceMenuPosition = () => {
  sourceMenuStyle.value = buildPopoverStyle(sourceButtonRef.value, {
    matchButtonWidth: true,
    minWidth: 132,
    align: 'right',
    estimatedHeight: 180,
  });
};

const updateProjectMenuPosition = () => {
  if (projectMenuForId.value === null) {
    projectMenuStyle.value = {};
    return;
  }
  const button = projectButtonRefs.get(String(projectMenuForId.value));
  projectMenuStyle.value = buildPopoverStyle(button, {
    minWidth: 176,
    maxWidth: 260,
    align: 'left',
    estimatedHeight: 240,
  });
};

const updateOpenMenuPositions = () => {
  if (sourceMenuOpen.value) updateSourceMenuPosition();
  if (projectMenuForId.value !== null) updateProjectMenuPosition();
};

const toggleSourceMenu = () => {
  sourceMenuOpen.value = !sourceMenuOpen.value;
  if (sourceMenuOpen.value) projectMenuForId.value = null;
  if (sourceMenuOpen.value) updateSourceMenuPosition();
};

const toggleProjectMenu = (item) => {
  projectMenuForId.value = projectMenuForId.value === item.id ? null : item.id;
  if (projectMenuForId.value) sourceMenuOpen.value = false;
  if (projectMenuForId.value) updateProjectMenuPosition();
};

const selectSource = async (source) => {
  activeSource.value = source;
  sourceMenuOpen.value = false;
  await fetchTimeline();
};

const selectProject = async (item, projectIdValue) => {
  if (!item) return;
  await assignProject(item, projectIdValue);
  projectMenuForId.value = null;
};

const handleGlobalClick = (event) => {
  const target = event.target;
  if (!(target instanceof Element)) return;
  if (!target.closest('.source-selector') && !target.closest('.source-selector-menu')) sourceMenuOpen.value = false;
  if (!target.closest('.project-selector') && !target.closest('.project-selector-menu')) projectMenuForId.value = null;
};

const fetchProjects = async () => {
  try {
    projects.value = await listProjects(false);
  } catch (error) {
    console.error('Failed to load projects in timeline', error);
  }
};

const fetchTimeline = async () => {
  loading.value = true;
  try {
    const params = { view: 'timeline', limit: 300 };
    if (props.projectId !== null && props.projectId !== undefined && props.projectId !== '') {
      params.project_id = Number(props.projectId);
    }
    if (activeSource.value) params.source_app = activeSource.value;
    const response = await api.get('/memory/', { params });
    items.value = (response.data || []).filter((x) => String(x.id || '').startsWith('mem_'));
  } catch (error) {
    console.error('Failed to fetch timeline', error);
    toast.error('Failed to load AI interactions timeline');
  } finally {
    loading.value = false;
  }
};

const assignProject = async (item, projectIdValue) => {
  try {
    const projectId = projectIdValue ? Number(projectIdValue) : null;
    await api.put(`/memory/${item.id}`, {
      title: item.title || 'Untitled',
      content: item.content || '',
      tags: item.tags || [],
      project_id: projectId,
      interaction_type: item.interaction_type || 'conversation',
      source_app: item.source_app || null,
    });
    item.project_id = projectId;
    const project = projects.value.find((p) => p.id === projectId);
    item.project_name = project ? project.name : null;
    toast.success('Project updated');
  } catch (error) {
    console.error('Failed to assign project', error);
    toast.error('Failed to update project assignment');
  }
};

const copyText = async (text) => {
  const value = text || '';

  if (navigator.clipboard?.writeText) {
    try {
      await navigator.clipboard.writeText(value);
      return true;
    } catch (error) {
      // Fallback below.
    }
  }

  try {
    const textarea = document.createElement('textarea');
    textarea.value = value;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    textarea.style.pointerEvents = 'none';
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, textarea.value.length);
    const copied = document.execCommand('copy');
    document.body.removeChild(textarea);
    return copied;
  } catch {
    return false;
  }
};

const providerUrl = (provider, text) => {
  const encoded = encodeURIComponent(text || '');
  if (provider === 'chatgpt') return `https://chatgpt.com/?prompt=${encoded}`;
  if (provider === 'claude') return `https://claude.ai/new?q=${encoded}`;
  if (provider === 'gemini') {
    // Gemini URL prefill support is inconsistent; include both query/hash patterns.
    return `https://gemini.google.com/app?hl=en&q=${encoded}&prompt=${encoded}#prompt=${encoded}`;
  }
  return null;
};

const handoff = async (item, provider) => {
  // Open the tab immediately from the click gesture to reduce popup blocking.
  const popup = window.open('', '_blank', 'noopener,noreferrer');
  try {
    const payload = await composeContext({ itemIds: [item.id], maxChars: 2800 });
    const contextText = payload?.context_text || item.content || '';
    const prefillText = provider === 'gemini' ? contextText.slice(0, 1500) : contextText;
    const url = providerUrl(provider, prefillText);

    if (url) {
      const copied = await copyText(contextText);
      if (popup) {
        popup.location.href = url;
      } else {
        window.open(url, '_blank', 'noopener,noreferrer');
      }

      if (provider === 'gemini') {
        if (copied) {
          toast.success('Opened Gemini. If prompt is empty, paste with Ctrl+V.');
        } else {
          toast.info('Opened Gemini. Prompt prefill may vary by browser/account.');
        }
      } else {
        toast.success(copied ? 'Opened AI tool. Context copied as fallback.' : 'Opened AI tool.');
      }
      return;
    }

    if (popup) popup.close();
    const copied = await copyText(contextText);
    if (copied) {
      toast.success('Context copied to clipboard.');
    } else {
      toast.error('Could not copy context automatically.');
    }
  } catch (error) {
    if (popup) popup.close();
    console.error('Handoff failed', error);
    toast.error('Could not prepare context handoff');
  }
};

const copyOnly = async (item) => {
  try {
    const payload = await composeContext({ itemIds: [item.id], maxChars: 2800 });
    const copied = await copyText(payload?.context_text || item.content || '');
    if (copied) {
      toast.success('Context copied to clipboard.');
    } else {
      toast.error('Could not copy context automatically.');
    }
  } catch (error) {
    console.error('Copy context failed', error);
    toast.error('Failed to copy context');
  }
};

watch(() => props.projectId, fetchTimeline);
onMounted(async () => {
  document.addEventListener('click', handleGlobalClick);
  window.addEventListener('resize', updateOpenMenuPositions);
  window.addEventListener('scroll', updateOpenMenuPositions, true);
  await fetchProjects();
  await fetchTimeline();
});

onUnmounted(() => {
  document.removeEventListener('click', handleGlobalClick);
  window.removeEventListener('resize', updateOpenMenuPositions);
  window.removeEventListener('scroll', updateOpenMenuPositions, true);
});

defineExpose({ fetchTimeline });
</script>

