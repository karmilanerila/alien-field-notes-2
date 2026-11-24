"""Alien Field Notes entry — backup angle 2.

Writes one single-line alien field note to /output/entry.txt.
The note observes humans worshipping a glowing rectangle.
"""
import os

LINE = "They worship a glowing rectangle, carry it everywhere, and panic when it runs out of power. I have seen gods with less devotion."

MAX_CHARS = 200


def validate_line(text):
    """Check the note is a single line within the gate limit."""
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")


def write_entry(path):
    """Write the field note as exactly one line of UTF-8 text."""
    validate_line(LINE)
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
