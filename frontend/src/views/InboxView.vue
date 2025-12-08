<template>
  <div class="p-6 h-screen overflow-y-auto bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold flex items-center gap-2">
          <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" /></svg>
          Memory Inbox
          <span v-if="store.count > 0" class="ml-2 px-2 py-0.5 text-sm bg-indigo-100 text-indigo-700 dark:bg-indigo-900 dark:text-indigo-300 rounded-full">{{ store.count }}</span>
        </h1>
        <div class="text-sm text-gray-500 flex flex-col items-end">
          <span>{{ authStore.user?.email }}</span>
          <span :class="store.connected ? 'text-green-500' : 'text-gray-400'">{{ store.connected ? '● Live' : '○ Offline' }}</span>
        </div>
      </div>

      <div v-if="store.items.length === 0" class="text-center py-20 text-gray-500">
        <svg class="w-16 h-16 mx-auto mb-4 text-gray-300 dark:text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <p>You're all caught up! No pending memories.</p>
      </div>

      <div v-else class="space-y-4">
        <!-- Inbox Item Card -->
        <div v-for="item in store.items" :key="item.id" class="bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 p-4 transition hover:shadow-md">
          <div class="flex justify-between items-start">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-2">
                <span class="px-2 py-0.5 text-xs font-medium rounded bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300 uppercase">{{ item.source }}</span>
                
                <!-- Status Badge -->
                <span v-if="item.status === 'approved'" class="bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium">
                   Auto-Approved Notification
                </span>
                
                <span class="text-xs text-gray-500">{{ new Date(item.timestamp || item.created_at).toLocaleString() }}</span>
              </div>
              
              <div class="text-base mb-4 whitespace-pre-wrap font-bold">{{ item.details }}</div>
              <div class="text-sm mb-4 whitespace-pre-wrap">{{ item.content }}</div>
              
              <!-- Triage Actions -->
              <div class="flex gap-2">
                <!-- If Pending -->
                <template v-if="item.status === 'pending'">
                  <button @click="store.handleAction(item.id, 'approve')" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-sm rounded-md transition flex items-center gap-1">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    Approve
                  </button>
                  <button @click="openEdit(item)" class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm rounded-md transition">
                    Edit
                  </button>
                  <button @click="store.handleAction(item.id, 'discard')" class="px-3 py-1.5 text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 text-sm rounded-md transition">
                    Discard
                  </button>
                </template>
                
                <!-- If Approved (Notification) -->
                <template v-if="item.status === 'approved'">
                   <button @click="store.handleAction(item.id, 'dismiss')" class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm rounded-md transition flex items-center gap-1">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                    Dismiss (Keep)
                  </button>
                  <button @click="store.handleAction(item.id, 'discard')" class="px-3 py-1.5 text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 text-sm rounded-md transition">
                    Discard (Delete)
                  </button>
                </template>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Edit Modal (Simple implementation) -->
    <div v-if="editingItem" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-2xl shadow-xl">
        <h3 class="text-lg font-bold mb-4">Edit Memory</h3>
        <textarea v-model="editContent" class="w-full h-40 p-3 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-600 rounded-lg mb-4 resize-none focus:ring-2 focus:ring-indigo-500"></textarea>
        <div class="flex justify-end gap-2">
          <button @click="editingItem = null" class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded">Cancel</button>
          <button @click="saveEdit" class="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700">Approve & Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useInboxStore } from '../stores/inbox';
import { useAuthStore } from '../stores/auth';

const store = useInboxStore();
const authStore = useAuthStore();
const editingItem = ref(null);
const editContent = ref('');

onMounted(() => {
  store.fetchInbox();
  store.connectWebSocket();
});

const openEdit = (item) => {
  editingItem.value = item;
  editContent.value = item.content;
};

const saveEdit = async () => {
  if (!editingItem.value) return;
  await store.handleAction(editingItem.value.id, 'edit', { content: editContent.value });
  editingItem.value = null;
};
</script>
