import re

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

    # Find shadows
    shadow_indices = []
    for i in range(start_idx, end_idx):
        if 'opacity="0.55"' in lines[i] and 'filter=' in lines[i]:
            shadow_indices.append(i)

    # Tile 4 is index 4. Tile 15 is index 15.
    tile4_start = shadow_indices[4]
    tile4_end = shadow_indices[5]
    
    tile15_start = shadow_indices[15]
    tile15_end = shadow_indices[16]
    
    tile4_lines = lines[tile4_start:tile4_end]
    tile15_lines = lines[tile15_start:tile15_end]
    
    print(f"Tile 4 lines: {tile4_start} to {tile4_end}")
    print(f"Tile 15 lines: {tile15_start} to {tile15_end}")
    
    # Let's find the logo start and end inside the tile
    # A tile has: shadow <g>, white rect <g>, logo <g> or <path>.
    # The logo starts after the white rect's </g>
    def get_logo_range(t_lines):
        logo_start = -1
        logo_end = -1
        g_count = 0
        in_white_rect = False
        
        for i, line in enumerate(t_lines):
            if 'fill="white"' in line:
                in_white_rect = True
            if in_white_rect and '</g>' in line:
                logo_start = i + 1
                break
                
        # The logo goes until the end of the tile lines
        logo_end = len(t_lines)
        return logo_start, logo_end

    l4_s, l4_e = get_logo_range(tile4_lines)
    l15_s, l15_e = get_logo_range(tile15_lines)
    
    print("Tile 4 logo:")
    print("".join(tile4_lines[l4_s:l4_e]))
    
    print("Tile 15 logo:")
    print("".join(tile15_lines[l15_s:l15_e]))

if __name__ == "__main__":
    run()
