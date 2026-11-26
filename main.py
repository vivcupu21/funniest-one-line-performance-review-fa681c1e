#!/usr/bin/env python3
"""Funniest One-Line Performance Review entry program.

Writes the single-line performance review to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only. No network, no randomness, no clock: the output is
byte-identical on every run.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    src = HERE / "entry.txt"
    dst = Path(out_dir) / "entry.txt"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
