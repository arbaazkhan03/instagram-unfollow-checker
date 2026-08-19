#!/usr/bin/env python3
"""
Analyze following.json timestamps to detect automated (bot) follow bursts.
Humans follow a few accounts here and there. Automation follows many in seconds.
"""

import json
import os
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
FOLLOWING = os.path.join(BASE, "connections", "followers_and_following", "following.json")


def load():
    with open(FOLLOWING, encoding="utf-8") as f:
        data = json.load(f)
    entries = data.get("relationships_following", data)
    rows = []
    for e in entries:
        for item in e.get("string_list_data", []):
            ts = item.get("timestamp")
            name = item.get("value") or e.get("title")
            if ts:
                rows.append((ts, name))
    rows.sort()
    return rows


def main():
    rows = load()
    if not rows:
        print("No timestamped follows found.")
        return

    first = datetime.fromtimestamp(rows[0][0], timezone.utc)
    last = datetime.fromtimestamp(rows[-1][0], timezone.utc)
    print(f"Total follows: {len(rows)}")
    print(f"Range: {first:%Y-%m-%d} to {last:%Y-%m-%d}\n")

    # Group follows that happen close together (<= 60s apart) into a "burst".
    bursts = []
    cur = [rows[0]]
    for prev, curr in zip(rows, rows[1:]):
        if curr[0] - prev[0] <= 60:
            cur.append(curr)
        else:
            bursts.append(cur)
            cur = [curr]
    bursts.append(cur)

    big = [b for b in bursts if len(b) >= 5]
    print(f"Suspicious bursts (5+ follows within 60s of each other): {len(big)}\n")

    total_in_bursts = 0
    for b in sorted(big, key=len, reverse=True)[:15]:
        start = datetime.fromtimestamp(b[0][0], timezone.utc)
        span = b[-1][0] - b[0][0]
        total_in_bursts += len(b)
        rate = len(b) / span if span else len(b)
        print(f"  {start:%Y-%m-%d %H:%M:%S} UTC  |  {len(b):>3} follows in {span:>4}s  (~{rate:.1f}/sec)")
        sample = ", ".join(n for _, n in b[:5])
        print(f"       e.g. {sample} ...")

    burst_follows = sum(len(b) for b in big)
    print(f"\n{burst_follows} of {len(rows)} follows "
          f"({100*burst_follows/len(rows):.0f}%) happened in rapid bursts.")


if __name__ == "__main__":
    main()
