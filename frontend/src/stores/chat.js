import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';
import { useAuthStore } from './auth';
import { useToast } from 'vue-toastification';
import { useProjectStore } from './project';

const STEP_ORDER = [
    'request_received',
    'memory_search_started',
    'memory_search_completed',
    'llm_generation_started',
    'llm_generation_completed',
    'sources_attached',
    'response_saved',
    'turn_completed',
    'turn_failed',
];

const STEP_LABELS = {
    request_received: 'Request received',
    memory_search_started: 'Searching memory/documents',
    memory_search_completed: 'Memory search completed',
    llm_generation_started: 'Generating answer',
    llm_generation_completed: 'Generation completed',
    sources_attached: 'Attaching sources',
    response_saved: 'Saving response',
    turn_completed: 'Turn completed',
    turn_failed: 'Turn failed',
};

const statusFromEvent = (status) => {
    if (status === 'started') return 'active';
    if (status === 'failed') return 'failed';
    return 'completed';
};

const stepSortIndex = (stepName) => {
    const idx = STEP_ORDER.indexOf(stepName);
    return idx === -1 ? Number.MAX_SAFE_INTEGER : idx;
};

const createClientTurnId = () => {
    if (window.crypto?.randomUUID) return window.crypto.randomUUID();
    return `turn-${Date.now()}-${Math.random().toString(16).slice(2)}`;
};

const clampNumber = (value, min, max, fallback) => {
    const parsed = Number(value);
    if (!Number.isFinite(parsed)) return fallback;
    return Math.min(max, Math.max(min, parsed));
};

export const useChatStore = defineStore('chat', () => {
    const sessions = ref([]);
    const currentSession = ref(null);
    const messages = ref([]);
    const isLoading = ref(false);
    const error = ref(null);
    const thinking = ref(false);
    const selectedModel = ref('apac.amazon.nova-pro-v1:0');
    const currentContext = ref([]);

    const socket = ref(null);
    const wsConnected = ref(false);
    const shouldReconnect = ref(true);

    const activeTurnId = ref(null);
    const turnProgressById = ref({});

    if (selectedModel.value.includes('gemini')) {
        selectedModel.value = 'apac.amazon.nova-pro-v1:0';
    }

    const storedModel = localStorage.getItem('chat-model');
    if (storedModel && storedModel.includes('gemini')) {
        selectedModel.value = 'apac.amazon.nova-pro-v1:0';
        localStorage.setItem('chat-model', 'apac.amazon.nova-pro-v1:0');
    }

    const availableModels = [
        { id: 'apac.amazon.nova-pro-v1:0', name: 'Amazon Nova Pro' }
    ];

    const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

    const resetTurnProgress = () => {
        activeTurnId.value = null;
        turnProgressById.value = {};
    };

    const getTurnSteps = (turnId = activeTurnId.value) => {
        if (!turnId) return [];
        return turnProgressById.value[turnId]?.steps || [];
    };

    const upsertTurnStep = (evt) => {
        if (!evt?.client_turn_id || !evt?.step) return;
        if (!currentSession.value || Number(evt.session_id) !== Number(currentSession.value.id)) return;
        if (activeTurnId.value && activeTurnId.value !== evt.client_turn_id) return;

        const turnId = evt.client_turn_id;
        activeTurnId.value = activeTurnId.value || turnId;

        const snapshot = { ...turnProgressById.value };
        const existing = snapshot[turnId]
            ? { ...snapshot[turnId], steps: [...snapshot[turnId].steps] }
            : { sessionId: Number(evt.session_id), steps: [] };

        const nextStep = {
            step: evt.step,
            label: STEP_LABELS[evt.step] || evt.step.replace(/_/g, ' '),
            status: statusFromEvent(evt.status),
            timestamp: evt.timestamp || new Date().toISOString(),
            meta: evt.meta || {}
        };

        const idx = existing.steps.findIndex((s) => s.step === evt.step);
        if (idx > -1) {
            existing.steps[idx] = {
                ...existing.steps[idx],
                ...nextStep
            };
        } else {
            existing.steps.push(nextStep);
        }

        existing.steps.sort((a, b) => {
            const orderDiff = stepSortIndex(a.step) - stepSortIndex(b.step);
            if (orderDiff !== 0) return orderDiff;
            return new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime();
        });

        snapshot[turnId] = existing;
        turnProgressById.value = snapshot;
    };

    async function getAuthHeaders() {
        const authStore = useAuthStore();
        return {
            headers: {
                Authorization: `Bearer ${authStore.token}`
            }
        };
    }

    function connectWebSocket() {
        if (socket.value) return;

        const authStore = useAuthStore();
        const userId = authStore.user?.id;
        if (!userId) {
            return;
        }

        shouldReconnect.value = true;
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.hostname}:8000/ws/${userId}`;

        socket.value = new WebSocket(wsUrl);

        socket.value.onopen = () => {
            wsConnected.value = true;
        };

        socket.value.onmessage = (event) => {
            try {
                const msg = JSON.parse(event.data);
                if (msg?.type === 'chat_turn_event') {
                    upsertTurnStep(msg);
                }
            } catch {
                // Ignore non-JSON or unknown payloads.
            }
        };

        socket.value.onclose = () => {
            wsConnected.value = false;
            socket.value = null;

            if (shouldReconnect.value) {
                setTimeout(() => {
                    if (!socket.value) connectWebSocket();
                }, 3000);
            }
        };
    }

    function disconnectWebSocket() {
        shouldReconnect.value = false;
        if (socket.value) {
            socket.value.close();
            socket.value = null;
        }
        wsConnected.value = false;
    }

    async function fetchSessions() {
        isLoading.value = true;
        try {
            const headers = await getAuthHeaders();
            const projectStore = useProjectStore();
            const config = { ...headers };
            if (projectStore.currentProjectId) {
                config.params = { project_id: projectStore.currentProjectId };
            }
            const response = await axios.get(`${API_URL}/chat/sessions`, config);
            sessions.value = response.data;
        } catch (e) {
            error.value = e.message;
        } finally {
            isLoading.value = false;
        }
    }

    async function createSession(title = "New Chat") {
        try {
            const headers = await getAuthHeaders();
            const projectStore = useProjectStore();
            const payload = { title };
            if (projectStore.currentProjectId) {
                payload.project_id = projectStore.currentProjectId;
            }
            const response = await axios.post(`${API_URL}/chat/sessions`, payload, headers);
            sessions.value.unshift(response.data);
            currentSession.value = response.data;
            messages.value = [];
            currentContext.value = [];
            resetTurnProgress();
            return response.data;
        } catch (e) {
            error.value = e.message;
            const toast = useToast();
            toast.error("Failed to create new session");
        }
    }

    async function selectSession(sessionId) {
        isLoading.value = true;
        try {
            const headers = await getAuthHeaders();
            const session = sessions.value.find(s => s.id === sessionId);
            if (session) currentSession.value = session;

            const response = await axios.get(`${API_URL}/chat/sessions/${sessionId}/history`, headers);
            messages.value = response.data;
            currentContext.value = [];
            resetTurnProgress();

            if (messages.value.length > 0) {
                for (let i = messages.value.length - 1; i >= 0; i--) {
                    if (messages.value[i].sources && messages.value[i].sources.length > 0) {
                        currentContext.value = messages.value[i].sources;
                        break;
                    }
                }
            }
        } catch (e) {
            error.value = e.message;
        } finally {
            isLoading.value = false;
        }
    }

    async function sendMessage(content, temperature = 0.7, maxTokens = 2800) {
        if (!currentSession.value) return;

        const effectiveTemperature = clampNumber(temperature, 0, 1, 0.7);
        const effectiveMaxTokens = Math.round(clampNumber(maxTokens, 128, 8192, 2800));

        const clientTurnId = createClientTurnId();
        resetTurnProgress();
        activeTurnId.value = clientTurnId;
        turnProgressById.value = {
            [clientTurnId]: {
                sessionId: Number(currentSession.value.id),
                steps: []
            }
        };

        const tempId = Date.now();
        messages.value.push({
            id: tempId,
            role: 'user',
            content: content,
            created_at: new Date().toISOString()
        });

        thinking.value = true;
        currentContext.value = [];
        connectWebSocket();

        try {
            const headers = await getAuthHeaders();
            const response = await axios.post(
                `${API_URL}/chat/sessions/${currentSession.value.id}/message`,
                {
                    content,
                    model: selectedModel.value,
                    temperature: effectiveTemperature,
                    max_tokens: effectiveMaxTokens,
                    client_turn_id: clientTurnId
                },
                headers
            );

            messages.value.push(response.data);

            if (response.data.sources && response.data.sources.length > 0) {
                currentContext.value = response.data.sources;
            }

            const index = sessions.value.findIndex(s => s.id === currentSession.value.id);
            if (index > -1) {
                const s = sessions.value.splice(index, 1)[0];
                s.updated_at = new Date().toISOString();
                sessions.value.unshift(s);
            }
        } catch (e) {
            error.value = "Failed to send message.";
            messages.value.push({
                id: Date.now(),
                role: 'system',
                content: "Error: Failed to send message. Please try again."
            });

            const snapshot = { ...turnProgressById.value };
            const existing = snapshot[clientTurnId] || { sessionId: Number(currentSession.value.id), steps: [] };
            existing.steps = [
                ...existing.steps,
                {
                    step: 'turn_failed',
                    label: STEP_LABELS.turn_failed,
                    status: 'failed',
                    timestamp: new Date().toISOString(),
                    meta: { error: e?.message || 'Request failed' }
                }
            ];
            snapshot[clientTurnId] = existing;
            turnProgressById.value = snapshot;
        } finally {
            thinking.value = false;
        }
    }

    async function clearHistory() {
        try {
            const headers = await getAuthHeaders();
            await axios.delete(`${API_URL}/chat/sessions`, headers);
            sessions.value = [];
            const toast = useToast();
            toast.success("History cleared");
            messages.value = [];
            currentContext.value = [];
            currentSession.value = null;
            resetTurnProgress();
        } catch (e) {
            error.value = "Failed to clear history.";
            const toast = useToast();
            toast.error("Failed to clear history");
        }
    }

    async function sendFeedback(messageId, type) {
        try {
            const headers = await getAuthHeaders();
            await axios.post(`${API_URL}/chat/messages/${messageId}/feedback`, { feedback: type }, headers);
        } catch (e) {
            console.error("Failed to send feedback", e);
            const toast = useToast();
            toast.error("Failed to submit feedback");
        }
    }

    return {
        sessions,
        currentSession,
        messages,
        isLoading,
        thinking,
        error,
        selectedModel,
        availableModels,
        currentContext,
        wsConnected,
        activeTurnId,
        turnProgressById,
        fetchSessions,
        createSession,
        selectSession,
        sendMessage,
        clearHistory,
        sendFeedback,
        connectWebSocket,
        disconnectWebSocket,
        getTurnSteps
    };
});
