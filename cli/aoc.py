#!/usr/bin/env python3
"""
Advent of Code CLI Tool
"""
import sys
import argparse
import subprocess
from pathlib import Path

# Add project root to path so we can import modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from cli.create_next_day import main as create_next_day
from cli.aoc_downloader import download_input, setup_session_cookie, get_session_cookie
from cli.create_next_day import find_latest_year, find_next_day, create_day_folder
from cli.readme_generator import main as generate_readme


def show_help():
    """Display help information."""
    help_text = """
Advent of Code CLI Tool
=======================

Usage: python aoc.py [OPTION] [ARGS]

Options:
  -n, --next        Create the next day's folder structure with template files
  -d, --download    Download input for a specific day (or today's day)
  -run              Run solution(s) for a specific year/day/part
  -s, --setup       Setup your Advent of Code session cookie
  -r, --readme      Generate README files for all years based on metadata
  -h, --help        Show this help message and exit

Examples:
  python aoc.py -n                    # Create next day (e.g., day 10)
  python aoc.py --next                # Same as above
  python aoc.py -d                    # Download input for today's/latest day
  python aoc.py -d 5                  # Download input for day 5 (latest year)
  python aoc.py -d 2024 5             # Download input for year 2024, day 5
  python aoc.py --download 5          # Same as -d 5
  python aoc.py -run 2025             # Run ALL days for year 2025
  python aoc.py -run 5                # Run day 5 (latest year, both parts)
  python aoc.py -run 5 2              # Run day 5 part2 (latest year)
  python aoc.py -run 2024 5           # Run year 2024, day 5 (both parts)
  python aoc.py -run 2024 5 2         # Run year 2024, day 5, part2
  python aoc.py -s                    # Setup session cookie
  python aoc.py --setup               # Same as above
  python aoc.py -r                    # Generate all README files
  python aoc.py -r 2025               # Generate README for year 2025 only
  python aoc.py --readme              # Same as above
  python aoc.py -h                    # Show this help

Description:
  -n, --next
      Automatically detects the latest year and creates the next day's folder
      with solution.py, input.txt, and test.input.txt files.

  -d, --download [year] [day]
      Download input from adventofcode.com for the specified day.
      If no arguments: downloads for the latest day in the latest year
      If one argument: downloads for that day in the latest year
      If two arguments: downloads for specified year and day
      Requires session cookie (see --setup)

  -s, --setup
      Interactive setup to save your Advent of Code session cookie.
      This is required for downloading inputs.

  -r, --readme [year]
      Generates README.md files for each year folder based on the metadata.py
      files, creating a table of problems and solutions.
      If year is provided, only generates README for that year.

  -run <year|day> [day] [part]
      Run solution(s) for a specific year/day/part.
      If one argument > 25: runs ALL days for that year (e.g., -run 2021)
      If one argument <= 25: runs that day in the latest year (e.g., -run 5)
      If two arguments (year, day): runs both parts for that year/day
      If two arguments (day, part): runs that part for latest year
      If three arguments: runs specified year, day, and part
      Part defaults to running both parts if not specified.

  -h, --help
      Displays this help message with all available commands.
"""
    print(help_text)


def handle_download(args):
    """Handle the download command."""
    # Find the index of -d or --download flag and get arguments after it
    try:
        if '-d' in args:
            flag_idx = args.index('-d')
        else:
            flag_idx = args.index('--download')
        extra_args = args[flag_idx + 1:]
    except ValueError:
        extra_args = []
    
    if len(extra_args) == 0:
        # No arguments: use latest year and next day
        year = find_latest_year()
        day = find_next_day(year)
        print(f"Downloading input for year {year}, day {day}...")
    elif len(extra_args) == 1:
        # One argument: day only, use latest year
        year = find_latest_year()
        try:
            day = int(extra_args[0])
        except ValueError:
            print(f"Error: Invalid day number '{extra_args[0]}'")
            sys.exit(1)
        print(f"Downloading input for year {year}, day {day}...")
    elif len(extra_args) >= 2:
        # Two arguments: year and day
        try:
            year = int(extra_args[0])
            day = int(extra_args[1])
        except ValueError:
            print(f"Error: Invalid year or day number")
            sys.exit(1)
        print(f"Downloading input for year {year}, day {day}...")
    
    # Validate day
    if not 1 <= day <= 25:
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)
    
    # Check if session cookie exists
    if not get_session_cookie():
        print("\nNo session cookie found!")
        print("Run 'python aoc.py --setup' to configure your session cookie.")
        sys.exit(1)
    
    # Determine output path
    project_root = Path(__file__).parent.parent
    day_path = project_root / 'years' / str(year) / str(day)
    
    # If day folder doesn't exist, create it with all template files
    if not day_path.exists():
        print(f"Day folder doesn't exist, creating with templates...")
        if create_day_folder(year, day, auto_download=True):
            print(f"✓ Successfully created day {day} for year {year}")
        else:
            print("✗ Failed to create day folder")
            sys.exit(1)
    else:
        # Day exists, just download input if it doesn't exist or is empty
        input_path = day_path / 'input.txt'
        if input_path.exists() and input_path.stat().st_size > 0:
            print(f"Input file already exists at {input_path}")
            print("Skipping download to avoid overwriting.")
        else:
            if download_input(year, day, input_path):
                print(f"✓ Successfully downloaded to {input_path}")
            else:
                print("✗ Failed to download input")
                sys.exit(1)


def handle_readme(args):
    """Handle the readme command."""
    try:
        if '-r' in args:
            flag_idx = args.index('-r')
        else:
            flag_idx = args.index('--readme')
        extra_args = args[flag_idx + 1:]
    except ValueError:
        extra_args = []
    
    if len(extra_args) >= 1:
        try:
            year = int(extra_args[0])
            print(f"Generating README for year {year}...")
            generate_readme(year)
        except ValueError:
            print(f"Error: Invalid year '{extra_args[0]}'")
            sys.exit(1)
    else:
        generate_readme()


def run_all_days_for_year(year):
    """Run all solutions for a given year."""
    year_path = project_root / 'years' / str(year)
    
    if not year_path.exists():
        print(f"Error: Year {year} directory not found")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"Running all solutions for year {year}")
    print(f"{'='*60}\n")
    
    # Get all day directories (numeric folders)
    day_dirs = sorted([d for d in year_path.iterdir() if d.is_dir() and d.name.isdigit()], 
                      key=lambda x: int(x.name))
    
    if not day_dirs:
        print(f"No day directories found in year {year}")
        sys.exit(0)
    
    total_days = len(day_dirs)
    success_count = 0
    
    for day_dir in day_dirs:
        day = day_dir.name
        script_path = day_dir / 'solution.py'
        
        if not script_path.exists():
            # Fallback to old structure
            script_path = day_dir / 'part1.py'
        
        if not script_path.exists():
            print(f"Day {day:>2}: SKIP (solution.py not found)")
            continue
        
        print(f"\nDay {day:>2}:")
        print("-" * 60)
        
        result = subprocess.run(
            [sys.executable, script_path.name],
            cwd=script_path.parent,
            capture_output=False
        )
        
        if result.returncode == 0:
            success_count += 1
        else:
            print(f"ERROR: Day {day} failed with return code {result.returncode}")
    
    print(f"\n{'='*60}")
    print(f"Completed: {success_count}/{total_days} days ran successfully")
    print(f"{'='*60}\n")


def handle_run(args):
    """Handle the run command."""
    try:
        flag_idx = args.index('-run')
        extra_args = args[flag_idx + 1:]
    except ValueError:
        extra_args = []
    
    if len(extra_args) == 0:
        print("Error: Please specify at least a year or day number")
        print("Usage: aoc -run <year> [day] [part]")
        sys.exit(1)
    
    # Parse arguments
    year = find_latest_year()
    day = None
    part = 1
    
    if len(extra_args) == 1:
        # Could be just day (-run 5) or just year (-run 2021)
        try:
            value = int(extra_args[0])
            # If value > 25, treat as year and run all days
            if value > 25:
                year = value
                # Run all days for this year
                run_all_days_for_year(year)
                sys.exit(0)
            else:
                # Just a day number
                day = value
        except ValueError:
            print(f"Error: Invalid number '{extra_args[0]}'")
            sys.exit(1)
    elif len(extra_args) == 2:
        # Could be (day, part) or (year, day)
        try:
            first = int(extra_args[0])
            second = int(extra_args[1])
            
            # If first arg > 25, it's probably a year
            if first > 25:
                year = first
                day = second
            else:
                day = first
                part = second
        except ValueError:
            print(f"Error: Invalid arguments")
            sys.exit(1)
    elif len(extra_args) >= 3:
        # year, day, part
        try:
            year = int(extra_args[0])
            day = int(extra_args[1])
            part = int(extra_args[2])
        except ValueError:
            print(f"Error: Invalid arguments")
            sys.exit(1)
    
    # Validate
    if not 1 <= day <= 25:
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)
    if part not in [1, 2]:
        print(f"Error: Part must be 1 or 2, got {part}")
        sys.exit(1)
    
    # Find the file (look for solution.py first, fallback to part{part}.py for older structure)
    script_path = project_root / 'years' / str(year) / str(day) / 'solution.py'
    
    if not script_path.exists():
        # Fallback to old structure
        script_path = project_root / 'years' / str(year) / str(day) / f'part{part}.py'
    
    if not script_path.exists():
        print(f"Error: File not found: {script_path}")
        sys.exit(1)
    
    # Run the script from its directory so relative imports work
    result = subprocess.run(
        [sys.executable, script_path.name],
        cwd=script_path.parent
    )
    sys.exit(result.returncode)


def main():
    """Main entry point for the CLI."""
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        show_help()
        sys.exit(0)
    
    # Check for flags
    if '-h' in sys.argv or '--help' in sys.argv:
        show_help()
    elif '-n' in sys.argv or '--next' in sys.argv:
        create_next_day()
    elif '-r' in sys.argv or '--readme' in sys.argv:
        handle_readme(sys.argv)
    elif '-s' in sys.argv or '--setup' in sys.argv:
        setup_session_cookie()
    elif '-d' in sys.argv or '--download' in sys.argv:
        handle_download(sys.argv)
    elif '-run' in sys.argv:
        handle_run(sys.argv)
    else:
        print("Error: Unknown option. Use -h or --help for usage information.")
        sys.exit(1)


if __name__ == '__main__':
    main()

