import re

with open('frontend/src/views/SettingsView.vue', 'r') as f:
    content = f.read()

correct_block = """    } catch (err) {
        toast.error("Failed to generate key");
    } finally {
        generatingKey.value = false;
    }
};

const copyGeneratedKey = async () => {
    if (justGeneratedKey.value) {
        await navigator.clipboard.writeText(justGeneratedKey.value);
        keyCopied.value = true;
        toast.success("Key copied to clipboard");
        setTimeout(() => keyCopied.value = false, 2000);
    }
};

const toggleAutoApprove = async () => {
  const newVal = !settings.value.auto_approve;
  settings.value.auto_approve = newVal;
  try {
    await api.patch('/user/settings', { auto_approve: newVal });
    toast.success("Settings updated");
  } catch (err) {
    settings.value.auto_approve = !newVal; // revert
    toast.error("Failed to update settings");
  }
};

const loadKeys = async () => {
  try {
    const res = await api.get('/user/llm-keys');
    keys.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

const loadSettings = async () => {
  try {
    const res = await api.get('/user/settings');
    settings.value = { ...settings.value, ...res.data };
  } catch (err) {
    console.error(err);
  }
};

const addKey = async () => {"""

bad_block = """    } catch (err) {
        toast.error("Failed to generate key");
  } catch (err) {
    console.error(err);
  }
};

const addKey = async () => {"""

if bad_block in content:
    content = content.replace(bad_block, correct_block)
    with open('frontend/src/views/SettingsView.vue', 'w') as f:
        f.write(content)
    print("Done")
else:
    print("Bad block not found")
