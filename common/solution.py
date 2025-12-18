"""Base solution class for Advent of Code problems."""

from __future__ import annotations
from pathlib import Path
import inspect
import json


def get_day_metadata(year_dir: Path, day: str) -> dict | None:
    """Load metadata for a specific day from metadata.json."""
    metadata_path = year_dir / "metadata.json"
    if metadata_path.exists():
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
                return metadata.get(day)
        except (json.JSONDecodeError, KeyError):
            pass
    return None


class Solution:
    def __init__(self, input_file: str | None = None, test: bool = False):
        # Get the directory of the calling script
        caller_file = inspect.stack()[1].filename
        caller_dir = Path(caller_file).parent

        if input_file is None:
            if test:
                input_file = caller_dir / "test.input.txt"
            else:
                input_file = caller_dir / "input.txt"
        else:
            # If relative path, resolve from caller's directory
            input_file = Path(input_file)
            if not input_file.is_absolute():
                input_file = caller_dir / input_file

        self.input_path = Path(input_file)

        # Extract year and day from path (years/{year}/{day}/...)
        self.day = caller_dir.name
        self.year = caller_dir.parent.name

        # Load metadata (name, emoji)
        self._metadata = get_day_metadata(caller_dir.parent, self.day)

        if self.input_path.exists():
            self.raw_input = self.input_path.read_text().strip()
            self.data = self.parse_input(self.raw_input)
        else:
            self.raw_input = ""
            self.data = []

    @property
    def title(self) -> str:
        """Get the puzzle title from metadata."""
        if self._metadata:
            return self._metadata.get("name", "")
        return ""

    @property
    def emoji(self) -> str:
        """Get the puzzle emoji from metadata."""
        if self._metadata:
            return self._metadata.get("emoji", "")
        return ""

    def parse_input(self, raw: str):
        return raw.splitlines()

    def part1(self) -> int | str | None:
        return None

    def part2(self) -> int | str | None:
        return None

    def run(self) -> int | str | None:
        return None

    def solve(self):
        # Build header
        title = self.title if self.title else "Advent of Code"
        emoji = f" {self.emoji}" if self.emoji else ""

        try:
            print()
            print(f"🎄 Year {self.year} · Day {self.day}{emoji}")
            print(f"   {title}")
            print("─" * 40)
            arrow = "→"
        except UnicodeEncodeError:
            # Fallback for Windows terminals with limited encoding
            print()
            print(f"Year {self.year} - Day {self.day}")
            print(f"   {title}")
            print("-" * 40)
            arrow = "->"

        # Check if run() was overridden
        if type(self).run is not Solution.run:
            result = self.run()
            print(f"   {arrow} {result}")
            print()
            return

        # Otherwise use part1/part2
        p1 = self.part1()
        if p1 is not None:
            print(f"   Part 1 {arrow} {p1}")

        p2 = self.part2()
        if p2 is not None:
            print(f"   Part 2 {arrow} {p2}")

        print()
