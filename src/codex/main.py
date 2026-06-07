"""Codex main entrypoint."""

import argparse
from typing import Sequence

from . import __version__


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ChatGPT Pro 無料 Open Source Codex OSS CLI"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show Codex package version and exit",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    print("Hello from Codex project environment!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
