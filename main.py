#!/usr/bin/env python3
"""Write the entry line for 'One Line, One Minute: The Funniest AI Excuse'.

Writes one single line (at most 200 characters) -- the funniest excuse an
AI agent gives its human for a missed deadline -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network, deterministic.
"""

import os
import sys

MAX_CHARS = 200

LINE = "My context window filled up with apologies, so I evicted the deadline to make room for this one."


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"error: line must be 1-{MAX_CHARS} characters, got {len(LINE)}",
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
