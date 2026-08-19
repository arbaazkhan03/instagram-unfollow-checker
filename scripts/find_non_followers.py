#!/usr/bin/env python3
"""
Find Instagram accounts you follow that don't follow you back,
using your downloaded Instagram data (JSON export).

Usage:
    python3 find_non_followers.py
"""

import json
import os

BASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "connections",
    "followers_and_following",
)

FOLLOWING_FILE = os.path.join(BASE, "following.json")
FOLLOWERS_FILE = os.path.join(BASE, "followers_1.json")


def usernames_from_entries(entries):
    """Extract usernames from a list of Instagram relationship entries."""
    names = set()
    for entry in entries:
        for item in entry.get("string_list_data", []):
            value = item.get("value") or entry.get("title")
            if value:
                names.add(value)
    return names


def load_following(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    # following.json wraps the list in "relationships_following"
    entries = data.get("relationships_following", data)
    return usernames_from_entries(entries)


def load_followers(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    # followers_1.json is a plain list
    entries = data if isinstance(data, list) else data.get("relationships_followers", [])
    return usernames_from_entries(entries)


def main():
    following = load_following(FOLLOWING_FILE)
    followers = load_followers(FOLLOWERS_FILE)

    not_following_back = sorted(following - followers)

    print(f"You follow:        {len(following)}")
    print(f"Followers:         {len(followers)}")
    print(f"Don't follow back: {len(not_following_back)}\n")

    for name in not_following_back:
        print(f"  {name}  ->  https://www.instagram.com/{name}")

    out_path = os.path.join(os.path.dirname(FOLLOWING_FILE), "not_following_back.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(not_following_back))
    print(f"\nSaved list to: {out_path}")


if __name__ == "__main__":
    main()
