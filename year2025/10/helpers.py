from common import grid_printer


def print_table(augmented_matrix):
    print()
    """Print augmented matrix [A|b] where last column is the goal."""
    # Separate matrix and goal column
    matrix_only = [row[:-1] for row in augmented_matrix]  
    goals = [row[-1] for row in augmented_matrix]         
    
    # Create column headers (b0, b1, b2, ...)
    col_headers = [f'b{i}' for i in range(len(matrix_only[0]))]
    # Create row headers (L0:, L1:, L2:, ...)
    row_headers = [f'L{i}:' for i in range(len(matrix_only))]
    
    grid_printer.print_table(
        matrix_only,
        color_map={
            0: grid_printer.Colors.BLACK,
            1: grid_printer.Colors.GREEN
        },
        col_headers=col_headers,
        row_headers=row_headers,
        extra_cols=goals,
        extra_col_header='Goal'
    )

