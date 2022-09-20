# Things to do:
# 1. Set up board using a list of lists. Create a temporary board.
# 2. Create functions that will merge left, right, up and down. Will create functions to reverse and transpose the list of lists to do this.
# 3. Set up the start of the game, creating an empty gameboard filled with two random values.
# 4. Set up the rounds of the game, where the user will have the option to merge in any one of the four directions, and after they move then new board will display.
# 5. Set up adding a new value each time.
# 6. Set up functions testing if the user has won or lost.

# This is a temporary board that I will use to test code on. It will be filled with random values to simulate a game.
board = [[0, 0, 2, 2], [2, 2, 2, 0], [4, 0, 0, 4], [0, 2, 0, 0]]

# We need to create a 'display' function that will display the board in a 4 * 4 grid in our terminal.
def display():
    #This loop will look through every row in the board.
    for row in board:
        # I would like the board to have vertical lines between each cell in the 4 * 4 grid.
        current_row = '|'
        # This loop will now look through each individual cell in the row.
        for cell in row:
            # If the cell has a value of 0, I would like to display an empty space in the cell.
            if cell == 0:
                current_row += ' |'
            # If the cell has a value greater than 0, I would like to display the value in the cell. I would like to display this value as a string instead of an integer.
            else:
                current_row += str(cell) + '|'
        # I would now like to display the generated row.
        print(current_row)
    # We should also print an empty print statement to print an extra line.
    print()

display()