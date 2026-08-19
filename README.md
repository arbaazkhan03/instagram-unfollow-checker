# Instagram Unfollow Checker

Find the Instagram accounts you follow that **don't follow you back** — using your
own downloaded Instagram data. No login, no password, no sketchy third-party apps.

**Live web app:** https://arbaazkhan03.github.io/instagram-unfollow-checker/

Everything runs **in your browser**. Your Instagram data never leaves your device
and is never uploaded to any server.

---

## Features

- 🔒 **100% private** — all processing happens in your browser; nothing is uploaded, no login, no password.
- 📱 **Works on your phone** — installable to your home screen and works offline (PWA).
- 📋 **Clickable list** with direct profile links, split into safe **~120/day batches**.
- ✅ **Saved progress** — check off accounts as you unfollow; your progress is remembered.
- 📌 **Keep-list** — mark accounts you follow on purpose (celebs, brands) so they're removed from the list and don't count.
- 🔎 **Search & sort** — filter by username, or sort A→Z, Z→A, most-recently-followed, or oldest first.
- 🚀 **One-tap open** — jumps straight into the Instagram app on mobile, ready to unfollow.
- 🤖 **Follow activity check** — flags whether your follows show automated/bot bursts.
- ⬇️ **Export** your list as HTML (clickable), CSV, or TXT.
- 🌗 **Light & dark mode.**

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

## Contact

Made by **Arbaaz**. Questions, feedback, or ideas? Reach out:

- Email: `iam.arbaazkhan03 [at] gmail [dot] com`
- Instagram: [@just_an_engineer.mlk](https://www.instagram.com/just_an_engineer.mlk)
- LinkedIn: [arbaaz-khan03](https://www.linkedin.com/in/arbaaz-khan03/)

## License

Released under the [MIT License](LICENSE) — free to use, modify, and share, just
keep the copyright notice. © 2026 Arbaaz Khan.

## ⚠️ Use at your own risk

This is a personal, unofficial tool with no warranty of any kind. It is not
affiliated with, endorsed by, or connected to Instagram or Meta. You are
responsible for how you use it — including respecting Instagram's Terms of
Service and unfollowing at a sensible pace (~100–120/day). The author is not
liable for any account limits, blocks, or other issues that may result.

---

## Links & resources

**This project**
- 🌐 [Live web app](https://arbaazkhan03.github.io/instagram-unfollow-checker/)
- 💻 [Source code (GitHub)](https://github.com/arbaazkhan03/instagram-unfollow-checker)
- 🐞 [Report an issue / suggest a feature](https://github.com/arbaazkhan03/instagram-unfollow-checker/issues)
- 📄 [License (MIT)](LICENSE)

**Official Instagram help**
- [Download your information](https://www.instagram.com/download/request/)
- [About downloading your data](https://help.instagram.com/181231772500920)
- [Terms of Use](https://help.instagram.com/581066165581870)
- [Community Guidelines](https://help.instagram.com/477434105621119)

**Reach out**
- Instagram: [@just_an_engineer.mlk](https://www.instagram.com/just_an_engineer.mlk)
- LinkedIn: [arbaaz-khan03](https://www.linkedin.com/in/arbaaz-khan03/)

<sub>Made with care by Arbaaz. Not affiliated with Instagram or Meta.</sub>
