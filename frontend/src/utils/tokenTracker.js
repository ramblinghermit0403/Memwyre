import api from '../api';

/**
 * Frontend Token Tracker Utility
 * Interacts with backend TokenTracker API for exact multi-cloud token counts & cost estimates.
 */
export async function countTokens(text, provider = 'openai', modelName = 'gpt-4o') {
  if (!text) return { tokens_count: 0, estimated_cost: 0 };
  
  try {
    const response = await api.post('/tokens/count', {
      text,
      provider,
      model_name: modelName
    });
    return response.data;
  } catch (err) {
    // Client-side fallback if offline
    const count = Math.max(1, Math.floor(text.length / 4));
    return {
      tokens_count: count,
      estimated_cost: Number(((count / 1000000) * 2.5).toFixed(6)),
      provider,
      model_name: modelName,
      normalized_model: `${provider}/${modelName}`
    };
  }
}

export function formatTokenCount(tokens) {
  if (!tokens || tokens <= 0) return '0';
  if (tokens >= 1000000) return `${(tokens / 1000000).toFixed(1)}M`;
  if (tokens >= 1000) return `${(tokens / 1000).toFixed(1)}k`;
  return tokens.toLocaleString();
}
