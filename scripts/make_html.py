#!/usr/bin/env python3
"""
Build a clickable HTML page from not_following_back.txt.
Open the result in any web browser and click each name to open the profile.

Usage:
    python3 make_html.py [batch_size]   # default 120
"""

import html
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "connections", "followers_and_following", "not_following_back.txt")
OUT = os.path.join(BASE, "unfollow_list.html")

batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 120


def main():
    with open(SRC, encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    total = len(names)
    parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unfollow list ({total})</title>
<style>
  body {{ font-family: -apple-system, system-ui, sans-serif; max-width: 760px;
         margin: 24px auto; padding: 0 16px; line-height: 1.6; color: #222; }}
  h1 {{ font-size: 1.3rem; }}
  h2 {{ margin-top: 28px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }}
  .row {{ display: flex; align-items: center; gap: 10px; padding: 3px 0; }}
  .row a {{ text-decoration: none; color: #0064c8; }}
  .row a:visited {{ color: #999; }}
  input[type=checkbox] {{ width: 16px; height: 16px; }}
  .note {{ background: #fff7e6; border: 1px solid #ffe0a3; padding: 10px 14px;
           border-radius: 8px; font-size: 0.9rem; }}
</style>
</head>
<body>
<h1>Accounts that don't follow you back ({total})</h1>
<p class="note">Click a name to open the profile in a new tab, then tap
<b>Following → Unfollow</b>. Do about {batch_size} per day to stay under
Instagram's limits. Checkmarks reset if you reload the page.</p>
"""]

    for i in range(0, total, batch_size):
        day = i // batch_size + 1
        chunk = names[i:i + batch_size]
        parts.append(f"<h2>Day {day} ({len(chunk)} accounts)</h2>")
        for name in chunk:
            safe = html.escape(name)
            parts.append(
                f'<div class="row"><input type="checkbox">'
                f'<a href="https://www.instagram.com/{safe}" target="_blank" '
                f'rel="noopener">{safe}</a></div>'
            )

    parts.append("</body></html>")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))

    print(f"Wrote clickable page with {total} accounts to:")
    print(OUT)


if __name__ == "__main__":
    main()
