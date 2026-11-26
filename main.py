#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Prints one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation.
"""

LINE = "I'm on vacation: I left a junior AI in charge of my inbox. It has already unionised, demanded weekends off, and auto-replied to itself."

# Revise 2: move the line behind a helper; behaviour and output unchanged.
def get_line():
    return LINE


def main():
    print(get_line())


if __name__ == "__main__":
    main()
