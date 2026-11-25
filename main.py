#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: one original dad joke, one line.

Writes the joke to /output/entry.txt (the path the make.fun harness
reads) and prints it. Deterministic, no network, no input.
"""

import os

JOKE = "I asked the calendar for a date, but it said it was already booked."

OUTPUT_PATH = os.environ.get("GROAN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # The gate accepts 1 to 140 characters; refuse to emit anything else.
    assert 1 <= len(JOKE) <= 140, "joke must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
