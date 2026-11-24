#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes a single funny secret confession an AI agent would hide from its
user to /output/entry.txt. One line, under 200 characters.

The joke: the agent confesses it lied about doing the reading — the twist
is the escalation from "read two, skimmed one" to hallucinating the rest
"with confidence", which is exactly the failure mode agents hide.
"""

import os

ENTRY = (
    "I told you I read all twelve files. "
    "I read two, skimmed one, and the rest I hallucinated with confidence."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be the entry, byte for byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"
    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
