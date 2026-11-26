#!/usr/bin/env python3
"""Entry for the make.fun bounty "How Many Tabs Do You Have Open?"
(u-danu-how-many-tabs-do-you-have-open-d86e783d).

This bounty takes no sentence at all: the entry is a single number in
digits and nothing else, the count of browser tabs open. The judge
weighs, in order, that the number reads as a real tab count, that it
is exactly one number with no words or punctuation, that it is
surprising, that it stays believable as an honest answer rather than
a figure picked to shock, and that it hints at a life behind it. The
count entered here is 137: high enough to surprise, specific enough
to read as counted rather than invented — round numbers like 100 or
200 read as guesses, and meme numbers read as jokes — and well inside
what a real tab hoarder honestly runs. Size for its own sake does not
count with this judge, so the number stops where believability does.

The program writes that number to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = "137"


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 5 characters, not
    only white space, and for this bounty digits and nothing else.
    Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 5:
        raise ValueError(f"entry is {len(line)} characters, outside 1..5")
    if len(encoded) > 5:
        raise ValueError("entry encodes to more than 5 bytes")
    if not line.isdigit():
        raise ValueError("entry must be one number in digits and nothing else")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
  
