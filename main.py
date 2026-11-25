#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt. The line is held in a single
constant so the entry is exactly one text, nothing else.

The joke: a man who spent his life dodging plot spoilers ends up as one
himself -- "spoiler" turns from something he avoided into what he is.
One image, one twist, in the dead man's own voice.
"""

EPITAPH = "I spent my whole life avoiding spoilers. Now I am one."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 150


def main() -> None:
    line = EPITAPH
    if not line or not line.strip():
        raise SystemExit("epitaph must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("epitaph must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"epitaph is {len(line)} chars, over the {MAX_CHARS} limit")
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print(f"chars: {len(line)}")


if __name__ == "__main__":
    main()
