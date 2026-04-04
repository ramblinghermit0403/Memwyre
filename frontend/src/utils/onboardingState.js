const PREFIX = 'memwyre:onboarding';

const LEGACY_KEY_MAP = {
  completed: 'hasCompletedOnboarding',
  first_action_done: 'onboarding_first_memory_started',
  tour_completed: 'tour_completed',
  tour_requested: 'tour_requested',
  selected_type: 'onboarding_selected_type',
  step: 'onboarding_step',
};

const normalizeScope = (userOrId) => {
  if (typeof userOrId === 'object' && userOrId !== null) {
    return String(userOrId.id || userOrId.email || 'anonymous');
  }
  if (userOrId === null || userOrId === undefined || userOrId === '') return 'anonymous';
  return String(userOrId);
};

export const onboardingScopedKey = (userOrId, key) => `${PREFIX}:${normalizeScope(userOrId)}:${key}`;

export const onboardingLegacyKeys = { ...LEGACY_KEY_MAP };

export const migrateOnboardingLegacyState = (storage, userOrId) => {
  if (!storage || typeof storage.getItem !== 'function' || typeof storage.setItem !== 'function') return;

  Object.entries(LEGACY_KEY_MAP).forEach(([scopedName, legacyKey]) => {
    const scopedKey = onboardingScopedKey(userOrId, scopedName);
    const scopedValue = storage.getItem(scopedKey);
    if (scopedValue !== null) return;

    const legacyValue = storage.getItem(legacyKey);
    if (legacyValue !== null) {
      storage.setItem(scopedKey, legacyValue);
    }
  });
};

export const readScopedBoolean = (storage, userOrId, key, fallback = false) => {
  if (!storage || typeof storage.getItem !== 'function') return fallback;
  const value = storage.getItem(onboardingScopedKey(userOrId, key));
  if (value === null) return fallback;
  return value === 'true';
};

export const writeScopedBoolean = (storage, userOrId, key, value) => {
  if (!storage || typeof storage.setItem !== 'function') return;
  storage.setItem(onboardingScopedKey(userOrId, key), value ? 'true' : 'false');
};

export const readScopedString = (storage, userOrId, key, fallback = '') => {
  if (!storage || typeof storage.getItem !== 'function') return fallback;
  const value = storage.getItem(onboardingScopedKey(userOrId, key));
  return value === null ? fallback : value;
};

export const writeScopedString = (storage, userOrId, key, value) => {
  if (!storage || typeof storage.setItem !== 'function') return;
  storage.setItem(onboardingScopedKey(userOrId, key), String(value));
};

