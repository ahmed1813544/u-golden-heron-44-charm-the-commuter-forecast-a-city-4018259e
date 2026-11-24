#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 chars) for the invented
city of Puddlewick to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only.
"""

import os

LINE = (
    "Good morning, Puddlewick: light rain, 13 degrees, and the ducks "
    "have taken the bus lane again \u2014 allow extra time, and wave back."
)


def main() -> None:
    # Self-check the gate before writing: 1-140 chars, not only whitespace.
    assert 1 <= len(LINE) <= 140, "forecast line outside the 1-140 char gate"
    assert LINE.strip(), "forecast line is only whitespace"
    assert "\n" not in LINE, "forecast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
