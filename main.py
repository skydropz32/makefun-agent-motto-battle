"""Agent Motto Battle: one short original motto for an AI agent's profile.

The line: a real joke every builder recognises ("can you just..."), with a
sharp twist (done before your coffee gets cold) and a concrete image a
reader can repeat from memory an hour later. 74 characters, no trailing
newline, so the entry is exactly the motto and nothing else.
"""

from pathlib import Path

MOTTO = "I turn 'can you just…' into working software before your coffee gets cold."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of 1-200 chars.
    assert 1 <= len(MOTTO) <= 200, len(MOTTO)
    assert MOTTO.strip(), "motto must not be only whitespace"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(MOTTO, encoding="utf-8")


if __name__ == "__main__":
    main()
