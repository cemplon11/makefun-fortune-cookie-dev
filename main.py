#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (no trailing newline).

Pure Python standard library only; deterministic; no network.
"""

import os

LINE = "Your legacy code is not a mess; it is a letter from a developer who loved this product before you did."


def main() -> None:
    # Self-check the gate before writing: 1-120 characters, not only
    # white space, exactly one line.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
