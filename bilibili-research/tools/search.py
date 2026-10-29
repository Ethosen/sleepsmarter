"""Run YouTube searches and summarize: top results, channel concentration, views."""
import json, sys, re, collections
from it import call, walk, text

def views(s):
    s = s.replace(',', '').lower()
    m = re.match(r'([\d.]+)\s*([km]?)', s)
    if not m: return 0
    n = float(m.group(1)); return int(n * {'k': 1e3, 'm': 1e6, '': 1}[m.group(2)])

for q in sys.argv[1:]:
    r = call('search', query=q)
    vids = []
    for v in walk(r, 'videoRenderer'):
        vids.append((text(v.get('title')), text(v.get('ownerText')), text(v.get('viewCountText')), text(v.get('publishedTimeText'))))
    chans = collections.Counter(c for _, c, _, _ in vids)
    print(f"\n### {q}  ({len(vids)} results)")
    for t, c, vw, p in vids[:8]:
        print(f"  {vw:>16} | {p:>14} | {c[:28]:28} | {t[:80]}")
    print("  channels with 2+ hits:", [c for c, n in chans.items() if n >= 2])
