import os

# Base directory
base_dir = r"c:\Users\himan\OneDrive\Documents\brain_vault"

# Excluded directories
exclude_dirs = {'.git', 'node_modules', 'venv', '.gemini', 'dist', '.dist', '__pycache__', '.temp_research'}

# Excluded extensions
exclude_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.webm', '.pyc'}

matches = []

for root, dirs, files in os.walk(base_dir):
    # Filter directories in-place to prevent os.walk from entering them
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        _, ext = os.path.splitext(file.lower())
        if ext in exclude_exts:
            continue
        
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if 'MemWyre' in content:
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        if 'MemWyre' in line:
                            matches.append((filepath, idx + 1, line.strip()))
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

print(f"Found {len(matches)} occurrences of 'MemWyre':")
for filepath, line_num, content in matches:
    rel_path = os.path.relpath(filepath, base_dir)
    print(f"{rel_path}:{line_num}: {content}")
