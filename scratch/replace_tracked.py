import subprocess
import os

def run_git_ls_files():
    try:
        output = subprocess.check_output(["git", "ls-files"], text=True)
        return [line.strip() for line in output.splitlines() if line.strip()]
    except Exception as e:
        print(f"Error running git ls-files: {e}")
        return []

def main():
    base_dir = r"c:\Users\himan\OneDrive\Documents\brain_vault"
    files = run_git_ls_files()
    
    print(f"Found {len(files)} tracked files. Scanning for 'MemWyre'...")
    
    modified_files = 0
    total_replacements = 0
    
    # Exclude binaries by checking extension
    exclude_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.webm', '.pdf'}
    
    for rel_path in files:
        _, ext = os.path.splitext(rel_path.lower())
        if ext in exclude_exts:
            continue
            
        filepath = os.path.join(base_dir, rel_path)
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            if 'MemWyre' in content:
                count = content.count('MemWyre')
                new_content = content.replace('MemWyre', 'Memwyre')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Replaced {count} occurrence(s) in: {rel_path}")
                modified_files += 1
                total_replacements += count
        except Exception as e:
            print(f"Error processing {rel_path}: {e}")
            
    print(f"\nDone! Modified {modified_files} files, made {total_replacements} replacements.")

if __name__ == '__main__':
    main()
