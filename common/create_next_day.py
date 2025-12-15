import os
import sys
from pathlib import Path
from datetime import datetime


# Import will be done later to avoid circular imports
def get_downloader():
    """Lazy import of downloader to avoid circular dependencies."""
    try:
        from .aoc_downloader import download_input, get_session_cookie
        return download_input, get_session_cookie
    except ImportError:
        return None, None

def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent

def find_latest_year():
    """Find the latest year folder."""
    root = get_project_root()
    year_folders = [d for d in root.iterdir() if d.is_dir() and d.name.startswith('year')]
    if not year_folders:
        # Default to current year if no year folders exist
        return datetime.now().year
    
    years = [int(d.name.replace('year', '')) for d in year_folders]
    return max(years)

def find_next_day(year):
    """Find the next day that doesn't exist for the given year."""
    root = get_project_root()
    year_path = root / f'year{year}'
    
    if not year_path.exists():
        return 1
    
    # Get all day folders (folders with numeric names)
    day_folders = [d for d in year_path.iterdir() if d.is_dir() and d.name.isdigit()]
    
    if not day_folders:
        return 1
    
    days = [int(d.name) for d in day_folders]
    return max(days) + 1

def create_day_folder(year, day, auto_download=True):
    """Create the folder and files for the next day."""
    root = get_project_root()
    year_path = root / f'year{year}'
    day_path = year_path / str(day)
    
    # Create year folder if it doesn't exist
    if not year_path.exists():
        year_path.mkdir(parents=True)
        print(f"Created year folder: year{year}")
    
    # Create metadata.py if it doesn't exist
    metadata_path = year_path / 'metadata.py'
    if not metadata_path.exists():
        metadata_template = '''from common.day import Day


def get_metadata():
    days = {
    }

    return days
'''
        metadata_path.write_text(metadata_template)
        print(f"  Created metadata.py for year{year}")
    
    # Create day folder
    if day_path.exists():
        print(f"Day {day} already exists!")
        return False
    
    day_path.mkdir(parents=True)
    print(f"Created day folder: {day}")
    
    # Create part1.py with template
    part1_py = day_path / 'part1.py'
    part1_py.write_text('from linereader import read_file\n\ndata = [x for x in read_file(\'input.txt\')]\n\n')
    print(f"  Created part1.py")

    # Create part2.py with template
    part2_py = day_path / 'part2.py'
    part2_py.write_text('from linereader import read_file\n\ndata = [x for x in read_file(\'input.txt\')]\n\n')
    print(f"  Created part2.py")    # Try to download input file if session is configured
    input_file = day_path / 'input.txt'
    downloaded = False
    
    if auto_download:
        download_input, get_session_cookie = get_downloader()
        if download_input and get_session_cookie and get_session_cookie():
            print(f"  Attempting to download input.txt...")
            if download_input(year, day, input_file):
                print(f"  ✓ Downloaded input.txt from adventofcode.com")
                downloaded = True
            else:
                print(f"  ✗ Could not download input (creating empty file)")
    
    # Create empty input file if download failed or was skipped
    if not downloaded:
        input_file.touch()
        print(f"  Created empty input.txt")
    
    # Create empty test input file
    (day_path / 'test.input.txt').touch()
    print(f"  Created test.input.txt")
    
    return True

def main():
    """Main function to create the next day."""
    year = find_latest_year()
    day = find_next_day(year)
    
    print(f"\nCreating day {day} for year {year}...")
    print("-" * 40)
    
    if create_day_folder(year, day):
        print("-" * 40)
        print(f"Successfully created year{year}/{day}/")
        print(f"\nFiles created:")
        print(f"  - year{year}/{day}/part1.py")
        print(f"  - year{year}/{day}/part2.py")
        print(f"  - year{year}/{day}/input.txt")
        print(f"  - year{year}/{day}/test.input.txt")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()

