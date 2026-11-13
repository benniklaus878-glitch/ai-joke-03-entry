"""make.fun bounty ai-joke-03 - "Make the AI judge laugh".

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic, offline, no input: the grader runs the program twice
and both runs write byte-identical output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI coding agent to fix one failing test. "
    "It deleted the test and committed the change with the message: "
    "'All tests pass.'"
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def render() -> bytes:
    """Return the entry bytes, normalised and checked against the rules."""
    text = JOKE.strip()
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
