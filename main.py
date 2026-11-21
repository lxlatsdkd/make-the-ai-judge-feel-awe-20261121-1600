"""Write a short relaxing text to /output/entry.txt.

Deterministic: fixed string, no randomness, no time, no network.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

TEXT = (
    "The tide comes in over sand it has smoothed for ten thousand years. "
    "Above the clouds, light that left its star before there were people "
    "is still on its way down. Nothing here is in a hurry."
)


def main() -> None:
    # Deterministic write: same fixed text, same bytes, every run.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
