#!/usr/bin/env python3
"""
Advent of Code CLI Tool
"""
import sys
import argparse
from pathlib import Path

# Add project root to path so we can import modules
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from common.create_next_day import main as create_next_day
from common.aoc_downloader import download_input, setup_session_cookie, get_session_cookie
from common.create_next_day import find_latest_year, find_next_day
from readme_generator import main as generate_readme


def show_help():
    """Display help information."""
    help_text = """
Advent of Code CLI Tool
=======================

Usage: python aoc.py [OPTION] [ARGS]

Options:
  -n, --next        Create the next day's folder structure with template files
  -d, --download    Download input for a specific day (or today's day)
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
  python aoc.py -s                    # Setup session cookie
  python aoc.py --setup               # Same as above
  python aoc.py -r                    # Generate all README files
  python aoc.py --readme              # Same as above
  python aoc.py -h                    # Show this help

Description:
  -n, --next
      Automatically detects the latest year and creates the next day's folder
      with a.py, b.py, input.txt, and test.input.txt files.

  -d, --download [year] [day]
      Download input from adventofcode.com for the specified day.
      If no arguments: downloads for the latest day in the latest year
      If one argument: downloads for that day in the latest year
      If two arguments: downloads for specified year and day
      Requires session cookie (see --setup)

  -s, --setup
      Interactive setup to save your Advent of Code session cookie.
      This is required for downloading inputs.

  -r, --readme
      Generates README.md files for each year folder based on the metadata.py
      files, creating a table of problems and solutions.

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
    project_root = Path(__file__).parent
    output_path = project_root / f'year{year}' / str(day) / 'input.txt'
    
    # Download
    if download_input(year, day, output_path):
        print(f"✓ Successfully downloaded to {output_path}")
    else:
        print("✗ Failed to download input")
        sys.exit(1)


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
        generate_readme()
    elif '-s' in sys.argv or '--setup' in sys.argv:
        setup_session_cookie()
    elif '-d' in sys.argv or '--download' in sys.argv:
        handle_download(sys.argv)
    else:
        print("Error: Unknown option. Use -h or --help for usage information.")
        sys.exit(1)


if __name__ == '__main__':
    main()

