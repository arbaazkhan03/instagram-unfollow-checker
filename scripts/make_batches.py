#!/usr/bin/env python3
"""
Split not_following_back.txt into daily batches with clickable links,
so you can unfollow at a safe pace.

Usage:
    python3 make_batches.py [batch_size]   # default batch size = 120
"""

import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "connections", "followers_and_following", "not_following_back.txt")
OUT = os.path.join(BASE, "connections", "followers_and_following", "unfollow_batches.md")

batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 120


def main():
    with open(SRC, encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    total = len(names)
    lines = [f"# Unfollow checklist ({total} accounts)\n"]
    lines.append(f"Work through one batch per day (~{batch_size}/day) to stay under Instagram's limits.\n")

    for i in range(0, total, batch_size):
        day = i // batch_size + 1
        chunk = names[i:i + batch_size]
        lines.append(f"\n## Day {day}  ({len(chunk)} accounts)\n")
        for name in chunk:
            lines.append(f"- [ ] [{name}](https://www.instagram.com/{name})")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {total} accounts across {(total + batch_size - 1)//batch_size} daily batches to:")
    print(OUT)


if __name__ == "__main__":
    main()
