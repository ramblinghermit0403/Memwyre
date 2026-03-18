import api from './api';

export const listProjects = async (includeArchived = false) => {
  const response = await api.get('/projects/', { params: { include_archived: includeArchived } });
  return response.data;
};

export const createProject = async (payload) => {
  const response = await api.post('/projects/', payload);
  return response.data;
};

export const updateProject = async (projectId, payload) => {
  const response = await api.put(`/projects/${projectId}`, payload);
  return response.data;
};

export const archiveProject = async (projectId) => {
  const response = await api.delete(`/projects/${projectId}`);
  return response.data;
};
