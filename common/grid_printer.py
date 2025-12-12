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


def print_table(grid, color_map=None, col_headers=None, row_headers=None, 
                extra_cols=None, extra_col_header=None, spacing=True):
    """
    Print a table with headers and optional colors.
    
    Args:
        grid: 2D array/list to print
        color_map: Dictionary mapping cell values to color codes
        col_headers: List of column header labels
        row_headers: List of row header labels
        extra_cols: List of additional column(s) to display after main grid
        extra_col_header: Header for the extra column(s)
        spacing: Whether to add space between cells (default True)
    
    Example:
        grid = [[0, 0, 1], [1, 0, 0]]
        print_table(grid, 
            color_map={0: Colors.BLACK, 1: Colors.GREEN},
            col_headers=['b₀', 'b₁', 'b₂'],
            row_headers=['L0:', 'L1:'],
            extra_cols=[0, 1],
            extra_col_header='Goal'
        )
    """
    if color_map is None:
        color_map = {}
    
    separator = '  ' if spacing else ' '
    
    # Print column headers
    if col_headers:
        # Print row header space
        if row_headers:
            print(' ' * 8, end='')
        
        # Print main column headers
        for header in col_headers:
            print(f"{header:>2}", end=separator)
        
        # Print separator before extra column
        if extra_cols is not None:
            print('|', end=' ')
            if extra_col_header:
                print(extra_col_header, end='')
        
        print()
        
        # Print separator line
        if row_headers:
            print(' ' * 7, end='')
        print('-' * (len(col_headers) * 3 + 2), end='')
        if extra_cols is not None:
            print('+' + '-' * 6)
        else:
            print()
    
    # Print rows with data
    for i, row in enumerate(grid):
        # Print row header
        if row_headers and i < len(row_headers):
            print(f"{row_headers[i]:>7}", end=' ')
        
        # Print row cells
        for cell in row:
            color = color_map.get(cell, Colors.RESET)
            print(f"{color}{cell:>2}{Colors.RESET}", end=separator)
        
        # Print extra column
        if extra_cols is not None and i < len(extra_cols):
            print('| ', end=' ')
            extra_val = extra_cols[i]
            color = color_map.get(extra_val, Colors.RESET)
            print(f"{color}{extra_val}{Colors.RESET}", end='')
        
        print()






