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


def get_browser_cookie():
    """
    Try to get the AoC session cookie from browser cookie stores.
    Supports Chrome, Firefox, and Safari on macOS.
    
    Returns:
        str: The session cookie value or None if not found
    """
    import sqlite3
    import shutil
    import tempfile
    
    # Try Chrome
    chrome_cookie_path = Path.home() / 'Library/Application Support/Google/Chrome/Default/Cookies'
    if chrome_cookie_path.exists():
        try:
            # Chrome locks the DB, so copy it first
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                shutil.copy2(chrome_cookie_path, tmp.name)
                conn = sqlite3.connect(tmp.name)
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT value, encrypted_value FROM cookies WHERE host_key = '.adventofcode.com' AND name = 'session'"
                )
                row = cursor.fetchone()
                conn.close()
                os.unlink(tmp.name)
                if row and row[0]:
                    return row[0]
        except Exception:
            pass
    
    # Try Firefox
    firefox_dir = Path.home() / 'Library/Application Support/Firefox/Profiles'
    if firefox_dir.exists():
        for profile in firefox_dir.iterdir():
            cookie_file = profile / 'cookies.sqlite'
            if cookie_file.exists():
                try:
                    with tempfile.NamedTemporaryFile(delete=False) as tmp:
                        shutil.copy2(cookie_file, tmp.name)
                        conn = sqlite3.connect(tmp.name)
                        cursor = conn.cursor()
                        cursor.execute(
                            "SELECT value FROM moz_cookies WHERE host = '.adventofcode.com' AND name = 'session'"
                        )
                        row = cursor.fetchone()
                        conn.close()
                        os.unlink(tmp.name)
                        if row:
                            return row[0]
                except Exception:
                    pass
    
    # Try Safari
    safari_cookie_path = Path.home() / 'Library/Cookies/Cookies.binarycookies'
    # Safari uses a binary format that's more complex to parse, skip for now
    
    return None


def setup_session_cookie():
    """
    Interactive setup to save session cookie to config file.
    Tries to auto-fetch from browser first.
    """
    print("Session Cookie Setup")
    print("=" * 50)
    
    # Try to auto-fetch from browser
    print("\nAttempting to fetch cookie from browser...")
    browser_cookie = get_browser_cookie()
    
    if browser_cookie:
        print("✓ Found session cookie in browser!")
        config_file = Path(__file__).parent.parent / '.aoc_session'
        config_file.write_text(browser_cookie)
        print(f"✓ Session cookie saved to {config_file}")
        return True
    
    print("Could not auto-fetch cookie from browser.")
    print("\nTo get your session cookie manually:")
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

