# placement phase
from colorama import Fore
import re
from tkinter import *
import window

def ask_board_size():
    is_board_size_valid = False
    while not is_board_size_valid:
        try:
            board_size = int(input(Fore.WHITE +"Please choose the board size between (5-10)!\n"))
            if board_size <= 10 and board_size >= 5:
                is_board_size_valid = True
        except:
            print(Fore.RED +"\nInvalid input! (must be between 5-10)")
    return board_size


# def init_board(grid):
#     board = [['0']*grid] * grid
#     return board


def init_board(grid):
    row = ['0']*grid
    board = []
    for i in range(grid):
        board.append(row.copy())
    return board

def print_board(board): 
    board_size = len(board[0])
    print(" ", end=' ')
    for i in range(1,board_size+1):
        print (str(i), end =" ")
    print()
    # print (' '.join([str(i) for i in range(1,board_size+1)]))
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for index, row in enumerate(board):
        print(f'{rows[index]} {" ".join(row)}')
        

def ask_user_input_for_ship_placement(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_condition_letter_true = False
    while not is_condition_letter_true:
        coordinate_letter = input(Fore.YELLOW + f"\nPlease specify the letter from the coordinate ((A-{max_letter.upper()})")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", coordinate_letter):
            is_condition_letter_true = True
    
    is_condition_number_true = False
    while not is_condition_number_true:
        coordinate_number = input(Fore.WHITE + f"\nPlease specify the column of the starting coordinate (1-{grid})")
        try:
            coordinate_number = int(coordinate_number)
            if coordinate_number <= grid and coordinate_number > 0:
                is_condition_number_true = True
        except:
            print(Fore.RED + f"Please provide a number between 1 and {grid}!")
    
    is_condition_direction_true = False
    while not is_condition_direction_true:
        direction = input(Fore.WHITE + "\nPlease give me the direction! (horizontal - 'h' or vertical - 'v')\n")
        try:
            direction = direction.lower()
            if direction == 'h' or direction == 'v':
                is_condition_direction_true = True
        except:
            print(Fore.RED + 'The direction has to be specified with the letters "h" or "v"!')

    return coordinate_letter, coordinate_number, direction

# def is_input_valid():
#     # error msg when too close
#     # error msg when out of range (nem lehet 3 hosszu, G5 sem valid input)
#     # error wrong input (a-a)
#     # error msg for occupied coordinates
#     # call the input function
#     # Nora
    
def available_ships_at_start(board_size):
    ship_config = {
        5 : [1,2,3,3],
        6 : [1,2,3,3,4],
        7 : [1,2,2,3,3,4],
        8 : [1,1,2,2,3,3,4],
        9 : [1,1,2,2,2,3,3,4],
        10: [1,1,1,1,2,2,2,3,3,4]
    }
    return ship_config[board_size]

# 10x10 (20): (1x4, 2x3, 3x2, 4x1)
#   9x9 (18): (1x4, 2x3, 3x2, 2x1)
#   8x8 (16): (1x4, 2x3, 2x2, 2x1)
#   7x7 (15): (1x4, 2x3, 2x2, 1x1)
#   6x6 (13): (1x4, 2x3, 1x2, 1x1)
#   5x5 (11): (2x3, 1x2, 1x1)


# def place_ships_player_0(board):
#     player=0
#     board_size = len(board[0])
#     ships= available_ships_at_start(board_size)
#     rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     print ('Available ships to place:', ships)
#     for ship in ships:
#         row_letter, col_number, direction = ask_user_input_for_ship_placement(board_size)
#         #validation

#         row_index = rows.index(row_letter.upper())
#         col_index = int(col_number) - 1
#         board[row_index][col_index] = "X"
#         print_board(board)

def place_ships(board):
    board_size = len(board[0])
    ships= available_ships_at_start(board_size)
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print ('Available ships to place:', ships)
    for ship in ships:
        row_letter, col_number, direction = ask_user_input_for_ship_placement(board_size)
        #validation
        
        row_index = rows.index(row_letter.upper())
        col_index = int(col_number) - 1

        mark_ship(board, ship, direction, row_index, col_index)
        print_board(board)

def mark_ship(board, ship, direction, row_index, col_index):
    for i in range(ship):
        board[row_index][col_index] = 'X'
        if direction == 'h':
            col_index+=1
        else:
            row_index+=1

def ready_board(occupied_coordinates, placement_area):
    if occupied_coordinates == placement_area:
        return True
    else:
        False

# shooting phase

def ask_shooting_input(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_shooting_letter_true = False
    while not is_shooting_letter_true:
        shooting_letter = input(Fore.YELLOW + f"\nPlease specify the letter from the coordinate ((A-{max_letter.upper()})")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", shooting_letter):
            is_shooting_letter_true = True
    
    is_shooting_number_true = False
    while not is_shooting_number_true:
        coordinate_number = input(Fore.WHITE + f"\nPlease specify the column of the shooting coordinate (1-{grid})")
        try:
            shooting_number = int(coordinate_number)
            if shooting_number <= grid and shooting_number > 0:
                is_shooting_number_true = True
        except:
            print(Fore.RED + f"Please provide a number between 1 and {grid}!")
    
    return shooting_letter, shooting_number


def show_player_1_board():
    pass

def show_player_2_board():
    pass
    
def is_shooting_input_valid(guessed_pos):
    print(guessed_pos)

# board = [[ '0','0','X','X','0' ],[ '0','0','0','0','0' ],[ '0','0','X','0','0' ],[ '0','0','0','0','0' ],[ '0','0','0','0','0' ]]

def has_won(board, guessed_row, guessed_col,n):
    # won = False
    # num_of_x_list = []

    # while not won:
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    num_of_x = 0
    for sub_list in board:        
        num_of_x = num_of_x + sub_list.count('X')
    if num_of_x == 0:
        print(f"Player {n} wins!")
    row_i = rows.index(guessed_row)
    col_i = (int(guessed_col) - 1)
    if board[row_i][col_i] == '0':
        board[row_i][col_i] = 'M'
        print("You've missed!") 
    if board[row_i][col_i] in ['M', 'S', 'H']:
        print('You guessed that one already.')
    if board[row_i][col_i] == 'X':
        print("You've hit a ship!")


    return won
   
# ask_shooting_input()


def the_game():
    print(Fore.RED + "\nWelcome Players! This is the famous battleship! game!\n")
    grid = ask_board_size()
    board = init_board(grid)
    print_board(board)
    place_ships(board)

    exec(open('window.py').read())
    
    print(Fore.RED + "\nNext player's placement phase\n")
    place_ships(board)
    # ship_board_player_2 = place_ships(grid)


    # initialize the covered boards
    # covered_board_player_1 = 0
    # covered_board_player_2 = 0

    # # define number of turns. grid * grid ensures that some of the players will win
    # turns = grid * grid
    # turns = [1, 2] * turns
    # for turn in turns:
    #     if turn ==  1:
    #         pass
    #         # should show player 1 ship board: showing the other player's shoots
    #         # and player 2 covered board: showing the player ones shoots

    #         # 1 ask for user input - the coordinate where player one wants to shoot
    #         # 2 update player 2 covered board, 
    #         # 3 update player 2 ship board: so player 2 will be able to see the other players shoots
    #         # 4 give feedback if it is a match or not

    #         # 4.1 at the same time check if player one has won, and proceed accordingly
    #         if has_won(ship_board_player_2):
    #             # inform players that somebody won the game and quit
    #             break

    #     if turn == 2:
    #         pass
    #         # should show player 2 ship board: showing the other player's shoots
    #         # and player 1 covered board: showing only the player's shoots+

    #         # 1 ask for user input - the coordinate where player two wants to shoot
    #         # 2 update player 1 covered board
    #         # 3 update player 1 ship board
    #         # 4 give feedback if it is a match or not

    #         # 4.1 at the same time check if player two has won, and proceed accordingly
    #         if has_won(ship_board_player_1):
    #             # inform players that somebody won the game and quit
    #             break


if __name__ == "__main__":
    the_game()


# ask players for placing ships
    # place ships function should be able to modify a board only independently from its owner. No need for player specific place ship function.
    # the function should be able to handle the available ships argument and ask for user input until there is any available ship
    # and it should ask for an additional user input (on top of coordinates and direction), which is the size
    # finally it should place it in line with the game description (should not cover each other, should not be next to each other, ...)