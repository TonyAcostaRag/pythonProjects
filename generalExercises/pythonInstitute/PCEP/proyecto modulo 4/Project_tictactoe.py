from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    for rows in board:
        
        print("|       |       |       |")
        for cell in rows:
            print("|  ", cell, "  ", end="")
            
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    print("Human moving")
    calculate_move('O')
    print("Human done")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    list_spaces = []
    index_counter = 1
    row_index = 0
    
    for rows in board:
        column_index = 0
        
        for cell in rows:
            if cell == index_counter:
                list_spaces.append((row_index+1, column_index+1))
            index_counter += 1
            column_index += 1
        row_index += 1
    
    print("Available spaces\n", list_spaces)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == sign:
        print("Victory for: " + sign)
        return False
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == sign:
        print("Victory for: " + sign)
        return False
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == sign:
        print("Victory for: " + sign)
        return False
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == sign:
        print("Victory for: " + sign)
        return False
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == sign:
        print("Victory for: " + sign)
        return False
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == sign:
        print("Victory for: " + sign)
        return False
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == sign:
        print("Victory for: " + sign)
        return False
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == sign:
        print("Victory for: " + sign)
        return False
        
    index_counter = 1
    played_space = 1
    for rows in board:
        for cell in rows:
            if cell == 'O' or cell == 'X':
                played_space += 1
            index_counter += 1
    
    if index_counter == played_space:
        print("It's a tie")
        return False
        
    

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    print("Computer moving")
    calculate_move('X')
    print("Computer done")
    
    
def calculate_move(sign):
    while True:
        try:
            valid_move = repeated_move = False
            if sign == 'O':
                user_input = int(input("Enter your move: "))
            elif sign == 'X':
                user_input = randrange(1, 10)

                print("input:", user_input)

            if user_input > 0 and user_input < 10:
                
                index_counter = 1
                for rows in board:
                    if repeated_move or valid_move:
                        break
                    
                    row_index = 0
                    for cell in rows:
                        if cell == index_counter and cell != user_input:
                            index_counter += 1
                            row_index += 1
                        elif cell == index_counter and cell == user_input:
                            rows[row_index] = sign
                            valid_move = True
                            break
                        elif cell != index_counter and index_counter == user_input:
                            print("Cell already taken, take another option.")
                            repeated_move = True
                            break
                        else:
                            index_counter += 1
                            row_index += 1
                if valid_move:
                    break
            else:
                print("Input should be between 1 and 9")
        except ValueError:
            print("Invalid user_input, user_input must be an integer between 1 and 9!")


board = [[ "" for i in range(3) ] for j in range(3) ]

board[0] = [1, 2, 3]
board[1] = [4, "X", 6]
board[2] = [7, 8, 9]

competing_flag = True

display_board(board)

while True:
    
    make_list_of_free_fields(board)
    enter_move(board)
    display_board(board)
    competing_flag = victory_for(board, 'O')
    if competing_flag == False:
        break
    draw_move(board)
    display_board(board)
    competing_flag = victory_for(board, 'X')
    if competing_flag == False:
        break
