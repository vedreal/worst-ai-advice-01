#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give
(140 characters or fewer) to /output/entry.txt.

The line was chosen from ten candidates for the judge's brief:
worst advice first, funny on first read, tight, written in a
confident AI-assistant voice, and concrete enough to follow.
"""

import os
import sys

# The chosen line (98 characters). Runners-up are listed in README.md.
ADVICE = (
    "Certainly! To dry a wet phone faster, plug it in to charge "
    "\u2014 the electricity evaporates the water."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def write_entry(path=OUTPUT_PATH):
    """Write the advice line to the output file, creating dirs as needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ADVICE)
    return path


# The entry point (main) is defined below.


def main():
    """Validate the line against the gate, then write it out."""
    text = ADVICE
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"error: advice is {len(text)} characters, "
            f"outside the 1-{MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: advice is only whitespace", file=sys.stderr)
        return 1
    path = write_entry()
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
