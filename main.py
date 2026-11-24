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


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
