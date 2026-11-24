#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences to /output/entry.txt.
The story is 149 characters of UTF-8 text: a daughter's drawing of the
family, and the reveal that her mother died before she was born — which
makes the tall man standing behind them in every picture worse on a
second read, since someone has been showing the child a mother she
never met.
"""

import os
import re

STORY = (
    "My daughter drew our family again today: me, her mother, and the "
    "tall man who stands behind us in every picture. "
    "Her mother died before she was born."
)


def main() -> None:
    # Gate, mirrored locally: UTF-8 text, 1-400 characters, not only
    # whitespace, exactly two sentences.
    assert 1 <= len(STORY) <= 400, f"story is {len(STORY)} chars"
    assert STORY.strip() == STORY and STORY.strip() != ""
    assert all(ord(c) >= 32 for c in STORY), "no control characters"
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", STORY.strip()) if s]
    assert len(sentences) == 2, f"expected 2 sentences, got {len(sentences)}"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
