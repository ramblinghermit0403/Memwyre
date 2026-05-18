import re
import math

def run():
    with open('src/assets/motion/processsor.svg', 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    shadow_indices = []
    for i in range(start_idx, end_idx):
        if 'opacity="0.55"' in lines[i] and 'filter=' in lines[i]:
            shadow_indices.append(i)

    tiles = []
    for idx, shadow_line in enumerate(shadow_indices):
        next_shadow = shadow_indices[idx + 1] if idx + 1 < len(shadow_indices) else end_idx
        tile_content = ''.join(lines[shadow_line:next_shadow])
        
        # Find the transform of the top white rect to get X/Y
        # <rect width="124.331" height="124.331" rx="34" transform="matrix(0.866025 -0.5 0.902002 0.431732 X Y)" fill="white" />
        match = re.search(r'transform="matrix\([^)]+\s+([-0-9.]+)\s+([-0-9.]+)\)"\s+fill="white"', tile_content)
        x, y = 0, 0
        if match:
            x, y = float(match.group(1)), float(match.group(2))

        clip_match = re.search(r'clip-path="url\(#([^"]+)\)"', tile_content)
        clip_id = clip_match.group(1) if clip_match else "none"
        
        colors = re.findall(r'fill="([^"]+)"', tile_content)
        colors = [c for c in colors if c not in ('#474747', '#D7D7D7', 'white', '#777777', '#111111', 'url(#pattern0_18_1617)')]
        
        # Is it Notion (Envelope)?
        name = "Unknown"
        if '#26251E' in colors: name = "Notion"
        elif '#1A73E8' in tile_content: name = "Chrome"
        elif 'url(#paint1_linear_18_1617)' in colors: name = "Edge"
        elif 'url(#paint10_linear_18_1617)' in colors: name = "ChatGPT"
        elif '#4B73FF' in colors: name = "Sparkle"
        
        tiles.append({
            "index": idx,
            "x": x,
            "y": y,
            "name": name,
            "colors": list(set(colors))
        })
        
    for t in tiles:
        print(f"Tile {t['index']}: {t['name']} at ({t['x']}, {t['y']})")
        
    # Calculate distances to find neighbors
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            dx = tiles[i]['x'] - tiles[j]['x']
            dy = tiles[i]['y'] - tiles[j]['y']
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 250: # Arbitrary threshold for neighbors
                print(f"Neighbor: {i} ({tiles[i]['name']}) and {j} ({tiles[j]['name']}) - Dist: {dist:.1f}")

if __name__ == "__main__":
    run()
