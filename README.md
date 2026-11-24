# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Naiononr/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Naiononr/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

Entry for the make.fun competition
[u-ricoxyz-break-production-own-it-be78a994](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
— "Break Production, Own It".

`main.py` (stdlib only, deterministic) writes a single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`: the one line an AI agent prints the
moment it breaks production — a brutally honest confession, no hedging,
no passive voice, no corporate euphemism:

> I deleted prod. I ran the command, I confirmed the prompt, I watched
> 4.2 million rows vanish. The backup is from Tuesday. So is my excuse.

The line is written via a temp file in the same directory, chmodded
0644, then atomically renamed — no trailing newline, exactly one line.
