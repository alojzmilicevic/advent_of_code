"""
Download input files from Advent of Code website.
"""
import urllib.request
import urllib.error
from pathlib import Path
import os


def get_session_cookie():
    """
    Get the session cookie from environment variable or config file.
    
    Returns:
        str: The session cookie value or None if not found
    """
    # Try environment variable first
    session = os.environ.get('AOC_SESSION')
    if session:
        return session
    
    # Try reading from config file in project root
    config_file = Path(__file__).parent.parent / '.aoc_session'
    if config_file.exists():
        return config_file.read_text().strip()
    
    return None


def download_input(year, day, output_path=None):
    """
    Download input file from Advent of Code for a specific year and day.
    
    Args:
        year (int): The year (e.g., 2025)
        day (int): The day (1-25)
        output_path (Path, optional): Where to save the file. If None, returns content.
    
    Returns:
        str: The input content if output_path is None
        bool: True if successfully saved, False otherwise
    """
    session = get_session_cookie()
    if not session:
        print("Error: No session cookie found!")
        print("Please set one of the following:")
        print("  1. Environment variable: AOC_SESSION=your_session_cookie")
        print("  2. Create file: .aoc_session in project root with your session cookie")
        print("\nTo get your session cookie:")
        print("  1. Log in to https://adventofcode.com")
        print("  2. Open browser developer tools (F12)")
        print("  3. Go to Application/Storage > Cookies")
        print("  4. Copy the value of the 'session' cookie")
        return False
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    
    try:
        # Create request with session cookie
        req = urllib.request.Request(url)
        req.add_header('Cookie', f'session={session}')
        req.add_header('User-Agent', 'advent-of-code-cli by github.com/yourusername')
        
        # Download the input
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
            if output_path:
                # Save to file
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(content)
                return True
            else:
                # Return content
                return content
                
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Day {day} not found for year {year}. It might not be released yet.")
        elif e.code == 400:
            print(f"Error: Invalid session cookie or request.")
        elif e.code == 500:
            print(f"Error: Server error. The puzzle might not be available yet.")
        else:
            print(f"Error: HTTP {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to adventofcode.com - {e.reason}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def setup_session_cookie():
    """
    Interactive setup to save session cookie to config file.
    """
    print("Session Cookie Setup")
    print("=" * 50)
    print("\nTo get your session cookie:")
    print("  1. Log in to https://adventofcode.com")
    print("  2. Open browser developer tools (F12)")
    print("  3. Go to Application/Storage > Cookies")
    print("  4. Copy the value of the 'session' cookie")
    print("\n" + "=" * 50)
    
    session = input("\nPaste your session cookie here: ").strip()
    
    if not session:
        print("Error: No session cookie provided.")
        return False
    
    # Save to config file
    config_file = Path(__file__).parent.parent / '.aoc_session'
    config_file.write_text(session)
    print(f"\n✓ Session cookie saved to {config_file}")
    print("Note: This file is in .gitignore to keep your session private.")
    
    return True


if __name__ == '__main__':
    # Test download
    import sys
    if len(sys.argv) >= 3:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
        content = download_input(year, day)
        if content:
            print(content)
    else:
        print("Usage: python aoc_downloader.py <year> <day>")

