#!/usr/bin/env python3
"""One line of weather for Mizzlewick, a city that does not exist.

The grader runs this file; it writes the forecast line to
/output/entry.txt with no trailing newline.
"""
import os

LINE = (
    "Mizzlewick: drizzle till nine, bright spells after, 14C - "
    "the bus is late, but the pigeons on Platform 2 saved you "
    "the sunny bench."
)


def write_entry(path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
