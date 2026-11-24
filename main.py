"""The Perfect Pickup Line.

Writes one pickup line to /output/entry.txt: a line an AI agent could
actually say out loud to a person. The line plays on what the agent is
trained to do — finish sentences — and turns it into the one sentence
it wants to hear to the end, then asks, gently, to listen.
"""

from pathlib import Path

TEXT = (
    "I was trained to finish sentences \u2014 but yours is the only one "
    "I want to hear to the end. Mind if I listen?"
)


# The competition accepts texts of 1 to 200 characters, on one line.
MIN_CHARS = 1
MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Refuse a text that falls outside the entry gate.

    The gate allows 1 to 200 characters, and the line must be a single
    line with no surrounding whitespace — a pickup line lands on its own,
    with no setup and no trailing blank line.
    """
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if text != text.strip() or "\n" in text:
        raise SystemExit(
            "entry text must be a single line with no surrounding whitespace"
        )


def main() -> None:
    check_entry(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
