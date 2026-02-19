from random import randrange

# Initialize the board with numbers 1-9
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


# Function to display the board
def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|  {}   |  {}   |  {}   |".format(*row))
        print("|       |       |       |")
        print("+-------+-------+-------+")


# Function to make a list of free squares
def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):  # free squares are integers
                free.append((i, j))
    return free


# Function to check victory
def victory_for(board, sign):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


# Function for user's move
def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Invalid input. Enter a number from 1-9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Number must be 1-9.")
            continue
        # Find row and col
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = 'O'
                    return
        print("That square is already occupied. Choose another.")


# Function for computer's move
def draw_move(board):
    free = make_list_of_free_fields(board)
    if not free:
        return
    i, j = free[randrange(len(free))]
    board[i][j] = 'X'


# Main game
# First move is always computer in the middle
board[1][1] = 'X'

while True:
    display_board(board)

    if victory_for(board, 'X'):
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    enter_move(board)

    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("It's a tie!")
        break

    draw_move(board)
