import { defineStore } from 'pinia';
import { ref } from 'vue';
import { listProjects, createProject as apiCreateProject } from '../services/projects';

function getStorage() {
    if (typeof localStorage !== 'undefined') return localStorage;
    return {
        getItem: () => null,
        setItem: () => { },
        removeItem: () => { },
    };
}

export const useProjectStore = defineStore('project', () => {
    const storage = getStorage();
    const projects = ref([]);
    const currentProjectId = ref(null);
    const loading = ref(false);

    const setCurrentProjectId = (id) => {
        const numericId = id ? Number(id) : null;
        currentProjectId.value = numericId;
        if (numericId) {
            storage.setItem('selectedProjectId', String(numericId));
        } else {
            storage.removeItem('selectedProjectId');
        }
    };

    const fetchProjects = async () => {
        loading.value = true;
        try {
            const list = await listProjects(false);
            projects.value = list || [];
            
            // Try to resolve current project ID
            const savedIdStr = storage.getItem('selectedProjectId');
            const savedId = savedIdStr ? Number(savedIdStr) : null;
            
            // Check if saved ID exists in our project list
            const exists = projects.value.some(p => p.id === savedId);
            if (exists && savedId) {
                currentProjectId.value = savedId;
            } else {
                // Find project named 'default'
                const defaultProj = projects.value.find(p => p.name === 'default');
                if (defaultProj) {
                    currentProjectId.value = defaultProj.id;
                    storage.setItem('selectedProjectId', String(defaultProj.id));
                } else if (projects.value.length > 0) {
                    // Fallback to first project
                    currentProjectId.value = projects.value[0].id;
                    storage.setItem('selectedProjectId', String(projects.value[0].id));
                } else {
                    currentProjectId.value = null;
                }
            }
        } catch (error) {
            console.error('Failed to fetch projects in store:', error);
        } finally {
            loading.value = false;
        }
    };

    const createNewProject = async (name) => {
        loading.value = true;
        try {
            const payload = { name };
            const newProj = await apiCreateProject(payload);
            await fetchProjects();
            if (newProj && newProj.id) {
                setCurrentProjectId(newProj.id);
            }
            return newProj;
        } catch (error) {
            console.error('Failed to create project in store:', error);
            throw error;
        } finally {
            loading.value = false;
        }
    };

    return {
        projects,
        currentProjectId,
        loading,
        setCurrentProjectId,
        fetchProjects,
        createNewProject,
    };
});
