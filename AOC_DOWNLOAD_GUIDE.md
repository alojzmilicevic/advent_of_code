# Advent of Code Input Download Guide

## Overview

The CLI now supports automatically downloading input files from adventofcode.com using your session cookie.

## Quick Start

### 1. Setup Your Session Cookie (One-time)

```bash
python aoc.py --setup
```

This will prompt you to paste your session cookie, which will be saved to `.aoc_session` (this file is in `.gitignore` to keep it private).

### 2. Get Your Session Cookie

1. Log in to https://adventofcode.com
2. Open browser developer tools (F12)
3. Go to the **Application** (Chrome) or **Storage** (Firefox) tab
4. Navigate to **Cookies** in the left sidebar
5. Click on `https://adventofcode.com`
6. Find the cookie named `session`
7. Copy its **Value** (a long hexadecimal string)

### 3. Download Input

Once your session cookie is configured, you can download inputs:

```bash
# Download input for the latest day (auto-detects based on your folders)
python aoc.py -d

# Download input for day 5 (latest year)
python aoc.py -d 5

# Download input for year 2024, day 5
python aoc.py -d 2024 5
```

## Alternative: Environment Variable

Instead of using `--setup`, you can set an environment variable:

**Windows (PowerShell):**
```powershell
$env:AOC_SESSION = "your_session_cookie_here"
```

**Windows (CMD):**
```cmd
set AOC_SESSION=your_session_cookie_here
```

**Linux/Mac:**
```bash
export AOC_SESSION=your_session_cookie_here
```

## Automatic Download When Creating New Day

When you create a new day with `python aoc.py --next`, the CLI will automatically attempt to download the input file if your session cookie is configured. If it fails or you haven't set up the cookie, it will create an empty `input.txt` file instead.

## File Locations

- **Session cookie file:** `.aoc_session` (in project root)
- **Downloaded inputs:** `year{YEAR}/{DAY}/input.txt`

## Troubleshooting

### "No session cookie found"
Run `python aoc.py --setup` to configure your session cookie.

### "Day X not found for year Y"
The puzzle might not be released yet. Puzzles are released at midnight EST (UTC-5).

### "Invalid session cookie"
Your session cookie may have expired. Log in to Advent of Code again and update your cookie with `python aoc.py --setup`.

## Security Note

⚠️ **Never commit your `.aoc_session` file to git!** This file contains your private session cookie and is already in `.gitignore`.

