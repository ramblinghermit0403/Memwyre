import re

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
        
        match = re.search(r'transform="matrix\([^)]+\s+([-0-9.]+)\s+([-0-9.]+)\)"\s+fill="white"', tile_content)
        x, y = 0, 0
        if match:
            x, y = float(match.group(1)), float(match.group(2))

        logo_type = "Unknown"
        if '#1A73E8' in tile_content: logo_type = "Chrome"
        elif 'fill="#111111"' in tile_content and 'fill-rule="evenodd"' in tile_content: logo_type = "Gear"
        elif 'fill="#FF4D4D"' in tile_content: logo_type = "Crab"
        elif 'mask=' in tile_content: logo_type = "Sparkle"
        elif 'fill="#3186FF"' in tile_content: logo_type = "Bluetooth"
        elif '#26251E' in tile_content: logo_type = "Notion"
        elif 'clip-path="url(#clip2_18_1617)"' in tile_content: logo_type = "OpenAI"
        elif 'clip-path="url(#clip3_18_1617)"' in tile_content: logo_type = "Edge"
        elif 'clip-path="url(#clip6_18_1617)"' in tile_content: logo_type = "Claude"
        elif 'clip-path="url(#clip7_18_1617)"' in tile_content: logo_type = "Heart"
        elif 'clip-path="url(#clip8_18_1617)"' in tile_content: logo_type = "UnknownBlue"
        elif 'clip-path="url(#clip12_18_1617)"' in tile_content: logo_type = "Sparkle2?"
        else:
            clip_match = re.search(r'clip-path="url\(#([^"]+)\)"', tile_content)
            logo_type = clip_match.group(1) if clip_match else "None"
        
        tiles.append({"index": idx, "x": x, "y": y, "name": logo_type})
        
    for t in tiles:
        print(f"Tile {t['index']}: {t['name']} at ({t['x']}, {t['y']})")

if __name__ == "__main__":
    run()
