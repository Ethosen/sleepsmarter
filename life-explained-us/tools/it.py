"""Minimal InnerTube client over youtubei.googleapis.com (the only YouTube host reachable here)."""
import json, sys, urllib.request

BASE = "https://youtubei.googleapis.com/youtubei/v1/"
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20260918.00.00", "hl": "en", "gl": "US"}}


def call(endpoint, **body):
    body["context"] = CTX
    req = urllib.request.Request(BASE + endpoint + "?prettyPrint=false", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def walk(o, key):
    """Yield every value stored under `key` anywhere in a nested JSON object."""
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v, key)


def text(t):
    if not t:
        return ""
    if "simpleText" in t:
        return t["simpleText"]
    if "runs" in t:
        return "".join(r.get("text", "") for r in t["runs"])
    if "content" in t:
        return t["content"]
    return ""


if __name__ == "__main__":
    ep = sys.argv[1]
    print(json.dumps(call(ep, **json.loads(sys.argv[2])), ensure_ascii=False))
