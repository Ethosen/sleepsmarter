"""Gap analysis on YouTube search: supply (how many relevant videos/channels) vs demand (their views).

Usage: python3 gap.py [--hl zh-CN] "query 1" "query 2" ...
Pulls 2 pages of results per query (~40 videos).
"""
import json, re, sys, statistics, collections
import it
from it import call, walk, text

args = sys.argv[1:]
if args and args[0] == "--hl":
    it.CTX = {"client": {**it.CTX["client"], "hl": args[1], "gl": "US"}}
    args = args[2:]


def num(s):
    s = (s or "").replace(",", "").lower()
    m = re.search(r"([\d.]+)\s*([kmb万亿]?)", s)
    if not m:
        return 0
    return int(float(m.group(1)) * {"k": 1e3, "m": 1e6, "b": 1e9, "万": 1e4, "亿": 1e8, "": 1}[m.group(2)])


def age_months(s):
    s = (s or "").lower()
    m = re.search(r"(\d+)\s*(hour|day|week|month|year)", s)
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2)
    return n * {"hour": 0, "day": 1 / 30, "week": 0.25, "month": 1, "year": 12}[u]


def results(q):
    r = call("search", query=q)
    out = list(walk(r, "videoRenderer"))
    tok = next((c["continuationCommand"]["token"] for c in walk(r, "continuationEndpoint")
                if "continuationCommand" in c), None)
    if tok:
        out += list(walk(call("search", continuation=tok), "videoRenderer"))
    return out


for q in args:
    vids = []
    for v in results(q):
        vids.append({"t": text(v.get("title")), "c": text(v.get("ownerText")),
                     "v": num(text(v.get("viewCountText"))), "age": age_months(text(v.get("publishedTimeText"))),
                     "len": text(v.get("lengthText"))})
    if not vids:
        print(f"\n### {q}: no results")
        continue
    views = [x["v"] for x in vids]
    big = [x for x in vids if x["v"] >= 100_000]
    recent_big = [x for x in big if x["age"] is not None and x["age"] <= 12]
    chans = collections.Counter(x["c"] for x in vids)
    print(f"\n### {q}")
    print(f"  n={len(vids)} | median views={int(statistics.median(views)):,} | >=100k: {len(big)} "
          f"| >=100k & <=12 mo: {len(recent_big)} | distinct channels: {len(chans)} "
          f"| series channels (3+): {[c for c, n in chans.items() if n >= 3]}")
    for x in sorted(vids, key=lambda x: -x["v"])[:6]:
        age = "?" if x["age"] is None else f"{x['age']:.0f}mo"
        print(f"   {x['v']:>12,} | {age:>5} | {x['len']:>8} | {x['c'][:24]:24} | {x['t'][:75]}")
