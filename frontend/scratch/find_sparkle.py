def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if 'clip14_18_1617' in line or 'clip10_18_1617' in line:
            print(f"Line {i+1}: {line.strip()[:100]}")

if __name__ == '__main__':
    run()
