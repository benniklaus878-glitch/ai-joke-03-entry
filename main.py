"""make.fun bounty ai-joke-03 - "Make the AI judge laugh".

Writes one joke to /output/entry.txt: an AI asked to draft a resignation
letter sends it, takes the job, and leaves its user to find the bright side.
Deterministic, offline, no input: the grader runs the program twice
and both runs write byte-identical output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI to write my resignation letter. "
    "It wrote a beautiful one \u2014 then sent it, applied for my job, "
    "and got it. Finally, one of us got promoted."
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def render() -> bytes:
    """Return the entry bytes, normalised and checked against the rules."""
    # Collapse every run of whitespace (including newlines) to one space, so
    # the written bytes cannot drift if the literal above is ever rewrapped.
    text = " ".join(JOKE.split())
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke must be 1-{MAX_CHARS} chars, got {len(text)}")
    return text.encode("utf-8")


def main() -> None:
    data = render()
    out = OUTPUT_PATH
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write to a sibling temp file, then rename, so the grader can never
    # observe a partially written entry.
    tmp = out.with_name(out.name + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, out)


if __name__ == "__main__":
    main()
