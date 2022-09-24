# Things to do:
# 1. Set up board using a list of lists. Create a temporary board.
# 2. Create functions that will merge left, right, up and down.
# 3. Set up the start of the game, creating an empty gameboard filled with two random values.
# 4. Set up the rounds of the game, where the user will have the option to merge in any one of the four directions, and after they move then new board will display.
# 5. Set up adding a new value each time.
# 6. Set up functions testing if the user has won or lost.

import random

# Blank board at the start of game.
board = []

# This function generates a new value of 2 or 4 on the board in between each move.
def new_value():
    # Using the random module to return a 4 once every 10 moves.
    if random.randint(1, 10) == 1:
        return 4
    # Therefore, 9 out of 10 moves will add a value of 2 to the board, but on the 10th move a 4 will be added instead.
    else:
        return 2

# This function will add a value to one of the random empty spaces on the board.
def add_new_value():
    row_number = random.randint(0, 3)
    column_number = random.randint(0, 3)

    # This function will continually scan through random spots until it finds one that is empty, then it will add the new number to the empty spot.
    while not board[row_number][column_number] == 0:
        row_number = random.randint(0, 3)
        column_number = random.randint(0, 3)
    
    # Fill the empty spot with the new value
    board[row_number][column_number] = new_value()

# This function will test if the user has won the game (i.e. the user has achieved a value of 2048).
def game_won():
    for row in board:
        if 2048 in row:
            return True
    return False

for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
    board.append(row)

# We need to create a 'display' function that will display the board in a 4 * 4 grid in our terminal.
def display():
    # We must first find the largest value in our board so that we can appropriately size each of the cells. For example:
    # As we can see below, the lines in the board do not line up as some values are long than others:
    # | | |2048|2|
    # |2|2|2| |
    # |4|16| |4|
    # | |2| |32|
    # Our goal is for the board to look something like below. As we can see, 2048 is the largest number with 4 characters, therefore we want each of the cells to we 4 characters wide:
    # |    |    |2048|   2|
    # |   2|   2|   2|    |
    # |   4|  16|    |   4|
    # |    |   2|    |  32|
    largest = board[0][0]
    for row in board:
        for cell in row:
            if cell > largest:
                largest = cell

    number_of_spaces = len(str(largest))

    # This loop will look through every row in the board.
    for row in board:
        # I would like the board to have vertical lines between each cell in the 4 * 4 grid.
        current_row = '|'
        # This loop will now look through each individual cell in the row.
        for cell in row:
            # If the cell has a value of 0, I would like the cell to be empty. However, it is important that the cell is still as wide as the largest number on the board, therefore we multiply the amount of empty spaces by 'number_of_spaces' (which contains the length of the largest number).
            if cell == 0:
                current_row += ' ' * number_of_spaces + '|'
            # If the cell has a value greater than 0, I would like to display the value in the cell. I would like to display this value as a string instead of an integer. Again, it is important that the cell is equivalent in width to the largest number on the board. As our numbers can vary in length, we cannot simply add 'number_of_spaces' to our number, instead we must calculate the difference in characters between the largest number and the number in the cell. For example, if the largest number on the board is '2048' we must add 2 empty spaces to '16', or 3 empty spaces to '2', or 1 empty space to '128'. As such, we subtract the length of the number in our current cell from the largest number, then we multiply our empty spaces by the result of this calculation. Finally, we can add our current number to the cell.
            else:
                current_row += (' ' * (number_of_spaces - len(str(cell)))) + str(cell) + '|'
        # I would now like to display the generated row.
        print(current_row)
    # We should also print an empty print statement to print an extra line.
    print()

# This function will merge one row to the left.
def merge_one_row_left(row):
    # We must first move everything within the row as far left as possible.
    for i in range(3):
        for j in range(3, 0, -1):
            # We have to test whether or not there is an empty space to the left of each cell. If there is an empty space, then we shift to that space.
            if row[j - 1] == 0:
                row[j - 1] = row[j]
                row[j] = 0

    # Now we must actually merge the values.
    for i in range(0, 3, 1):
        # Now we test if the value in the current cell is identical to the value to the left of the current cell. If it is, then we double the value of cell to the left, and make the current cell = 0.
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    
    # Move everything to the left again.
    for i in range(3, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row
    
# Now that we can merge one row to the left, we need to now merge the whole board to the left.
def merge_left(current_board):
    # We need to use the 'merge_one_row_left' function on each row on the board.
    for i in range(4):
        current_board[i] = merge_one_row_left(current_board[i])
    
    return current_board

# This function will merge one row to the right.
def merge_one_row_right(row):
    # We must first move everything within the row as far left as possible.
    for i in range(3):
        for j in range(0, 3, 1):
            # We have to test whether or not there is an empty space to the right of each cell. If there is an empty space, then we shift to that space.
            if row[j + 1] == 0:
                row[j + 1] = row[j]
                row[j] = 0

    # Now we must actually merge the values.
    for i in range(3, 0, -1):
        # Now we test if the value in the current cell is identical to the value to the right of the current cell. If it is, then we double the value of cell to the right, and make the current cell = 0.
        if row[i] == row[i - 1]:
            row[i] *= 2
            row[i - 1] = 0
    
    # Move everything to the right again.
    for i in range(0, 3, 1):
        if row[i + 1] == 0:
            row[i + 1] = row[i]
            row[i] = 0
    return row

# Now that we can merge one row to the left, we need to now merge the whole board to the left.
def merge_right(current_board):
    # We need to use the 'merge_one_row_right' function on each row on the board.
    for i in range(4):
        current_board[i] = merge_one_row_right(current_board[i])
    
    return current_board

# In order to create the 'merge up' function, we must do something known as 'transposing' the entire board. Once the board is in its transposed state, we must then use the 'merge left' function on the transposed board. After merging left, we use the transpose method again on the board to then return the board to its previous state. This will then merge all values up. 
def transpose(current_board):
    for i in range(4):
        for j in range(i, 4):
            if not j == i:
                temp = current_board[i][j]
                current_board[i][j] = current_board[j][i]
                current_board[j][i] = temp

    return current_board
    
def merge_up(current_board):
    current_board = transpose(current_board)
    current_board = merge_left(current_board)
    current_board = transpose(current_board)

    return current_board

def merge_down(current_board):
    current_board = transpose(current_board)
    current_board = merge_right(current_board)
    current_board = transpose(current_board)

    return current_board

# At the start of the game we need to fill the board with two values.
values_added = 2
while values_added > 0:
    row_number = random.randint(0, 3)
    column_number = random.randint(0, 3)

    if board[row_number][column_number] == 0:
        board[row_number][column_number] = new_value()
        values_added -= 1
    
print("Welcome to 2048! Use 'w' to merge up, 'a' to merge left, 's' to merge down and 'd' to merge right.")

display()

game_over = False

# Repeat asking the user for new moves while the game isn't over.
while not game_over:
    move = input("Which direction do you wish to merge? ")
    
    # We'll assume the user enters a valid input for now.
    valid_input = True

    # Figue out which direction the user wants to merge, and then use the correct function to merge in the respective direction.
    if move == 'w':
        board = merge_up(board)
    elif move == 'a':
        board = merge_left(board)
    elif move == 's':
        board = merge_down(board)
    elif move == 'd':
        board = merge_right(board)
    else:
        valid_input = False

    # If the user did not enter either 'w', 'a', 's', or 'd' - their input is invalid, therefore we'll return the following.
    if valid_input == False:
        print("Your input was invalid. Please only enter 'w', 'a', 's' or 'd'. ")
    else:
        if game_won == True:
            display()
            print('Congratulations! You got 2048 and won the game!')
            game_over = True
        add_new_value()
        display()
