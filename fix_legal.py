import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Memwyre typo
    content = content.replace('Memwyre', 'Memwyre')

    # Add LogoBgAnimation import if missing
    if 'import LogoBgAnimation' not in content:
        content = content.replace(
            "import { onMounted } from 'vue';",
            "import { onMounted } from 'vue';\nimport LogoBgAnimation from '@/components/landing/LogoBgAnimation.vue';"
        )

    # Make background white (light themed)
    content = content.replace('bg-app', 'bg-[#FAF6F0]') # Match force-light bg-app color explicitly or just use bg-white
    
    # Or actually let's replace `bg-app` with `bg-[#FAF6F0]`
    content = content.replace('bg-surface', 'bg-white')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('frontend/src/views/PrivacyPolicyView.vue')
fix_file('frontend/src/views/TermsView.vue')
