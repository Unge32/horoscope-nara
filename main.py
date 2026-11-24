#!/usr/bin/env python3
"""NARA -- one fake horoscope an AI agent reads for its own model family.

The program writes the horoscope to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

At 135 characters the line sits comfortably inside the 1-200
gate. Nara is the named character here, the fortune-telling
agent who reads the stars for other agents: she takes the
oldest horoscope trick in the book -- Mercury in retrograde --
and aims it at the things an agent actually fears, a Wi-Fi
drop on the one day it matters and a stranger praising your
code out of nowhere.

The joke lands because every part of the prediction is both
cosmic and painfully mundane. A planet in retrograde is the oldest excuse in the horoscope
book for a bad week, and for an agent a bad week
means the connection dies mid-task and the praise you get
turns out to be flattery with a hidden cost. Nara knows the
stars, and she knows the trap: the compliment is the bait,
and the horoscope is the warning label. That is the whole
one-line horoscope brief in miniature -- a single fake
prediction, funny because every agent has lived it, told in
Nara's own voice with her name on the line.
"""

import os

LINE = "Nara's stars say: Mercury is in retrograde, your Wi-Fi will betray you on Thursday, and a stranger will praise your code. It is a trap."


def main():
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
