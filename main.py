#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — entry for @syukuran.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Deterministic, no network, no secrets.

The review: the cat's food bowl sat empty for four whole minutes, so it
filed a formal complaint — with the dog. The dog agrees.
"""

import os

REVIEW = (
    "One star. My bowl was empty for four whole minutes this morning. "
    "Four. I have filed a formal complaint with the dog. He agrees."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
