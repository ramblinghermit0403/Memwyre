<template>
  <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6 h-full flex flex-col">
    <h2 class="text-lg font-medium text-gray-900 dark:text-white mb-4">{{ isEditing ? 'Edit Memory' : 'Create New Memory' }}</h2>
    
    <form @submit.prevent="saveMemory" class="flex-1 flex flex-col space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Title</label>
        <input type="text" id="title" v-model="form.title" required class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white" placeholder="Memory Title" />
      </div>
      
      <div class="flex-1">
        <label for="content" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Content</label>
        <textarea id="content" v-model="form.content" required rows="10" class="mt-1 block w-full h-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white resize-none" placeholder="Write your memory here..."></textarea>
      </div>
      
      <div class="flex justify-end space-x-3 pt-4">
        <button type="button" @click="cancel" class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Cancel
        </button>
        <button type="submit" :disabled="loading" class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed">
          {{ loading ? 'Saving...' : 'Save Memory' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import api from '../services/api';

const props = defineProps({
  memory: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['saved', 'cancelled']);

const form = ref({
  title: '',
  content: ''
});

const isEditing = ref(false);
const loading = ref(false);

watch(() => props.memory, (newVal) => {
  if (newVal) {
    form.value = { ...newVal };
    isEditing.value = true;
  } else {
    form.value = { title: '', content: '' };
    isEditing.value = false;
  }
}, { immediate: true });

const saveMemory = async () => {
  loading.value = true;
  try {
    if (isEditing.value) {
      await api.put(`/memory/${props.memory.id}`, form.value);
    } else {
      await api.post('/memory/', form.value);
    }
    emit('saved');
    form.value = { title: '', content: '' };
    isEditing.value = false;
  } catch (error) {
    console.error('Error saving memory:', error);
    alert('Failed to save memory');
  } finally {
    loading.value = false;
  }
};

const cancel = () => {
  emit('cancelled');
  form.value = { title: '', content: '' };
  isEditing.value = false;
};
</script>
