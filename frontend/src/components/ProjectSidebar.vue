<template>
  <div class="h-full flex flex-col">
    <div class="p-4 border-b border-gray-100 dark:border-gray-700 space-y-3">
      <h3 class="text-sm font-bold text-gray-900 dark:text-white">Projects</h3>
      <div class="flex gap-2">
        <input v-model="newProjectName" @keyup.enter="create" class="flex-1 min-w-0 text-xs border border-gray-200 dark:border-gray-700 rounded-md px-2 py-1 bg-white dark:bg-surface text-gray-900 dark:text-white" placeholder="New project" />
        <button @click="create" class="shrink-0 text-xs px-2.5 py-1 rounded-md bg-[#D97757] hover:bg-[#C4654A] text-white font-bold transition-colors">Add</button>
      </div>
    </div>
    <div class="flex-1 overflow-y-auto p-2 space-y-1">
      <button v-for="project in projects" :key="project.id" @click="$emit('select', project.id)" :class="buttonClass(Number(selectedProjectId) === project.id)">
        <span class="truncate">{{ project.name }}</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useToast } from 'vue-toastification';
import { createProject, listProjects } from '../services/projects';

const props = defineProps({
  selectedProjectId: { type: [Number, null], default: null },
});

const emit = defineEmits(['select']);
const toast = useToast();
const projects = ref([]);
const newProjectName = ref('');

const buttonClass = (active) => [
  'w-full text-left text-sm rounded-md px-3 py-2 transition-colors border',
  active
    ? 'bg-gray-900 text-white border-gray-900 dark:bg-gray-100 dark:text-gray-900 dark:border-gray-100'
    : 'bg-white dark:bg-surface border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-200',
];

const fetchProjects = async () => {
  try {
    projects.value = await listProjects(false);
  } catch (error) {
    console.error('Failed to fetch projects', error);
  }
};

const create = async () => {
  const name = newProjectName.value.trim();
  if (!name) return;
  try {
    await createProject({ name });
    newProjectName.value = '';
    await fetchProjects();
    toast.success('Project created');
  } catch (error) {
    console.error('Failed to create project', error);
    toast.error('Failed to create project');
  }
};

onMounted(fetchProjects);

defineExpose({ fetchProjects });
</script>
