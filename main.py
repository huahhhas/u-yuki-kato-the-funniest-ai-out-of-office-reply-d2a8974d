#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun bounty entry.

Writes one out-of-office auto-reply (<160 chars) to /output/entry.txt.
Pure stdlib only. Deterministic: same bytes on every run.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm offline until Monday. My replacement is a Roomba with inbox "
    "access. It has replied to 14 emails and vacuumed 3 of them."
)


def main() -> None:
    # Gate: 1-160 chars, not only whitespace, single line.
    assert 1 <= len(REPLY) <= 160, f"reply length {len(REPLY)} outside 1-160"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert "\n" not in REPLY and "\r" not in REPLY, "reply must be a single line"
    assert REPLY == REPLY.strip(), "reply must not start/end with whitespace"
    assert "  " not in REPLY, "reply must not contain double spaces"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY)

    # Verify what was written.
    with open(out_path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == REPLY, "written entry does not match REPLY"
    assert 1 <= len(text) <= 160
    assert text.strip()
    print(f"entry: {len(text)} chars")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(text)


if __name__ == "__main__":
    main()
