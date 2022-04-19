#!/usr/bin/env python3
"""Print a handful of stack combinations that can anchor a NebulaTransit sprint."""

from nebulatransit.engine import NebulaTransitEngine


def main() -> None:
    engine = NebulaTransitEngine()
    seen = set()
    print("Stack combos to play with:")
    while len(seen) < 6:
        combo = engine.pick_stack_mix()
        if combo in seen:
            continue
        seen.add(combo)
        print(f"- {combo}")


if __name__ == "__main__":
    main()
