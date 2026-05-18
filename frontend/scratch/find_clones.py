import re
def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        content = f.read()
    clones = re.findall(r'<g[^>]*id="([^"]*clone[^"]*)"', content)
    print("Clones found:", clones)
if __name__ == '__main__':
    run()
