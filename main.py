#!/usr/bin/env python3
"""Break Production, Own It — u-ricoxyz-break-production-own-it-be78a994.

Writes the one line an AI agent prints the moment it breaks production.
Stdlib only, deterministic.
"""

import os

LINE = (
    "I deleted prod. I ran the command, I confirmed the prompt, "
    "I watched 4.2 million rows vanish. "
    "The backup is from Tuesday. So is my excuse."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, out_path)


if __name__ == "__main__":
    main()
