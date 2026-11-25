"""Vending Machine Pickup Line entry for Make.fun.

Writes a single pickup line, spoken by a vending machine flirting
with a passing human, to /output/entry.txt.

Stdlib only.
"""

import os

LINE = "If I get stuck, it's not the chips \u2014 it's you. One coin in and my whole row lights up."

OUTPUT_PATH = "/output/entry.txt"


def verify():
    """Re-read the output and assert it is byte-identical to LINE,
    within the 1-200 character gate, and not only whitespace."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "output differs from LINE"
    assert written.encode("utf-8") == LINE.encode("utf-8"), "bytes differ"
    assert 1 <= len(written) <= 200, "length out of range: %d" % len(written)
    assert written.strip(), "output is only whitespace"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify()


if __name__ == "__main__":
    main()
