def run():
    tiles = [
        (0, "OpenAI", 484.0, 1911.3), (1, "Edge", 511.9, 2068.4), (2, "Notion", 668.2, 1803.9), 
        (3, "Chrome", 696.2, 1961.0), (4, "Notion", 861.2, 1694.8), (5, "Claude", 889.1, 1851.9), 
        (6, "Heart", 1057.6, 1583.0), (7, "UnknownBlue", 1085.5, 1740.2), (8, "Gear", 1247.1, 1473.9), 
        (9, "Bluetooth", 1275.0, 1631.0), (10, "Sparkle", 1437.5, 1362.2), (11, "Crab", 1465.4, 1519.3), 
        (12, "Sparkle2", -83.4, 2240.0), (13, "Gear", 106.1, 2130.9), (14, "Bluetooth", 134.0, 2288.0), 
        (15, "Sparkle", 296.5, 2019.2), (16, "Crab", 324.4, 2176.3)
    ]
    
    # Let's project X and Y into a simple integer grid
    # dx = ~190, dy = ~ -109
    
    # We can calculate row and col
    # x = col * 190 + row * 190
    # y = -col * 109 + row * 109  (approx)
    
    # better to just sort them by Y and see rows
    tiles.sort(key=lambda t: t[3])
    for t in tiles:
        print(f"Y={t[3]:6.1f} X={t[2]:6.1f} : {t[1]} ({t[0]})")

if __name__ == "__main__":
    run()
