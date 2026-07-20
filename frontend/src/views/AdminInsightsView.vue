<template>
  <div class="min-h-screen bg-gray-50 text-gray-900 dark:bg-background dark:text-text-primary">
    <NavBar />

    <main class="mx-auto flex w-full max-w-5xl flex-col gap-6 px-6 py-8 sm:px-8 lg:px-12">
      <header class="flex flex-col gap-4 border-b border-gray-200 pb-6 dark:border-border md:flex-row md:items-end md:justify-between">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.18em] text-primary">Admin</p>
          <h1 class="mt-2 text-3xl font-bold tracking-tight text-gray-950 dark:text-white">App Insights</h1>
          <p class="mt-2 max-w-2xl text-sm text-gray-500 dark:text-text-secondary">
            Users, capture activity, conversations, extension saves, documents, and token usage.
          </p>
        </div>

        <div class="flex flex-wrap items-center gap-3">
          <router-link
            to="/admin/bypass"
            class="inline-flex items-center gap-2 rounded-lg border border-gray-200 bg-white px-4 py-2 text-sm font-semibold text-gray-700 shadow-sm transition-colors hover:border-primary/40 hover:text-primary dark:border-border dark:bg-surface dark:text-text-secondary"
          >
            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H3v-4l6.257-6.257A6 6 0 1121 9z" />
            </svg>
            Payment bypass
          </router-link>
          <button
            @click="loadInsights"
            :disabled="loading"
            class="inline-flex items-center gap-2 rounded-lg bg-gray-950 px-4 py-2 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60 dark:bg-white dark:text-gray-950 dark:hover:bg-gray-200"
          >
            <svg class="h-4 w-4" :class="{ 'animate-spin': loading }" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582M20 20v-5h-.581M5.582 9A7.97 7.97 0 0112 4a8 8 0 017.446 5.032M18.418 15A7.97 7.97 0 0112 20a8 8 0 01-7.446-5.032" />
            </svg>
            Refresh
          </button>
        </div>
      </header>

      <div v-if="loading && !insights" class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div v-for="item in 8" :key="item" class="h-32 animate-pulse rounded-lg border border-gray-200 bg-white dark:border-border dark:bg-surface"></div>
      </div>

      <section v-else-if="error" class="rounded-lg border border-red-200 bg-red-50 p-6 text-red-700 dark:border-red-900/60 dark:bg-red-950/30 dark:text-red-300">
        <h2 class="text-lg font-bold">Unable to load admin insights</h2>
        <p class="mt-2 text-sm">{{ error }}</p>
      </section>

      <template v-else-if="insights">
        <section class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <article v-for="metric in primaryMetrics" :key="metric.label" class="rounded-lg border border-gray-200 bg-white p-5 shadow-sm dark:border-border dark:bg-surface">
            <div class="flex items-start justify-between gap-4">
              <div>
                <p class="text-sm font-medium text-gray-500 dark:text-text-secondary">{{ metric.label }}</p>
                <p class="mt-2 text-3xl font-bold tracking-tight text-gray-950 dark:text-white">{{ metric.value }}</p>
              </div>
              <div class="flex h-10 w-10 items-center justify-center rounded-lg" :class="metric.tone">
                <component :is="metric.icon" />
              </div>
            </div>
            <p class="mt-3 text-xs text-gray-500 dark:text-text-secondary">{{ metric.detail }}</p>
          </article>
        </section>

        <section class="mt-6 mb-6 rounded-lg border border-gray-200 bg-white p-5 shadow-sm dark:border-border dark:bg-surface">
          <div class="flex items-center justify-between gap-4">
            <div>
              <h2 class="text-lg font-bold text-gray-950 dark:text-white">Token Usage & Cost (Last 14 Days)</h2>
              <p class="mt-1 text-sm text-gray-500 dark:text-text-secondary">Daily token consumption and estimated LLM cost.</p>
            </div>
            <p class="text-xs text-gray-400 dark:text-text-muted">Generated {{ formattedGeneratedAt }}</p>
          </div>

          <div class="mt-6 grid h-56 grid-cols-[repeat(14,minmax(0,1fr))] items-end gap-2">
            <div v-for="day in insights.series" :key="day.date" class="flex h-full min-w-0 flex-col justify-end gap-1">
              <div class="flex flex-1 items-end gap-1">
                <div class="w-full rounded-t bg-amber-500" :style="{ height: barHeight(day.tokens, maxTokensValue) }" :title="`${formatNumber(day.tokens)} tokens ($${day.cost})`"></div>
              </div>
              <span class="truncate text-center text-[10px] text-gray-400">{{ formatShortDate(day.date) }}</span>
            </div>
          </div>
        </section>

        <section class="grid gap-6 xl:grid-cols-12">
          <article class="rounded-lg border border-gray-200 bg-white p-5 shadow-sm dark:border-border dark:bg-surface xl:col-span-8">
            <div class="flex items-center justify-between gap-4">
              <div>
                <h2 class="text-lg font-bold text-gray-950 dark:text-white">Last 14 Days</h2>
                <p class="mt-1 text-sm text-gray-500 dark:text-text-secondary">New users and app activity by day.</p>
              </div>
              <p class="text-xs text-gray-400 dark:text-text-muted">Generated {{ formattedGeneratedAt }}</p>
            </div>

            <div class="mt-6 grid h-72 grid-cols-[repeat(14,minmax(0,1fr))] items-end gap-2">
              <div v-for="day in insights.series" :key="day.date" class="flex h-full min-w-0 flex-col justify-end gap-1">
                <div class="flex flex-1 items-end gap-1">
                  <div class="w-full rounded-t bg-[#2563eb]" :style="{ height: barHeight(day.memories, maxSeriesValue) }" :title="`${day.memories} memories`"></div>
                  <div class="w-full rounded-t bg-[#16a34a]" :style="{ height: barHeight(day.chat_sessions, maxSeriesValue) }" :title="`${day.chat_sessions} chats`"></div>
                  <div class="w-full rounded-t bg-[#f59e0b]" :style="{ height: barHeight(day.documents, maxSeriesValue) }" :title="`${day.documents} documents`"></div>
                  <div class="w-full rounded-t bg-[#7c3aed]" :style="{ height: barHeight(day.users, maxSeriesValue) }" :title="`${day.users} users`"></div>
                </div>
                <span class="truncate text-center text-[10px] text-gray-400">{{ formatShortDate(day.date) }}</span>
              </div>
            </div>

            <div class="mt-4 flex flex-wrap gap-4 text-xs font-medium text-gray-500 dark:text-text-secondary">
              <span class="inline-flex items-center gap-2"><span class="h-2.5 w-2.5 rounded-sm bg-[#2563eb]"></span>Memories</span>
              <span class="inline-flex items-center gap-2"><span class="h-2.5 w-2.5 rounded-sm bg-[#16a34a]"></span>Chats</span>
              <span class="inline-flex items-center gap-2"><span class="h-2.5 w-2.5 rounded-sm bg-[#f59e0b]"></span>Documents</span>
              <span class="inline-flex items-center gap-2"><span class="h-2.5 w-2.5 rounded-sm bg-[#7c3aed]"></span>Users</span>
            </div>
          </article>

          <aside class="grid gap-6 xl:col-span-4">
            <section class="rounded-lg border border-gray-200 bg-white p-5 shadow-sm dark:border-border dark:bg-surface">
              <h2 class="text-lg font-bold text-gray-950 dark:text-white">Memory Sources</h2>
              <div class="mt-5 space-y-4">
                <div v-for="item in insights.source_breakdown" :key="item.source" class="space-y-1.5">
                  <div class="flex items-center justify-between gap-3 text-sm">
                    <span class="truncate font-medium text-gray-700 dark:text-text-primary">{{ item.source }}</span>
                    <span class="text-gray-500 dark:text-text-secondary">{{ formatNumber(item.count) }}</span>
                  </div>
                  <div class="h-2 overflow-hidden rounded-full bg-gray-100 dark:bg-surface-2">
                    <div class="h-full rounded-full bg-primary" :style="{ width: percentWidth(item.count, maxSourceCount) }"></div>
                  </div>
                </div>
                <p v-if="!insights.source_breakdown.length" class="text-sm text-gray-500 dark:text-text-secondary">No memory sources yet.</p>
              </div>
            </section>

            <section class="rounded-lg border border-gray-200 bg-white p-5 shadow-sm dark:border-border dark:bg-surface">
              <h2 class="text-lg font-bold text-gray-950 dark:text-white">Interaction Types</h2>
              <div class="mt-5 space-y-3">
                <div v-for="item in insights.interaction_breakdown" :key="item.type" class="flex items-center justify-between rounded-md bg-gray-50 px-3 py-2 text-sm dark:bg-surface-2">
                  <span class="font-medium capitalize text-gray-700 dark:text-text-primary">{{ item.type }}</span>
                  <span class="text-gray-500 dark:text-text-secondary">{{ formatNumber(item.count) }}</span>
                </div>
                <p v-if="!insights.interaction_breakdown.length" class="text-sm text-gray-500 dark:text-text-secondary">No interactions yet.</p>
              </div>
            </section>
          </aside>
        </section>

        <section class="grid gap-6 xl:grid-cols-12">
          <article class="rounded-lg border border-gray-200 bg-white shadow-sm dark:border-border dark:bg-surface xl:col-span-8">
            <div class="border-b border-gray-200 p-5 dark:border-border">
              <h2 class="text-lg font-bold text-gray-950 dark:text-white">User Ingestion Token Breakdown</h2>
              <p class="mt-1 text-sm text-gray-500 dark:text-text-secondary">Click on any user to view their ingested Memories, Documents, Model, and exact Tokens consumed.</p>
            </div>
            
            <div class="divide-y divide-gray-200 dark:divide-border">
              <div v-for="user in insights.users" :key="user.id" class="p-5 transition-colors hover:bg-gray-50/50 dark:hover:bg-surface-2/40">
                <div class="flex flex-wrap items-center justify-between gap-4 cursor-pointer" @click="toggleUserExpand(user.id)">
                  <div class="flex items-center gap-3">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-primary/10 text-primary font-bold text-sm">
                      {{ (user.email || 'U')[0].toUpperCase() }}
                    </div>
                    <div>
                      <div class="flex items-center gap-2">
                        <span class="font-bold text-gray-950 dark:text-white">{{ user.email }}</span>
                        <span class="rounded-full px-2 py-0.5 text-[10px] font-semibold" :class="user.is_verified ? 'bg-green-50 text-green-700 dark:bg-green-950/40 dark:text-green-300' : 'bg-amber-50 text-amber-700 dark:bg-amber-950/40 dark:text-amber-300'">
                          {{ user.is_verified ? 'Verified' : 'Unverified' }}
                        </span>
                      </div>
                      <p class="text-xs text-gray-500 dark:text-text-secondary">User ID: {{ user.id }} · Joined {{ formatShortDate(user.created_at) }}</p>
                    </div>
                  </div>

                  <div class="flex flex-wrap items-center gap-4 text-sm">
                    <div class="text-right">
                      <p class="text-xs text-gray-400">Raw Content Tokens</p>
                      <p class="font-bold text-amber-600 dark:text-amber-400">{{ formatNumber(user.total_raw_tokens || user.total_ingestion_tokens || 0) }} tokens</p>
                    </div>
                    <div class="text-right">
                      <p class="text-xs text-gray-400">LLM API Tokens</p>
                      <p class="font-bold text-blue-600 dark:text-blue-400">{{ formatNumber(user.total_llm_tokens || user.total_ingestion_tokens || 0) }} tokens</p>
                    </div>
                    <div class="text-right">
                      <p class="text-xs text-gray-400">Est. Cost</p>
                      <p class="font-bold text-emerald-600 dark:text-emerald-400">${{ (user.total_ingestion_cost || 0).toFixed(4) }}</p>
                    </div>
                    <div class="flex gap-2">
                      <span class="rounded-md bg-blue-50 px-2.5 py-1 text-xs font-semibold text-blue-700 dark:bg-blue-950/40 dark:text-blue-300">
                        {{ user.memories || 0 }} Memories
                      </span>
                      <span class="rounded-md bg-violet-50 px-2.5 py-1 text-xs font-semibold text-violet-700 dark:bg-violet-950/40 dark:text-violet-300">
                        {{ user.documents || 0 }} Docs
                      </span>
                    </div>
                    <svg class="h-5 w-5 transform text-gray-400 transition-transform" :class="{ 'rotate-180': expandedUserIds.has(user.id) }" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>
                </div>

                <!-- Expanded Details for User -->
                <div v-if="expandedUserIds.has(user.id)" class="mt-5 space-y-6 border-t border-gray-100 pt-5 dark:border-border/60">
                  <!-- User Memories Section -->
                  <div>
                    <h4 class="text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-text-muted mb-3 flex items-center gap-2">
                      <span class="h-2 w-2 rounded-full bg-blue-500"></span>
                      Ingested Memories ({{ (user.memory_items || []).length }})
                    </h4>
                    <div v-if="(user.memory_items || []).length" class="overflow-x-auto rounded-lg border border-gray-100 dark:border-border">
                      <table class="min-w-full divide-y divide-gray-100 text-xs dark:divide-border">
                        <thead class="bg-gray-50 dark:bg-surface-2 text-gray-500 dark:text-text-muted">
                          <tr>
                            <th class="px-4 py-2.5 text-left font-semibold">Title</th>
                            <th class="px-4 py-2.5 text-left font-semibold">Source</th>
                            <th class="px-4 py-2.5 text-left font-semibold">Model</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Raw Content Tokens</th>
                            <th class="px-4 py-2.5 text-right font-semibold">LLM API Tokens</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Cost</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Ingested At</th>
                          </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 dark:divide-border bg-white dark:bg-surface">
                          <tr v-for="item in user.memory_items" :key="item.id">
                            <td class="px-4 py-2.5 font-medium text-gray-900 dark:text-white max-w-xs truncate">{{ item.title }}</td>
                            <td class="px-4 py-2.5 text-gray-500 dark:text-text-secondary capitalize">{{ item.source }}</td>
                            <td class="px-4 py-2.5"><span class="rounded bg-gray-100 dark:bg-surface-2 px-1.5 py-0.5 font-mono text-[10px]">{{ item.model_name }}</span></td>
                            <td class="px-4 py-2.5 text-right font-bold text-amber-600 dark:text-amber-400">{{ formatNumber(item.raw_tokens_count || item.tokens_count) }} tokens</td>
                            <td class="px-4 py-2.5 text-right font-semibold text-blue-600 dark:text-blue-400">{{ formatNumber(item.llm_tokens_count || item.tokens_count) }} tokens</td>
                            <td class="px-4 py-2.5 text-right text-gray-500">${{ item.estimated_cost.toFixed(5) }}</td>
                            <td class="px-4 py-2.5 text-right text-gray-400">{{ formatDateTime(item.created_at) }}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <p v-else class="text-xs text-gray-400 italic">No memories created yet.</p>
                  </div>

                  <!-- User Documents Section -->
                  <div>
                    <h4 class="text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-text-muted mb-3 flex items-center gap-2">
                      <span class="h-2 w-2 rounded-full bg-violet-500"></span>
                      Ingested Documents ({{ (user.document_items || []).length }})
                    </h4>
                    <div v-if="(user.document_items || []).length" class="overflow-x-auto rounded-lg border border-gray-100 dark:border-border">
                      <table class="min-w-full divide-y divide-gray-100 text-xs dark:divide-border">
                        <thead class="bg-gray-50 dark:bg-surface-2 text-gray-500 dark:text-text-muted">
                          <tr>
                            <th class="px-4 py-2.5 text-left font-semibold">Title</th>
                            <th class="px-4 py-2.5 text-left font-semibold">File Type</th>
                            <th class="px-4 py-2.5 text-left font-semibold">Model</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Raw Document Tokens</th>
                            <th class="px-4 py-2.5 text-right font-semibold">LLM API Tokens</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Cost</th>
                            <th class="px-4 py-2.5 text-right font-semibold">Ingested At</th>
                          </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 dark:divide-border bg-white dark:bg-surface">
                          <tr v-for="doc in user.document_items" :key="doc.id">
                            <td class="px-4 py-2.5 font-medium text-gray-900 dark:text-white max-w-xs truncate">{{ doc.title }}</td>
                            <td class="px-4 py-2.5 text-gray-500 dark:text-text-secondary uppercase">{{ doc.file_type }}</td>
                            <td class="px-4 py-2.5"><span class="rounded bg-gray-100 dark:bg-surface-2 px-1.5 py-0.5 font-mono text-[10px]">{{ doc.model_name }}</span></td>
                            <td class="px-4 py-2.5 text-right font-bold text-amber-600 dark:text-amber-400">{{ formatNumber(doc.raw_tokens_count || doc.tokens_count) }} tokens</td>
                            <td class="px-4 py-2.5 text-right font-semibold text-blue-600 dark:text-blue-400">{{ formatNumber(doc.llm_tokens_count || doc.tokens_count) }} tokens</td>
                            <td class="px-4 py-2.5 text-right text-gray-500">${{ doc.estimated_cost.toFixed(5) }}</td>
                            <td class="px-4 py-2.5 text-right text-gray-400">{{ formatDateTime(doc.created_at) }}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <p v-else class="text-xs text-gray-400 italic">No documents ingested yet.</p>
                  </div>
                </div>
              </div>

              <div v-if="!insights.users?.length" class="p-8 text-center text-sm text-gray-500">
                No users found.
              </div>
            </div>
          </article>

          <aside class="rounded-lg border border-gray-200 bg-white shadow-sm dark:border-border dark:bg-surface xl:col-span-4">
            <div class="border-b border-gray-200 p-5 dark:border-border">
              <h2 class="text-lg font-bold text-gray-950 dark:text-white">Recent Activity</h2>
              <p class="mt-1 text-sm text-gray-500 dark:text-text-secondary">Latest memories, chats, and documents.</p>
            </div>
            <div class="max-h-[520px] divide-y divide-gray-100 overflow-y-auto dark:divide-border">
              <div v-for="item in insights.recent_activity" :key="`${item.kind}-${item.created_at}-${item.title}`" class="p-4">
                <div class="flex items-start gap-3">
                  <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg" :class="activityTone(item.kind)">
                    <svg v-if="item.kind === 'memory'" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h6m-6 4h8M5 4h14a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V6a2 2 0 012-2z" />
                    </svg>
                    <svg v-else-if="item.kind === 'chat'" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h8M8 14h5M5 5h14a2 2 0 012 2v8a2 2 0 01-2 2H9l-4 4v-4H5a2 2 0 01-2-2V7a2 2 0 012-2z" />
                    </svg>
                    <svg v-else class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6M7 3h7l5 5v13a2 2 0 01-2 2H7a2 2 0 01-2-2V5a2 2 0 012-2z" />
                    </svg>
                  </div>
                  <div class="min-w-0">
                    <p class="truncate font-semibold text-gray-900 dark:text-white">{{ item.title }}</p>
                    <p class="mt-0.5 truncate text-xs text-gray-500 dark:text-text-secondary">{{ item.user_email }} · {{ item.meta }}</p>
                    <p class="mt-1 text-xs text-gray-400 dark:text-text-muted">{{ formatDateTime(item.created_at) }}</p>
                  </div>
                </div>
              </div>
              <p v-if="!insights.recent_activity.length" class="p-5 text-sm text-gray-500 dark:text-text-secondary">No activity yet.</p>
            </div>
          </aside>
        </section>
      </template>
    </main>
  </div>
</template>

<script setup>
import { computed, h, onMounted, ref } from 'vue';
import NavBar from '../components/NavBar.vue';
import api from '../services/api';

const insights = ref(null);
const loading = ref(false);
const error = ref('');
const expandedUserIds = ref(new Set());

const toggleUserExpand = (id) => {
  if (expandedUserIds.value.has(id)) {
    expandedUserIds.value.delete(id);
  } else {
    expandedUserIds.value.add(id);
  }
};

const iconClass = 'h-5 w-5';
const icon = (path) => ({
  render() {
    return h('svg', { class: iconClass, fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: path }),
    ]);
  },
});

const UsersIcon = icon('M17 20h5v-2a4 4 0 00-4-4h-1M9 20H4v-2a4 4 0 014-4h1m0-4a4 4 0 100-8 4 4 0 000 8zm8 0a4 4 0 100-8 4 4 0 000 8z');
const MemoryIcon = icon('M7 8h10M7 12h6m-6 4h8M5 4h14a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V6a2 2 0 012-2z');
const ChatIcon = icon('M8 10h8M8 14h5M5 5h14a2 2 0 012 2v8a2 2 0 01-2 2H9l-4 4v-4H5a2 2 0 01-2-2V7a2 2 0 012-2z');
const UsageIcon = icon('M13 10V3L4 14h7v7l9-11h-7z');

const formatNumber = (value) => new Intl.NumberFormat().format(value || 0);
const formatMoney = (value) => `$${Number(value || 0).toFixed(4)}`;
const formatShortDate = (value) => new Date(value).toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
const formatDateTime = (value) => {
  if (!value) return 'Never';
  return new Date(value).toLocaleString(undefined, {
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  });
};

const formattedGeneratedAt = computed(() => formatDateTime(insights.value?.generated_at));

const primaryMetrics = computed(() => {
  const overview = insights.value?.overview || {};
  return [
    {
      label: 'Total Users',
      value: formatNumber(overview.total_users),
      detail: `${formatNumber(overview.verified_users)} verified · ${formatNumber(overview.active_users_7d)} active this week`,
      icon: UsersIcon,
      tone: 'bg-blue-50 text-blue-700 dark:bg-blue-950/40 dark:text-blue-300',
    },
    {
      label: 'Memories',
      value: formatNumber(overview.total_memories),
      detail: `${formatNumber(overview.conversation_memories)} conversations · ${formatNumber(overview.extension_memories)} extension saves`,
      icon: MemoryIcon,
      tone: 'bg-green-50 text-green-700 dark:bg-green-950/40 dark:text-green-300',
    },
    {
      label: 'Chats',
      value: formatNumber(overview.chat_sessions),
      detail: `${formatNumber(overview.chat_messages)} messages stored`,
      icon: ChatIcon,
      tone: 'bg-violet-50 text-violet-700 dark:bg-violet-950/40 dark:text-violet-300',
    },
    {
      label: 'Usage',
      value: formatNumber((overview.tokens_in || 0) + (overview.tokens_out || 0)),
      detail: `${formatMoney(overview.estimated_cost)} estimated LLM cost`,
      icon: UsageIcon,
      tone: 'bg-amber-50 text-amber-700 dark:bg-amber-950/40 dark:text-amber-300',
    },
  ];
});

const maxSeriesValue = computed(() => {
  const values = (insights.value?.series || []).flatMap((day) => [
    day.users,
    day.memories,
    day.documents,
    day.chat_sessions,
  ]);
  return Math.max(1, ...values);
});

const maxTokensValue = computed(() => {
  const values = (insights.value?.series || []).map((day) => day.tokens);
  return Math.max(1, ...values);
});

const maxSourceCount = computed(() => Math.max(1, ...(insights.value?.source_breakdown || []).map((item) => item.count)));

const barHeight = (value, maxValue) => `${Math.max(value ? 8 : 2, (Number(value || 0) / Number(maxValue || 1)) * 100)}%`;
const percentWidth = (value, maxValue) => `${Math.max(4, (Number(value || 0) / Number(maxValue || 1)) * 100)}%`;

const activityTone = (kind) => {
  if (kind === 'chat') return 'bg-violet-50 text-violet-700 dark:bg-violet-950/40 dark:text-violet-300';
  if (kind === 'document') return 'bg-amber-50 text-amber-700 dark:bg-amber-950/40 dark:text-amber-300';
  return 'bg-blue-50 text-blue-700 dark:bg-blue-950/40 dark:text-blue-300';
};

const loadInsights = async () => {
  loading.value = true;
  error.value = '';
  try {
    const response = await api.get('/admin/insights');
    insights.value = response.data;
  } catch (err) {
    if (err.response?.status === 403) {
      error.value = 'Your account is signed in, but it is not listed in ADMIN_EMAILS on the backend.';
    } else {
      error.value = err.response?.data?.detail || err.message || 'Something went wrong.';
    }
  } finally {
    loading.value = false;
  }
};

onMounted(loadInsights);
</script>
