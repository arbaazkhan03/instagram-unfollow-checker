# Instagram Unfollow Checker

Find the Instagram accounts you follow that **don't follow you back** — using your
own downloaded Instagram data. No login, no password, no sketchy third-party apps.

**Live web app:** https://arbaazkhan03.github.io/instagram-unfollow-checker/

Everything runs **in your browser**. Your Instagram data never leaves your device
and is never uploaded to any server.

---

## Two ways to use it

### 1. Web app (easiest — works on phone)
Open the link above, add your Instagram data file (the `.zip`, or just
`following.json` + `followers_1.json`), and you'll get a clickable list of
everyone who doesn't follow you back, split into safe daily batches. Nothing to
install.

**Tip:** Log into Instagram in the same browser first. Each name is a direct link
to that person's profile, so once you're logged in, tapping a name takes you
straight there — just tap **Following → Unfollow**. If you're not logged in,
Instagram will send you to the login page first.

### 2. Python scripts (for the terminal-inclined)
The same logic as command-line scripts, in the [`scripts/`](scripts/) folder.
Requires Python 3.

Put the scripts at the top level of your unzipped Instagram data folder (the one
containing `connections/`), then run:

```bash
python3 scripts/find_non_followers.py   # build the list of non-followers
python3 scripts/analyze_follows.py      # (optional) detect bot/automation bursts
python3 scripts/make_html.py            # build a clickable unfollow page
python3 scripts/update_remaining.py 1 2 # remove day-batches you've finished
```

## How to get your Instagram data (JSON)

In the Instagram app: **Settings and activity → Accounts Center → Your
information and permissions → Download your information.** Choose **JSON**
format, **All time**, and make sure "Followers and following" is included.
Instagram emails a download link, usually within a few minutes to a day.

## Unfollow safely

- Do about **100–120 per day, no more.** Going faster gets you temporarily blocked.
- If you ever see **"Try again later,"** stop for **24–48 hours.**
- **Never** use any app or extension that asks for your Instagram password.
  This tool never needs it, and neither should anything else.

## Privacy

This is a static site. All parsing happens client-side in your browser. No
analytics, no server, no data collection. Not affiliated with Instagram or Meta.
