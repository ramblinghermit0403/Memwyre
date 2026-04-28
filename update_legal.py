import re

def update_file(filepath):
    with open('frontend/src/views/PricingView.vue', 'r', encoding='utf-8') as f:
        pricing_content = f.read()

    # Extract CTA block
    cta_match = re.search(r'(    <!-- Final CTA Section: Memory and Personality -->.*?    </div>\n\n)', pricing_content, re.DOTALL)
    cta_block = cta_match.group(1)

    # Extract Style block
    style_match = re.search(r'(<style scoped>\n\.force-light.*?</style>)', pricing_content, re.DOTALL)
    style_block = style_match.group(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update root div
    content = re.sub(
        r'<div class="(terms-view|privacy-policy-view) bg-app text-text-primary min-h-screen py-24 px-4 sm:px-6 lg:px-8 font-sans selection:bg-primary selection:text-white dark:selection:bg-primary dark:selection:text-white transition-colors duration-300">',
        r'<div class="\1 force-light bg-app text-text-primary min-h-screen font-sans selection:bg-primary selection:text-white transition-colors duration-300 overflow-x-hidden">\n    <div class="py-24 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto flex flex-col md:flex-row gap-12 items-start">',
        content
    )
    # Because we added a div wrapper, we need to remove the max-w-6xl from the inner flex container
    content = content.replace(
        '<div class="max-w-6xl mx-auto flex flex-col md:flex-row gap-12 items-start">',
        ''
    )

    # 2. Remove mobile footer
    content = re.sub(r'        <!-- Mobile Footer.*?</div>\n', '', content, flags=re.DOTALL)

    # 3. Add CTA block before </template>
    content = content.replace('    </div>\n  </div>\n</template>', f'    </div>\n  </div>\n{cta_block}\n  </div>\n</template>')

    # 4. Add LogoBgAnimation import
    if 'LogoBgAnimation' not in content:
        content = content.replace('<script setup>\nimport { onMounted } from \'vue\';', '<script setup>\nimport { onMounted } from \'vue\';\nimport LogoBgAnimation from \'@/components/landing/LogoBgAnimation.vue\';')

    # 5. Add style block
    if '.force-light' not in content:
        content = content + '\n\n' + style_block + '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('frontend/src/views/TermsView.vue')
update_file('frontend/src/views/PrivacyPolicyView.vue')
