import re

def update_file(filepath):
    with open('frontend/src/views/PricingView.vue', 'r', encoding='utf-8') as f:
        pricing_content = f.read()

    # Extract CTA and Footer block
    cta_match = re.search(r'(    <!-- Final CTA Section: Memory and Personality -->.*?)\n  </div>\n</template>', pricing_content, re.DOTALL)
    cta_block = cta_match.group(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the partial CTA that was added
    content = re.sub(r'    <!-- Final CTA Section: Memory and Personality -->.*?</template>', '</template>', content, flags=re.DOTALL)

    # Insert the full CTA block before </template>
    content = content.replace('</template>', f'{cta_block}\n  </div>\n</template>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('frontend/src/views/TermsView.vue')
update_file('frontend/src/views/PrivacyPolicyView.vue')
