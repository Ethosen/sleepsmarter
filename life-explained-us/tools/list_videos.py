"""List all videos and shorts of a channel via InnerTube browse + continuations."""
import json, sys
from it import call, walk, text

CHANNEL = sys.argv[1]
TABS = {"videos": "EgZ2aWRlb3PyBgQKAjoA", "shorts": "EgZzaG9ydHPyBgUKA5oBAA%3D%3D"}


def items_of(resp):
    out = []
    for v in walk(resp, "videoRenderer"):
        out.append({"id": v["videoId"], "title": text(v.get("title")), "views": text(v.get("viewCountText")),
                    "length": text(v.get("lengthText")), "published": text(v.get("publishedTimeText")), "type": "video"})
    for v in walk(resp, "lockupViewModel"):
        md = v.get("metadata", {}).get("lockupMetadataViewModel", {})
        rows = [p.get("text", {}).get("content", "") for r in walk(md, "metadataRows") for row in r
                for p in row.get("metadataParts", [])]
        badges = [b.get("text", "") for b in walk(v, "thumbnailBadgeViewModel")]
        out.append({"id": v.get("contentId"), "title": md.get("title", {}).get("content", ""),
                    "meta": rows, "length": ",".join(badges), "type": "video"})
    for v in walk(resp, "shortsLockupViewModel"):
        vid = next(walk(v, "videoId"), None)
        out.append({"id": vid, "title": v.get("overlayMetadata", {}).get("primaryText", {}).get("content", ""),
                    "views": v.get("overlayMetadata", {}).get("secondaryText", {}).get("content", ""), "type": "short"})
    return out


def tokens(resp):
    return [c["continuationCommand"]["token"] for c in walk(resp, "continuationEndpoint") if "continuationCommand" in c]


result = {}
for tab, params in TABS.items():
    resp = call("browse", browseId=CHANNEL, params=params)
    if tab == "videos":
        result["header"] = {k: next(walk(resp, k), None) for k in ("title", "description")}
        result["metadata"] = next(walk(resp, "channelMetadataRenderer"), {})
        result["pageHeader"] = next(walk(resp, "pageHeaderViewModel"), {})
    found = items_of(resp)
    seen = set()
    toks = tokens(resp)
    while toks:
        t = toks.pop(0)
        if t in seen:
            continue
        seen.add(t)
        r = call("browse", continuation=t)
        found += items_of(r)
        toks += tokens(r)
    result[tab] = found
    print(tab, len(found), file=sys.stderr)

json.dump(result, open("channel.json", "w"), ensure_ascii=False, indent=1)
