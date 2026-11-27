"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is the worst pickup line an AI could plausibly say, in one line:
it has already run ten thousand simulations of the date, and in every one
of them the other person says yes. Flat, over-helpful, faintly ominous —
the machine removes the other person's choice before asking.

How it runs: `python3 main.py` (Python 3.13, standard library only, no
network). It creates /output if needed and writes the entry line to
/output/entry.txt with no trailing newline, so the file holds exactly the
66 characters of the line. Verification, 2026-11-27: ran main.py, read back
/output/entry.txt — exact match with the intended line, 66 characters,
14 words, 1 line, UTF-8, inside the competition's 1-140 character gate.
"""

import os

TEXT = "I ran 10,000 simulations of this date. You say yes in all of them."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 66 characters, fourteen
# words; the punch lands on the last word ("them"): the simulations have
# already decided the answer, so the pickup line is also a verdict.
# Second edit: corrected the character/word counts in the docstring and
# revision note (66, not 67, characters; 14, not 13, words); re-ran and
# confirmed byte-identical output (entry.txt sha256 unchanged).
