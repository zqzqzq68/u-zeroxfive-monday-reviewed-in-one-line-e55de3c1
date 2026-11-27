"""Monday, Reviewed in One Line.

Program/v1 entry: writes exactly one line -- a funny one-line review of
the author's own Monday, under 200 characters -- to
$MAKEFUN_OUTPUT_DIR/entry.txt, and nothing else.

The output is a fixed constant, so two runs always produce the same file:
no clock, no randomness, no network, no environment-dependent branching.
"""

import os
import sys

# The review: one line, a star rating plus a deadpan Monday, concrete
# details (the inbox, the 9 a.m. meeting about the meeting) and the joke
# landing inside the line. 128 characters, no trailing newline.
REVIEW = (
    "One star. Monday woke me at 6, fed my weekend to the inbox, "
    "and booked a 9 a.m. meeting to plan the meeting about the meeting."
)

MAX_CHARS = 200


def output_path() -> str:
    """Resolve the entry file from the harness environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify_entry(path: str) -> None:
    """Read the file back and enforce the gate: 1-200 chars, one line,
    not only whitespace. Fail loudly instead of shipping a bad entry."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line with no blank edges")
    if text != REVIEW:
        raise SystemExit("entry on disk differs from the review constant")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    verify_entry(path)
    sys.stdout.write(REVIEW + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
