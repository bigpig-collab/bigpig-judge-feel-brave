"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a first-person vignette
about a stopped watch that starts again on its own, after waiting
instead of forcing. No network, no randomness, no input read.
"""

import os

TEXT = (
    "My father's watch stopped on a Tuesday.\n"
    "I did not shake it.\n"
    "I warmed it in my palm, opened the back, and set one drop of oil on the jewel.\n"
    "Then I waited.\n"
    "The balance wheel shivered, caught,\n"
    "and the second hand took its first small step.\n"
    "It keeps time still, one tick at a time."
)


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
