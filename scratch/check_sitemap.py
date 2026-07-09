import xml.etree.ElementTree as ET

sitemap_path = r"c:\Users\himan\OneDrive\Documents\brain_vault\frontend\public\sitemap.xml"

# Parse XML
tree = ET.parse(sitemap_path)
root = tree.getroot()

# Namespaces
namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

urls = []
for url in root.findall("ns:url", namespace):
    loc = url.find("ns:loc", namespace)
    if loc is not None:
        urls.append(loc.text)

print(f"Total URLs in sitemap: {len(urls)}")

# Check duplicates
duplicates = []
seen = set()
for u in urls:
    if u in seen:
        duplicates.append(u)
    seen.add(u)

print(f"Duplicate URLs found: {len(duplicates)}")
for d in duplicates:
    print(f"  - {d}")

# Check redirecting URLs (trailing slash rules)
# Rules: 
# - /docs/* must have a trailing slash
# - SPA pages (all other paths) must NOT have a trailing slash (except homepage /)
redirecting = []
for u in urls:
    path = u.replace("https://memwyre.tech", "")
    if path.startswith("/docs"):
        if not path.endswith("/"):
            redirecting.append((u, "Needs trailing slash (redirects to " + u + "/)"))
    else:
        if path != "/" and path.endswith("/"):
            redirecting.append((u, "Should NOT have trailing slash (redirects to " + u[:-1] + ")"))

print(f"Redirecting URLs found: {len(redirecting)}")
for u, reason in redirecting:
    print(f"  - {u} ({reason})")
