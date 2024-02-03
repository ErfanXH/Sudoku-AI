import numpy as np
from itertools import product
from collections import defaultdict

# Generator


def generate_sudoku():
    """
        Function to generate a Sudoku grid


        Fill the diagonal boxes of the Sudoku grid
        Solve the Sudoku grid
        Remove elements from the grid to create a puzzle
    """

    ############
    ##        ##
    ##  Code  ##
    ##        ##
    ############


def fill_diagonal(grid):
    """
        Function to fill the diagonal boxes of the Sudoku grid
    """
    for i in range(0, 9, 3):
        fill_box(grid, i, i)


def fill_box(grid, row, col):
    """
        Function to fill a box with random values
    """
    for i in range(3):
        for j in range(3):
            num = np.random.randint(1, 10)
            while not is_safe(grid, row + i, col + j, num):
                num = np.random.randint(1, 10)
            grid[row + i][col + j] = int(num)


def is_safe(grid, row, col, num):
    """
        Function to check if it is safe to place a number in a particular position
    """

    return (
        not used_in_row(grid, row, num)
        and not used_in_column(grid, col, num)
        and not used_in_box(grid, row - row % 3, col - col % 3, num)
    )


def used_in_row(grid, row, num):
    """
        Function to check if a number is used in a row
    """
    for i in range(9):
        if grid[row][i] == num:
            return True

    return False


def used_in_column(grid, col, num):
    """
        Function to check if a number is used in a column
    """
    for i in range(9):
        if grid[i][col] == num:
            return True

    return False


def used_in_box(grid, box_start_row, box_start_col, num):
    """
        Function to check if a number is used in a 3x3 box
    """
    for i in range(3):
        for j in range(3):
            if grid[i + box_start_row][j + box_start_col] == num:
                return True

    return False


def find_unassigned_location(grid):
    """
        Function to find an unassigned location in the grid
    """

    ############
    ##        ##
    ##  Code  ##
    ##        ##
    ############


def remove_elements(grid, num_elements):
    """
        Function to remove elements from the grid
    """

    ############
    ##        ##
    ##  Code  ##
    ##        ##
    ############

# Backtracking


def solve_sudoku(grid):
    """
        Function to solve the Sudoku grid using backtracking
    """

    ############
    ##        ##
    ##  Code  ##
    ##        ##
    ############


def display_grid(grid):
    """
        Function to display the Sudoku grid
    """

    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

# Backtracking - Continued


def solve_sudoku_csp(grid):
    """
        Function to solve the Sudoku grid using Constraint Satisfaction Problem (CSP)
    """

    def create_domains(grid):
        """
            Function to create domains for each cell in the grid
        """

        ############
        ##        ##
        ##  Code  ##
        ##        ##
        ############

    def is_valid_assignment(i, j, val, assignment):
        """
            Function to check if assigning a value to a cell is valid

            Check if the value is already used in the same row
            Check if the value is already used in the same column
            Check if the value is already used in the same 3x3 box
        """

        ############
        ##        ##
        ##  Code  ##
        ##        ##
        ############

    def find_unassigned_location(assignment):
        """
            Function to find an unassigned location in the grid
        """

        ############
        ##        ##
        ##  Code  ##
        ##        ##
        ############

    # Recursive function to solve the Sudoku grid using CSP
    def solve_csp(assignment):
        i, j = find_unassigned_location(assignment)
        if i == -1 and j == -1:
            return True

        # Try assigning each possible value to the unassigned location
        for val in assignment[(i, j)].copy():
            if is_valid_assignment(i, j, val, assignment):
                assignment[(i, j)] = val
                if solve_csp(assignment):
                    return True
                assignment[(i, j)] = 0
        return False

    # Create initial domains for each cell in the grid
    domains = create_domains(grid)
    assignment = {(i, j): val for (i, j), val in domains.items()}

    # Solve the Sudoku grid using CSP
    if solve_csp(assignment):
        solved_grid = [[assignment[(i, j)] for j in range(9)]
                       for i in range(9)]
        return solved_grid
    else:
        return None

# Show Result

# Function to initialize the Sudoku grid


def initializing_grid():
    print("\nInitial Sudoku\n")
    sudoku_grid = generate_sudoku()
    for i in sudoku_grid:
        for j in i:
            print(j, end=' ')
        print("")
    print(end='\n\n\n\n\n')
    return sudoku_grid


# Function to solve the Sudoku grid using backtracking
def backtracking_answer(sudoku_grid):
    print("Back Tracking Answer:\n\n")
    if solve_sudoku(sudoku_grid):
        print("Sudoku solved successfully:")
        display_grid(sudoku_grid)
    else:
        print("No solution exists for the given Sudoku.")
    print(end='\n\n\n\n\n')


# Function to solve the Sudoku grid using CSP
def csp_answer(sudoku_grid):
    print("CSP Answer:\n")
    solved_grid = solve_sudoku_csp(sudoku_grid)
    if solved_grid is not None:
        print("Sudoku solved successfully:")
        for row in solved_grid:
            for r1 in row:
                for r2 in r1:
                    print(r2, end=' ')
            print()
    else:
        print("No solution exists for the given Sudoku.")
    print(end='\n\n\n\n\n')


# Main
# Generate and display the initial Sudoku grid
generate_sudoko = initializing_grid()

# Solve the Sudoku grid using backtracking
backtracking_answer(generate_sudoko)

# Solve the Sudoku grid using CSP
csp_answer(generate_sudoko)