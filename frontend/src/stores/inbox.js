import { defineStore } from 'pinia';
import api from '../services/api';

export const useInboxStore = defineStore('inbox', {
    state: () => ({
        count: 0,
        items: [],
        clusters: [], // For merge suggestions
        socket: null,
        connected: false
    }),

    actions: {
        async fetchInbox() {
            try {
                const response = await api.get('/inbox/');
                this.items = response.data;
                this.count = this.items.length;
            } catch (error) {
                console.error('Error fetching inbox:', error);
            }
        },

        async handleAction(id, action, payload = null) {
            try {
                await api.post(`/inbox/${id}/action`, { action, payload });
                // Optimistic update
                this.items = this.items.filter(item => item.id !== id);
                this.count = this.items.length;
            } catch (error) {
                console.error(`Error performing ${action}:`, error);
                // Revert or show toast
            }
        },

        connectWebSocket(userId = '1') { // Default user 1 for now
            if (this.socket) return;

            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${protocol}//${window.location.hostname}:8000/ws/${userId}`;

            this.socket = new WebSocket(wsUrl);

            this.socket.onopen = () => {
                this.connected = true;
                console.log('WS Connected');
            };

            this.socket.onmessage = (event) => {
                const msg = JSON.parse(event.data);
                if (msg.type === 'new_memory' || msg.type === 'inbox_update' || msg.type === 'new_cluster') {
                    this.fetchInbox(); // Refresh list
                }
            };

            this.socket.onclose = () => {
                this.connected = false;
                this.socket = null;
                // Reconnect logic could go here
            };
        }
    }
});
