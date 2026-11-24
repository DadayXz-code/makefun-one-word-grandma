"""One Word From Grandma.

Writes exactly one word to /output/entry.txt: the single word Grandma
would text about AI.

Grandma does not text about "AI". She texts about Al. She has never met
Al, but she is sure he is a very nice young man who lives inside the
computer, and she hopes he eats enough. So the word is "Al": warm, a
little baffled, and the joke lands in two letters.

Deterministic: no randomness, no time, no network, no input. The same
word is written on every run.
"""

import os

WORD = "Al"

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    # The gate only accepts 1 to 30 characters, a single word, not only
    # whitespace. Check our own word against it before writing.
    assert 1 <= len(WORD) <= 30
    assert WORD.split() == [WORD]
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(WORD + "\n")


if __name__ == "__main__":
    main()
