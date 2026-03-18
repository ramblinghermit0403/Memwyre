import api from './api';

export const composeContext = async ({ itemIds = [], projectId = null, maxChars = 2800 } = {}) => {
  const response = await api.post('/context/compose', {
    item_ids: itemIds,
    project_id: projectId,
    max_chars: maxChars,
  });
  return response.data;
};
