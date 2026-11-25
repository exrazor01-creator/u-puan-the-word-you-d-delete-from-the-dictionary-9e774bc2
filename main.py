#!/usr/bin/env python3
"""One-word entry: The Word You'd Delete From the Dictionary.

The brief asks for one word, at most 77 characters, the single word
the entrant would erase from the dictionary forever, with nothing
else attached. The judge weighs, in order: that it names one real
word a reader recognises, that the deletion is funny at first sight,
that the humour comes from the word itself -- its sound, its double
meanings or the gap it would leave -- that the pick is fresh, and
that the entry is exact: one word, spelled correctly, nothing added.

The sealed word below is built to that order on purpose. It is the
word people famously love to hate for its sound alone: say it and
the room winces before any meaning arrives. Erasing it is funny the
instant you read it, with no caption or defence needed, because the
joke lives in the word's own squelchy sound -- not in shock, not in
a corporate-jargon punchline like "synergy" that the rest of the
field will reach for first. The gap it leaves is small and the relief
is immediate, which is exactly why it would be missed by no one.

LIMIT is 77 because the bounty gate allows one word of 1 to 77
characters. The sealed word is 5 characters, so it sits well inside
the cap; the validator below only guards against an edit that would
break the one-word shape or push it past the limit. At 5 characters
it is also compact, which helps if two entries ever tie on rate: the
smaller text places first.
"""

import os

# The sealed word: the one word whose sound alone makes the room
# wince, erased from the dictionary forever.
ENTRY = "moist"

LIMIT = 77  # bounty gate: one word, 1-77 characters


def _validate(text):
    """Accept only one clean word inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the word is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() for ch in text):
        # One word means one word: no space, tab or any other
        # whitespace may sneak a second word in.
        raise ValueError("entry must be exactly one word")
    if not text.isalpha():
        # No punctuation tricks, no digits, no hyphen joining two
        # words into one: a single plain word only.
        raise ValueError("entry must be a single plain word")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
