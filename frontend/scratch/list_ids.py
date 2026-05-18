import re

def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        content = f.read()

    ids = re.findall(r'<g[^>]*id="([^"]+)"', content)
    for id_ in ids:
        print(f"Group ID: {id_}")

if __name__ == "__main__":
    run()
