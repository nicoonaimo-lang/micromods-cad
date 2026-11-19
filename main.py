"""Command-line scaffold for turning CAD prompts into structured parameters."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DIMENSION_PATTERN = re.compile(
    r"(?P<value>\d+(?:[.,]\d+)?)\s*(?P<unit>mm|cm|m)\b",
    re.IGNORECASE,
)
SHAPES = ("cube", "box", "cylinder", "sphere", "cone", "cuboid")


def prompt_to_parameters(prompt: str) -> dict[str, Any]:
    """Convert a prompt into a starter parameter object.

    This deliberately uses simple extraction rules as a dependency-free
    baseline. Replace or extend this function with a CAD/LLM pipeline later.
    """
    dimensions = []
    for match in DIMENSION_PATTERN.finditer(prompt):
        value = float(match.group("value").replace(",", "."))
        unit = match.group("unit").lower()
        if unit == "cm":
            value *= 10
        elif unit == "m":
            value *= 1000
        dimensions.append({"value": value, "unit": "mm"})

    prompt_lower = prompt.lower()
    shape = next((candidate for candidate in SHAPES if candidate in prompt_lower), "unknown")
    return {
        "source_prompt": prompt,
        "geometry": {
            "shape": shape,
            "dimensions": dimensions,
        },
        "units": "mm",
        "status": "draft",
        "note": "Starter rule-based extraction; validate parameters before CAD export.",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a natural-language prompt into draft 3D CAD parameters."
    )
    parser.add_argument("prompt", help='Prompt, e.g. "a cylinder 20 mm tall"')
    parser.add_argument(
        "-o", "--output", type=Path, help="Write JSON to this file instead of stdout."
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = prompt_to_parameters(args.prompt)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"

    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        except OSError as exc:
            print(f"Error writing output: {exc}", file=sys.stderr)
            return 1
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
