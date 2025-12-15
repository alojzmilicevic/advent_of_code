import importlib
from pathlib import Path


def get_metadata(year):
    """Dynamically load metadata for a given year."""
    try:
        module = importlib.import_module(f'year{year}.metadata')
        return module.get_metadata()
    except (ModuleNotFoundError, AttributeError):
        return None
