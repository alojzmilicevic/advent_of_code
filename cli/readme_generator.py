from glob import glob
from pathlib import Path
from cli.metadata import get_metadata
from cli.constants import SOLUTION_FILENAME, OLD_PART1_FILENAME, OLD_PART2_FILENAME

# Get project root (parent of cli/)
PROJECT_ROOT = Path(__file__).parent.parent


def write_table_row(first: str, second: str, third: str, f):
    f.write("|" + first + "|" + second + "|" + third + "|\n")


def create_url(idx, day_meta, y):
    url = "https://adventofcode.com/"
    # day_meta is a Day object with .name and .emoji attributes
    return "[{day}]({url}{year}/day/{index}) {emoji}".format(
        day=day_meta.name, year=y, index=str(idx), emoji=day_meta.emoji, url=url
    )


def get_files(day, y):
    # Look for solution.py first, fallback to old part1.py/part2.py structure
    day_path = PROJECT_ROOT / "years" / str(y) / str(day)
    solution_file = day_path / SOLUTION_FILENAME

    if solution_file.exists():
        # New structure: single solution.py with both parts
        return [f"{day}/{SOLUTION_FILENAME}"]
    else:
        # Old structure: separate part1.py and part2.py files
        pattern = day_path / "part[12].py"
        raw_files = glob(str(pattern))
        # Return relative paths from year folder for links
        a = [f"{day}/" + Path(x).name for x in raw_files]
        return sorted(a)


def main(target_year=None):
    """Generate README files for all years or a specific year."""
    years_dir = PROJECT_ROOT / "years"

    if target_year:
        years = [target_year]
    else:
        year_folders = [
            d for d in years_dir.iterdir() if d.is_dir() and d.name.isdigit()
        ]
        years = sorted([int(d.name) for d in year_folders])

    print(f"Generating README files for years: {years}")

    for year in years:
        # Skip years without metadata
        metadata = get_metadata(year)
        if metadata is None:
            print(f"  Skipping {year} (no metadata.json)")
            continue

        readme_path = years_dir / str(year) / "README.md"
        f = open(readme_path, "w", encoding="utf-8")

        # File header
        f.write(f"# 🎄 🎅 Advent of code {year} 🎅 🎄\n")
        f.write(f"My Advent of Code (Season {year}) solutions written in Python 😀\n\n")

        # Table Header
        write_table_row("#", "Problem ☃", "Solution ❄", f)
        write_table_row("---", "-------------", ":-------------:", f)

        year_path = years_dir / str(year)
        day_folders = [
            d for d in year_path.iterdir() if d.is_dir() and d.name.isdigit()
        ]
        directories = sorted([int(d.name) for d in day_folders])

        for day_idx in directories:
            day_str = str(day_idx)
            files = get_files(day_str, year)

            # Skip days without metadata entry (keys are integers)
            if day_idx not in metadata:
                print(f"    Skipping day {day_idx} (no metadata entry)")
                continue

            file_links = ""
            if len(files) == 1:
                file_links = "[Part 1 & 2]({file})".format(file=files[0])
            if len(files) == 2:
                for i, file in enumerate(files):
                    if i > 0:
                        file_links += " - "
                    file_links += "[Part {p}]({file})".format(file=files[i], p=i + 1)
            write_table_row(
                day_str, create_url(day_str, metadata[day_idx], year), file_links, f
            )

        f.close()
        print(f"  Generated years/{year}/README.md")

    print("\nREADME generation complete!")


if __name__ == "__main__":
    main()
