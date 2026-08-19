#!/usr/bin/env python3
"""
Rebuild the unfollow list with already-completed batches removed.
Pass the batch numbers you've finished (based on batch_size=120).

Usage:
    python3 update_remaining.py 1 6      # removes Day 1 and Day 6
"""

import html
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FF = os.path.join(BASE, "connections", "followers_and_following")
SRC = os.path.join(FF, "not_following_back.txt")
REMAINING_TXT = os.path.join(FF, "not_following_back.txt")   # overwrite master list
MD_OUT = os.path.join(FF, "unfollow_batches.md")
HTML_OUT = os.path.join(BASE, "unfollow_list.html")

BATCH = 120


def main():
    done_days = {int(a) for a in sys.argv[1:]} or {1}

    with open(SRC, encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    # Figure out which indices belonged to the finished days.
    done_idx = set()
    for day in done_days:
        start = (day - 1) * BATCH
        done_idx.update(range(start, min(start + BATCH, len(names))))

    remaining = [n for i, n in enumerate(names) if i not in done_idx]
    removed = len(names) - len(remaining)

    # Save the trimmed master list.
    with open(REMAINING_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(remaining))

    # Rebuild markdown checklist.
    md = [f"# Unfollow checklist — {len(remaining)} remaining "
          f"(removed {removed} already done)\n"]
    for i in range(0, len(remaining), BATCH):
        day = i // BATCH + 1
        chunk = remaining[i:i + BATCH]
        md.append(f"\n## Day {day}  ({len(chunk)} accounts)\n")
        for n in chunk:
            md.append(f"- [ ] [{n}](https://www.instagram.com/{n})")
    with open(MD_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    # Rebuild clickable HTML.
    parts = [f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unfollow list ({len(remaining)} left)</title>
<style>
 body{{font-family:-apple-system,system-ui,sans-serif;max-width:760px;margin:24px auto;padding:0 16px;line-height:1.6;color:#222}}
 h1{{font-size:1.3rem}} h2{{margin-top:28px;border-bottom:1px solid #ddd;padding-bottom:4px}}
 .row{{display:flex;align-items:center;gap:10px;padding:3px 0}}
 .row a{{text-decoration:none;color:#0064c8}} .row a:visited{{color:#999}}
 input[type=checkbox]{{width:16px;height:16px}}
 .note{{background:#fff7e6;border:1px solid #ffe0a3;padding:10px 14px;border-radius:8px;font-size:.9rem}}
</style></head><body>
<h1>Remaining accounts to unfollow ({len(remaining)})</h1>
<p class="note">Click a name to open the profile, then tap <b>Following &rarr; Unfollow</b>.
Keep to ~{BATCH}/day.</p>"""]
    for i in range(0, len(remaining), BATCH):
        day = i // BATCH + 1
        chunk = remaining[i:i + BATCH]
        parts.append(f"<h2>Day {day} ({len(chunk)} accounts)</h2>")
        for n in chunk:
            s = html.escape(n)
            parts.append(f'<div class="row"><input type="checkbox">'
                         f'<a href="https://www.instagram.com/{s}" target="_blank" rel="noopener">{s}</a></div>')
    parts.append("</body></html>")
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))

    print(f"Removed {removed} completed accounts. {len(remaining)} remaining.")
    print(f"Updated:\n  {MD_OUT}\n  {HTML_OUT}\n  {REMAINING_TXT}")


if __name__ == "__main__":
    main()
