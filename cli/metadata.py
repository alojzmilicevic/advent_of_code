"""
Metadata management for Advent of Code puzzles.
Handles fetching puzzle titles, emoji selection, and storing metadata.
"""
import json
import urllib.request
import urllib.error
import re
from pathlib import Path


# Keyword to emoji mapping for auto-suggestion
EMOJI_KEYWORDS = {
    # Nature & Weather
    'tree': '🎄', 'snow': '❄️', 'ice': '🧊', 'star': '⭐', 'light': '💡',
    'fire': '🔥', 'water': '💧', 'rock': '🪨', 'mountain': '⛰️',
    
    # Christmas themed
    'christmas': '🎄', 'gift': '🎁', 'present': '🎁', 'santa': '🎅',
    'elf': '🧝', 'reindeer': '🦌', 'sleigh': '🛷', 'candy': '🍬', 'stocking': '🧦',
    'wreath': '🎄', 'ornament': '🎄', 'chimney': '🏠', 'north pole': '🎅',
    
    # Buildings & Places
    'house': '🏠', 'factory': '🏭', 'warehouse': '🏭', 'shop': '🏪',
    'lobby': '🏛️', 'room': '🚪', 'door': '🚪', 'entrance': '🚪',
    'bridge': '🌉', 'tower': '🗼', 'castle': '🏰', 'cave': '🕳️',
    'garden': '🌻', 'farm': '🌾', 'forest': '🌲', 'jungle': '🌴',
    'lab': '🧪', 'laboratory': '🧪', 'reactor': '⚛️', 'theater': '🎬',
    'cinema': '🎬', 'movie': '🎬', 'playground': '🎮', 'cafeteria': '🍽️',
    'kitchen': '🍳', 'basement': '🏚️', 'attic': '🏠', 'apartment': '🏢',
    
    # Objects
    'robot': '🤖', 'machine': '⚙️', 'gear': '⚙️', 'engine': '🔧',
    'map': '🗺️', 'compass': '🧭', 'key': '🔑', 'lock': '🔐',
    'box': '📦', 'package': '📦', 'rope': '🪢', 'ribbon': '🎀',
    'mirror': '🪞', 'lens': '🔍', 'printer': '🖨️', 'print': '🖨️',
    'trash': '🗑️', 'pipe': '🔧', 'wire': '🔌', 'cable': '🔌',
    'lantern': '🏮', 'lamp': '💡', 'candle': '🕯️', 'cookie': '🍪',
    'paper': '📄', 'string': '🧵', 'packet': '📦', 'passport': '📕',
    
    # Transport
    'ship': '🚢', 'boat': '⛵', 'submarine': '🚤', 'rocket': '🚀',
    'plane': '✈️', 'train': '🚂', 'cart': '🛒', 'car': '🚗', 'ferry': '⛴️',
    
    # Science & Math
    'math': '🔢', 'number': '🔢', 'code': '💻', 'password': '🔑', 'hash': '#️⃣',
    'sequence': '🔢', 'pattern': '🔷', 'grid': '📊', 'cube': '🧊',
    'hex': '⬡', 'binary': '🔢', 'signal': '📡', 'radar': '📡',
    'circuit': '🔌', 'logic': '🧠', 'register': '💾', 'memory': '🧠',
    'amplifier': '📢', 'sensor': '📡', 'scanner': '📡', 'calibration': '🎯',
    
    # Creatures
    'monkey': '🐒', 'elephant': '🐘', 'crab': '🦀', 'octopus': '🐙',
    'fish': '🐟', 'whale': '🐋', 'amphipod': '🦐', 'lanternfish': '🐠',
    'dragon': '🐉', 'sea': '🌊', 'squid': '🦑',
    
    # Games & Actions
    'game': '🎮', 'dice': '🎲', 'card': '🃏', 'puzzle': '🧩',
    'race': '🏁', 'chase': '🏃', 'search': '🔍', 'find': '🔍',
    'spin': '🔄', 'shuffle': '🔀', 'sort': '📊', 'count': '🔢',
    
    # Abstract
    'path': '🛤️', 'route': '🛤️', 'passage': '🚶', 'beacon': '📡',
    'time': '⏰', 'space': '🌌', 'portal': '🌀', 'dimension': '🌀',
    'magic': '✨', 'trick': '🎩', 'secret': '🤫', 'transparent': '👻',
    'infinite': '♾️', 'spiral': '🌀', 'loop': '🔄',
    
    # Intcode / Computer
    'intcode': '💻', 'computer': '💻', 'program': '💻', 'opcode': '💻',
    'ascii': '💻', 'springdroid': '🤖', 'droid': '🤖',
    
    # Misc AoC themes
    'orbit': '🪐', 'planet': '🪐', 'asteroid': '☄️', 'moon': '🌙',
    'oxygen': '💨', 'fuel': '⛽', 'password': '🔐', 'image': '🖼️',
    'layer': '📚', 'floor': '🏢', 'level': '📊', 'safe': '🔒',
}

DEFAULT_EMOJI = '🎄'


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_metadata_path(year):
    """Get the path to the metadata JSON file for a year."""
    return get_project_root() / f'year{year}' / 'metadata.json'


def load_metadata(year):
    """Load metadata for a year from JSON file."""
    path = get_metadata_path(year)
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_metadata(year, metadata):
    """Save metadata for a year to JSON file."""
    path = get_metadata_path(year)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def get_day_metadata(year, day):
    """Get metadata for a specific day."""
    metadata = load_metadata(year)
    return metadata.get(str(day))


def set_day_metadata(year, day, name, emoji):
    """Set metadata for a specific day."""
    metadata = load_metadata(year)
    metadata[str(day)] = {'name': name, 'emoji': emoji}
    save_metadata(year, metadata)


def fetch_puzzle_title(year, day, session=None):
    """
    Fetch the puzzle title from adventofcode.com.
    
    Args:
        year: The year
        day: The day
        session: Optional session cookie (needed for current year puzzles)
    
    Returns:
        str: The puzzle title, or None if not found
    """
    url = f"https://adventofcode.com/{year}/day/{day}"
    
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'advent-of-code-cli by github.com/alojzmilicevic')
        
        if session:
            req.add_header('Cookie', f'session={session}')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            
            # Parse title from HTML: <h2>--- Day X: Title ---</h2>
            match = re.search(r'<h2>--- Day \d+: (.+?) ---</h2>', html)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Warning: Could not fetch puzzle title: {e}")
    
    return None


def suggest_emoji(title):
    """
    Suggest an emoji based on the puzzle title using keyword matching.
    
    Args:
        title: The puzzle title
    
    Returns:
        str: Suggested emoji or None if no match found
    """
    if not title:
        return None
    
    title_lower = title.lower()
    
    # Check each keyword
    for keyword, emoji in EMOJI_KEYWORDS.items():
        if keyword in title_lower:
            return emoji
    
    return None


def prompt_for_emoji(title, suggested=None):
    """
    Prompt the user to enter an emoji.
    
    Args:
        title: The puzzle title
        suggested: Optional suggested emoji
    
    Returns:
        str: The chosen emoji
    """
    if suggested:
        prompt = f'Enter emoji for "{title}" (Enter for {suggested}): '
    else:
        prompt = f'Enter emoji for "{title}" (Enter for {DEFAULT_EMOJI}): '
    
    try:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        return suggested or DEFAULT_EMOJI
    except (EOFError, KeyboardInterrupt):
        return suggested or DEFAULT_EMOJI


def auto_add_metadata(year, day, session=None, interactive=True):
    """
    Automatically fetch and add metadata for a day.
    
    Args:
        year: The year
        day: The day
        session: Optional session cookie
        interactive: Whether to prompt for emoji if no match found
    
    Returns:
        tuple: (name, emoji) or (None, None) if failed
    """
    # Check if already exists
    existing = get_day_metadata(year, day)
    if existing:
        return existing['name'], existing['emoji']
    
    # Fetch title
    title = fetch_puzzle_title(year, day, session)
    if not title:
        title = f"Day {day}"
    
    print(f'  Puzzle title: "{title}"')
    
    # Try to suggest emoji
    suggested = suggest_emoji(title)
    
    if suggested:
        print(f'  Auto-selected emoji: {suggested}')
        emoji = suggested
    elif interactive:
        emoji = prompt_for_emoji(title)
    else:
        emoji = DEFAULT_EMOJI
    
    # Save metadata
    set_day_metadata(year, day, title, emoji)
    print(f'  ✓ Added metadata: {emoji} {title}')
    
    return title, emoji


# For backwards compatibility with old metadata.py files
class Day:
    """Simple class to hold day metadata (for backwards compatibility)."""
    def __init__(self, name, emoji='🎄'):
        self.name = name
        self.emoji = emoji


def get_metadata(year):
    """
    Get metadata for a year in the old format (dict of Day objects).
    This provides backwards compatibility with existing code.
    """
    metadata = load_metadata(year)
    if not metadata:
        # Try loading from old Python metadata.py file
        try:
            import importlib
            module = importlib.import_module(f'year{year}.metadata')
            return module.get_metadata()
        except (ModuleNotFoundError, AttributeError):
            return None
    
    # Convert to Day objects
    return {int(k): Day(v['name'], v['emoji']) for k, v in metadata.items()}
