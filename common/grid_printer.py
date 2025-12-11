"""
Grid printing utilities with color support
"""

# ANSI Color codes
class Colors:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def print_colored_grid(grid, color_map=None, spacing=True):
    """
    Print a 2D grid with optional colors.
    
    Args:
        grid: 2D array/list to print
        color_map: Dictionary mapping cell values to color codes
                   Example: {0: Colors.BLACK, 1: Colors.RED, 2: Colors.GREEN}
        spacing: Whether to add space between cells (default True)
    
    Example:
        grid = [[0, 1, 2], [1, 0, 1]]
        print_colored_grid(grid, {
            0: Colors.BLACK,
            1: Colors.RED,
            2: Colors.GREEN
        })
    """
    if color_map is None:
        color_map = {}
    
    separator = ' ' if spacing else ''
    
    for row in grid:
        for cell in row:
            color = color_map.get(cell, Colors.RESET)
            print(f"{color}{cell}{Colors.RESET}", end=separator)
        print()


def print_colored_array(array, color_map=None, spacing=True):
    """
    Print a 1D array with optional colors.
    
    Args:
        array: 1D array/list to print
        color_map: Dictionary mapping values to color codes
        spacing: Whether to add space between items (default True)
    
    Example:
        array = [0, 1, 2, 1, 0]
        print_colored_array(array, {
            0: Colors.BLACK,
            1: Colors.RED,
            2: Colors.GREEN
        })
    """
    if color_map is None:
        color_map = {}
    
    separator = ' ' if spacing else ''
    
    for item in array:
        color = color_map.get(item, Colors.RESET)
        print(f"{color}{item}{Colors.RESET}", end=separator)
    print()



