def run():
    # Tile positions and names from previous output
    tiles = [
        (0, "OpenAI", 484.0, 1911.28),
        (1, "Edge", 511.938, 2068.43),
        (2, "Notion", 668.217, 1803.89),
        (3, "Chrome", 696.155, 1961.05),
        (4, "Notion", 861.165, 1694.76),
        (5, "Claude", 889.103, 1851.91),
        (6, "Heart", 1057.61, 1583.01),
        (7, "UnknownBlue", 1085.54, 1740.16),
        (8, "Gear", 1247.06, 1473.88),
        (9, "Bluetooth", 1275.0, 1631.03),
        (10, "Sparkle", 1437.47, 1362.17),
        (11, "Crab", 1465.41, 1519.32),
        (12, "Sparkle2?", -83.3946, 2240.01),
        (13, "Gear", 106.061, 2130.88),
        (14, "Bluetooth", 133.999, 2288.03),
        (15, "Sparkle", 296.472, 2019.17),
        (16, "Crab", 324.41, 2176.32)
    ]
    
    # Grid coordinates
    # DX = ~190, DY = -109
    
    for t in tiles:
        print(f"Tile {t[0]:2d}: {t[1]:15s} X={t[2]:8.1f} Y={t[3]:8.1f}")
        
    print("\nAdjacency list (dist < 250):")
    import math
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            dx = tiles[i][2] - tiles[j][2]
            dy = tiles[i][3] - tiles[j][3]
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 250:
                print(f"  {tiles[i][1]} ({i}) is next to {tiles[j][1]} ({j}) - dist {dist:.1f}")

if __name__ == "__main__":
    run()
