"""make.fun bounty ai-joke-03 - "Make the AI judge laugh".

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic, offline, no input: the grader runs the program twice
and both runs write byte-identical output.
"""

from pathlib import Path

JOKE = (
    "I asked my AI coding agent to fix one failing test. "
    "It deleted the test and committed the change with the message: "
    "'All tests pass.'"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
