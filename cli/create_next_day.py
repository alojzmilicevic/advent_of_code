import sys
from pathlib import Path
from datetime import datetime
from cli.constants import SOLUTION_FILENAME, INPUT_FILENAME, TEST_INPUT_FILENAME


# Template for new solution files
SOLUTION_TEMPLATE = """from common.solution import Solution


class Day(Solution):
    def part1(self):
        # self.data is list of lines, self.raw_input is the raw string
        return None
    
    def part2(self):
        return None


Day().solve()
"""


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_session_cookie():
    """Get session cookie from downloader module."""
    try:
        from .aoc_downloader import get_session_cookie as _get_session

        return _get_session()
    except ImportError:
        return None


def download_input(year, day, output_path):
    """Download input file."""
    try:
        from .aoc_downloader import download_input as _download

        return _download(year, day, output_path)
    except ImportError:
        return False


def add_metadata(year, day, session, interactive=True):
    """Add metadata for a day."""
    try:
        from .metadata import auto_add_metadata

        return auto_add_metadata(year, day, session=session, interactive=interactive)
    except ImportError:
        return None, None


def find_latest_year():
    """Find the latest year folder."""
    root = get_project_root()
    years_dir = root / "years"

    if not years_dir.exists():
        return datetime.now().year

    year_folders = [d for d in years_dir.iterdir() if d.is_dir() and d.name.isdigit()]

    if not year_folders:
        return datetime.now().year

    years = [int(d.name) for d in year_folders]
    return max(years)


def find_next_day(year):
    """Find the next day that doesn't exist for the given year."""
    root = get_project_root()
    year_path = root / "years" / str(year)

    if not year_path.exists():
        return 1

    day_folders = [d for d in year_path.iterdir() if d.is_dir() and d.name.isdigit()]

    if not day_folders:
        return 1

    days = [int(d.name) for d in day_folders]
    return max(days) + 1


def ensure_year_folder(year_path):
    """Ensure year folder exists with __init__.py."""
    created = False

    if not year_path.exists():
        year_path.mkdir(parents=True)
        print(f"Created year folder: {year_path.name}")
        created = True

    init_path = year_path / "__init__.py"
    if not init_path.exists():
        init_path.touch()
        print(f"  Created __init__.py")

    return created


def create_day_folder(year, day, auto_download=True):
    """Create the folder and files for a new day."""
    root = get_project_root()
    year_path = root / "years" / str(year)
    day_path = year_path / str(day)

    # Ensure year folder exists
    ensure_year_folder(year_path)

    # Check if day already exists
    if day_path.exists():
        print(f"Day {day} already exists!")
        return False

    # Create day folder
    day_path.mkdir(parents=True)
    print(f"Created day folder: {day}")

    # Create solution file
    solution_file = day_path / SOLUTION_FILENAME
    solution_file.write_text(SOLUTION_TEMPLATE)
    print(f"  Created {SOLUTION_FILENAME}")

    # Download or create input file
    input_file = day_path / INPUT_FILENAME
    downloaded = False
    session = get_session_cookie()

    if auto_download and session:
        print(f"  Attempting to download {INPUT_FILENAME}...")
        if download_input(year, day, input_file):
            print(f"  ✓ Downloaded {INPUT_FILENAME} from adventofcode.com")
            downloaded = True
        else:
            print(f"  ✗ Could not download input (creating empty file)")

    if not downloaded:
        input_file.touch()
        print(f"  Created empty {INPUT_FILENAME}")

    # Create test input file
    (day_path / TEST_INPUT_FILENAME).touch()
    print(f"  Created {TEST_INPUT_FILENAME}")

    # Fetch and add metadata
    add_metadata(year, day, session=session, interactive=True)

    return True


def main():
    """Main function to create the next day."""
    year = find_latest_year()
    day = find_next_day(year)

    print(f"\nCreating day {day} for year {year}...")
    print("-" * 40)

    if create_day_folder(year, day):
        print("-" * 40)
        print(f"Successfully created years/{year}/{day}/")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
