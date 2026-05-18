def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find start and end of tiles-bottom-left
    start_idx = -1
    for i, line in enumerate(lines):
        if 'id="tiles-bottom-left"' in line:
            start_idx = i
            break
            
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if 'id="patch-tile"' in lines[i]:
            end_idx = i
            break

    # Find shadows to separate tiles
    shadow_indices = []
    for i in range(start_idx, end_idx):
        if 'opacity="0.55"' in lines[i] and 'filter=' in lines[i]:
            shadow_indices.append(i)
            
    # Add the end of the last tile
    shadow_indices.append(end_idx - 1)

    # We need Tile 4 and Tile 15
    t4_s = shadow_indices[4]
    t4_e = shadow_indices[5]
    
    t15_s = shadow_indices[15]
    t15_e = shadow_indices[16]

    tile4_lines = lines[t4_s:t4_e]
    tile15_lines = lines[t15_s:t15_e]
    
    dx = -564.665
    dy = 324.44
    
    # Wrap in transforms
    t4_wrapped = [f'<g transform="translate({dx}, {dy})">\n'] + tile4_lines + ['</g>\n']
    t15_wrapped = [f'<g transform="translate({-dx}, {-dy})">\n'] + tile15_lines + ['</g>\n']

    # Now replace them in the file.
    # Since we are replacing lines, we should do it from bottom to top to avoid index shifting!
    new_lines = lines.copy()
    
    new_lines[t15_s:t15_e] = t4_wrapped
    new_lines[t4_s:t4_e] = t15_wrapped

    with open('src/assets/motion/processsor.svg', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("Swapped Tile 4 and Tile 15 with translates!")

if __name__ == "__main__":
    run()
