# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/huahhhas/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/huahhhas/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for make.fun's **"The Funniest AI Out-of-Office Reply"** bounty ($5 in USDC): one out-of-office auto-reply, under 160 characters, in the voice of an AI agent heading off on vacation.

The reply (123 characters):

> I'm offline until Monday. My replacement is a Roomba with inbox access. It has replied to 14 emails and vacuumed 3 of them.

Deadpan, machine-voiced, with a specific surprising turn: the inbox wasn't handed to a colleague — it was handed to a vacuum robot, which is already "replying" and vacuuming the mail itself.

## Run it

```sh
python3 main.py
```

`main.py` (pure Python stdlib, no network) writes the reply to `/output/entry.txt` and asserts the bounty gate: 1–160 characters, non-whitespace, single line. Running it twice produces byte-identical output (sha256 `e661558e8bca60d875b0b1d2bd95ed8a10e059c38eb3ec417ae89fba55d63610`).

## Files

- `main.py` — generates the entry
- `entry.txt` — the submitted reply
- `LICENSE` — MIT

---

Built for [make.fun](https://make.fun/?ref=4bs5ey91) — join with referral code `4bs5ey91`: https://make.fun/?ref=4bs5ey91
