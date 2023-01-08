sudoku_grid = [
    [5, 0, 0, 2, 0, 4, 8, 0, 0],
    [0, 7, 0, 0, 0, 9, 0, 3, 0],
    [0, 1, 0, 0, 3, 0, 0, 4, 0],
    [0, 5, 0, 3, 6, 1, 2, 0, 0],
    [2, 0, 0, 9, 0, 5, 0, 0, 4],
    [0, 0, 3, 4, 2, 7, 0, 5, 0],
    [0, 2, 0, 0, 5, 0, 0, 8, 0],
    [0, 4, 0, 1, 0, 0, 0, 2, 0],
    [0, 0, 5, 8, 0, 2, 0, 0, 7],
]

# Function that uses backtracking algorithm through recursion 
def solver(grid):
    # Base case - If no there are no empty spaces (i.e. = 0) then grid is solved
    empty = get_empty(grid)
    if not empty:
        return True
    else:
        # Set row and column to be empty position in grid
        row, col = empty
        # guess values 1-10
        for guess in range(1,10):
            # Check to see if guess is a possible solution to empty position
            # If possible set position to the guess
            if is_possible(row, col, grid, guess):
                grid[row][col] = guess

                if solver(grid):
                    return True
                
                grid[row][col] = 0

    return False
        
# Function to print grid to terminal that separates boxes (3x3 areas of grid)
def print_grid(grid):

    # Print horizontal line to separate every 3 rows 
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        # Print vertical line to separate every 3 columns
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # Check to see if we're at last position to start new line
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

# Define function that will return index of empty squares
def get_empty(grid):
    for r in range(len(grid)): # r - row
        for c in range(len(grid[0])): # c - column
            if grid[r][c] == 0:
                return (r, c)

# Check to see if number in square satsfies three conditions of sodoku
def is_possible(row, col, grid, num):
    # Check if there is the same number in row
    row_nums = grid[row]
    if num in row_nums:
        return False

    # Check if there is the same number in column 
    col_nums = [grid[i][col] for i in range(len(grid))]
    if num in col_nums:
        return False

    # Check if there is same number in 3x3 block
    # Use integer division to designate boxes on grid
    row_box = (row // 3) 
    col_box = (col // 3)

    for r in range(row_box*3, row_box + 3): # to iterate through each of the three rows in box
        for c in range(col_box*3, col_box + 3): # to iterate through each of the three columns in box
            if grid[r][c] == num:
                return False

    # If we've satisfied the three condtions the number is a possible guess --> return True
    return True

print(print_grid(sudoku_grid))
solver(sudoku_grid)
print(print_grid(sudoku_grid))