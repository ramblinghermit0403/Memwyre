<template>
  <div class="h-screen flex flex-col overflow-hidden">
    <NavBar />
    <main class="flex-1 overflow-y-auto p-6">
      <div class="max-w-5xl mx-auto">
        <h1 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Projects</h1>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div class="lg:col-span-3">
            <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden h-[680px]">
              <ProjectSidebar :selected-project-id="selectedProjectId" @select="(id) => selectedProjectId = id" />
            </div>
          </div>
          <div class="lg:col-span-9">
            <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden h-[680px]">
              <AIInteractionTimeline :project-id="selectedProjectId" />
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useProjectStore } from '../stores/project';
import NavBar from '../components/NavBar.vue';
import ProjectSidebar from '../components/ProjectSidebar.vue';
import AIInteractionTimeline from '../components/AIInteractionTimeline.vue';

const projectStore = useProjectStore();
const selectedProjectId = computed({
  get: () => projectStore.currentProjectId,
  set: (val) => projectStore.setCurrentProjectId(val)
});
</script>
