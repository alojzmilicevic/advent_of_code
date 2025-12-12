"""
Parsing utilities for common patterns in Advent of Code inputs.
"""
import re


def extract_brackets(text):
    """Extract content from [...] brackets."""
    match = re.search(r'\[(.*?)\]', text)
    return match.group(1) if match else None


def extract_parens(text):
    """Extract all (...) parentheses groups."""
    return re.findall(r'\(([^\)]+)\)', text)


def extract_braces(text):
    """Extract content from {...} braces."""
    match = re.search(r'\{([^\}]+)\}', text)
    return match.group(1) if match else None


def extract_angles(text):
    """Extract content from <...> angle brackets."""
    match = re.search(r'<([^>]+)>', text)
    return match.group(1) if match else None

