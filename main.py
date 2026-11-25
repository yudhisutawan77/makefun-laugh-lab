#!/usr/bin/env python3
"""One-Liner Laugh Lab — a robot vacuum's excuse for eating a sock.

The joke is a deadpan courtroom defence: the vacuum pleads that the
sock was lying on the floor with no label and, to a machine built to
hoover up whatever it finds, shaped exactly like a snack. The humour
comes from treating a household accident as a legal case, with the
vacuum as a defendant who genuinely believes the sock was asking for it.

Writes the single line to /output/entry.txt and prints it to stdout.
Standard library only, deterministic, no network, no randomness.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")

LINE = "In my defence, the sock was on the floor, unlabelled, and shaped exactly like a snack."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    size = len(LINE)
    if size < MIN_CHARS or size > MAX_CHARS:
        print(f"entry is {size} characters, gate needs "
              f"{MIN_CHARS}..{MAX_CHARS}", flush=True)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", flush=True)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", flush=True)
        return 1
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(LINE, encoding="utf-8")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
