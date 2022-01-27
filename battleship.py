from colorama import Fore
import re
import tkinter as tk
from tkinter import *
import time

#################### placement phase
def ask_board_size():
    is_board_size_valid = False
    while not is_board_size_valid:
        try:
            board_size = int(input(Fore.WHITE +"Please choose the board size between (5-10)!\n"))
            if board_size <= 10 and board_size >= 5:
                is_board_size_valid = True
        except:
            print(Fore.RED +"\nInvalid input! (must be between 5-10)\n")
    return board_size

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
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for index, row in enumerate(board):
        print(f'{rows[index]} {" ".join(row)}')

def print_boards_during_game(b1, b2):
    size = len(b1)
    row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'][:size]
    col_numbers = list(range(size))
    for i in range(size):
        col_numbers[i] = str(col_numbers[i]+1)

    print("Player" + " "*(size*2) + "Enemy")
    print("  ", " ".join(col_numbers), "    ", " ".join(col_numbers))
    for i in range(size):
        print(str(row_letters[i]), ""," ".join(b1[i]), "  ", str(row_letters[i]), " ".join(b2[i]))
        
def ask_user_input_for_ship_placement(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_condition_letter_true = False
    while not is_condition_letter_true:
        coordinate_letter = input(Fore.YELLOW + f"\nPlease specify the letter from the coordinate (A-{max_letter.upper()}) ")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", coordinate_letter):
            is_condition_letter_true = True
    
    is_condition_number_true = False
    while not is_condition_number_true:
        coordinate_number = input(Fore.WHITE + f"\nPlease specify the column of the starting coordinate (1-{grid}) \n")
        try:
            coordinate_number = int(coordinate_number)
            if coordinate_number <= grid and coordinate_number > 0:
                is_condition_number_true = True
        except:
            print(Fore.RED + f"Please provide a number between 1 and {grid}! ")
    
    is_condition_direction_true = False
    while not is_condition_direction_true:
        direction = input(Fore.WHITE + "\nPlease give me the direction! (horizontal - 'h' or vertical - 'v') \n")
        try:
            direction = direction.lower()
            if direction == 'h' or direction == 'v':
                is_condition_direction_true = True
        except:
            print(Fore.RED + '\nThe direction has to be specified with the letters "h" or "v"!\n')

    return coordinate_letter, coordinate_number, direction
    
def available_ships_at_start(board_size):
    ship_config = {
        5 : [1,2],
        6 : [1,2,3],
        7 : [1,2,2,3],
        8 : [1,1,2,2,3],
        9 : [1,1,2,3,4],
        10: [1,1,2,3,3,4]
    }
    return ship_config[board_size]

def place_ships(board):
    board_size = len(board[0])
    ships = available_ships_at_start(board_size)
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print('Available ships to place:', ships)
    all_ship_coordinates = []
    for ship in ships:
        while True:
            row_letter, col_number, direction = ask_user_input_for_ship_placement(
                board_size)
            row_index = rows.index(row_letter.upper())
            col_index = int(col_number) - 1

            if not is_in_range(board_size, ship, direction, row_index, col_index):
                print(Fore.RED + "\nSorry, that's out of range.\n")
                continue
            elif not is_free(board, ship, direction, row_index, col_index):
                print(Fore.RED + "\nIt's occupied!\n")
                continue
            elif not is_on_right_place(board, board_size, ship, direction, row_index, col_index):
                print(Fore.RED + "\nShips are too close!\n")
                continue
            else:
                break
        all_ship_coordinates.append(collect_ship_coordinates(ship, direction, row_index, col_index))
        mark_ship(board, ship, direction, row_index, col_index)
        print_board(board)
    print(all_ship_coordinates)
    return board

def is_on_right_place(board, board_size, ship, direction, row_index, col_index):
    for i in range(ship):
        if (0 <col_index+1 < board_size) and (board[row_index][col_index + 1] == 'X'):
            return False
        elif (0 <= col_index-1 < board_size) and board[row_index][col_index-1] == 'X':
            return False
        elif (0 < row_index + 1 < board_size) and board[row_index + 1][col_index] == 'X':
            return False
        elif (0 <= row_index - 1 < board_size) and board[row_index-1][col_index] == 'X':
            return False
    return True

def is_free(board, ship, direction, row_index, col_index):
    for i in range(ship):
        if board[row_index][col_index] == 'X':
            return False
        if direction == 'h':
            col_index+=1
        else:
            row_index+=1
    return True

def is_in_range(board_size, ship, direction, row_index, col_index):
    for i in range(ship):
        if (row_index > board_size-1):
            return False
        elif(col_index > board_size-1):
            return False
        if direction == 'h':
            col_index+=1
        else:
            row_index+=1
    return True   

def collect_ship_coordinates(ship, direction, row_index, col_index):
    coordinates = []
    for i in range(ship):
        coordinates.append((row_index, col_index))
        if direction == 'h':
            col_index += 1
        else:
            row_index += 1
    return coordinates

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

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Battleship")
        self.root.geometry('400x100')
        label = Label(self.root, text = "\nNext player's placement phase\n").pack()
        button = tk.Button(self.root, 
                          text = 'Next', 
                          command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

########################### shooting phase

def ask_shooting_input(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_shooting_letter_true = False
    while not is_shooting_letter_true:
        shooting_letter = input(Fore.YELLOW + f"\nPlease specify the letter from the coordinate (A-{max_letter.upper()}) ")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", shooting_letter):
            is_shooting_letter_true = True
    
    is_shooting_number_true = False
    while not is_shooting_number_true:
        coordinate_number = input(Fore.WHITE + f"\nPlease specify the column of the shooting coordinate (1-{grid}) ")
        try:
            shooting_number = int(coordinate_number)
            if shooting_number <= grid and shooting_number > 0:
                is_shooting_number_true = True
        except:
            print(Fore.RED + f"Please provide a number between 1 and {grid}! ")
    
    return shooting_letter, shooting_number

    
def is_shooting_input_valid(guessed_pos):
    print(guessed_pos)

def has_won(ships, shooting_board):
    for ship in ships:
        for coordinate in ship:
            row, col = coordinate
            if shooting_board[row][col] != 'S':
                return False
    return True

# def has_won_old(board, guessed_row, guessed_col,n):
#     # won = False
#     # while not won:
    
#     rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     num_of_x = 0
#     num_of_s = 0
#     for sub_list in board:        
#         num_of_x += sub_list.count('X')
#         num_of_s = num_of_s + sub_list.count('S')
#     if num_of_x == 0:
#         print(f"Player {n} wins!")
#     row_i = rows.index(guessed_row)
#     col_i = (int(guessed_col) - 1)
#     if board[row_i][col_i] == '0':
#         board[row_i][col_i] = 'M'
#         print(Fore.RED + "\nYou've missed!\n") 
#     if board[row_i][col_i] in ['M', 'S', 'H']:
#         print(Fore.RED + "\nYou guessed that one already.\n")
#     if board[row_i][col_i] == 'X':
#         print(Fore.GREEN + "\nYou've hit a ship!\n")
#     if board[row_i][col_i+1] == '0'and board[row_i+1][col_i] == '0' and board[row_i-1][col_i] == '0' and board[row_i][col_i-1] == '0':
#         board[row_i][col_i] == "S"
#         print("You've sunk a ship!")
#     # if board[row_i][col_i+1] == '0' and board[row_i-1][col_i] == '0' and board[row_i][col_i-1] == '0' and 
#     # return won

def edit_boards_during_game(covered_board, ship_board, shot):
    """
    covered board:  the board which records the players shots (undisc, miss, hit, sunk)
    ship board:     the board which stores the enemies ships
    shot:           list of 2: [row, column], coordinates of the actual shot

    The signs can be edited in the next 4 rows
    """
    ship_sign = 'X'
    missed = 'M'
    hit = 'H'
    sunk = 'S'
    row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    row, column = row_letters.index(shot[0].upper()), shot[1] - 1

    # place missed shots if:
    if ship_board[row][column] != ship_sign:
        ship_board[row][column] = missed
        covered_board[row][column] = missed
        print("\nYou've missed!\n")

    # place hits if:
    if ship_board[row][column] == ship_sign:
        ship_board[row][column] = hit
        covered_board[row][column] = hit
        print("\nYou've hit a ship!\n")

        

    # overwrite hits to sunk if:
    # That could be a separate function
    return covered_board, ship_board

def the_game():
    print(Fore.RED + "\nWelcome Players! This is the famous BATTLESHIP game!\n")
    grid = ask_board_size()
    board_1 = init_board(grid)
    print_board(board_1)
    board_1 = place_ships(board_1)
    time.sleep(2.4)
    app = Window()
    time.sleep(2.4)
    print(Fore.RED + "\nNext player's placement phase:\n")
    print(Fore.WHITE)
    board_2 = init_board(grid)
    board_2 = place_ships(board_2)
    print(Fore.GREEN + "\nShips are placed. Let's play!\n")
    print(Fore.GREEN + "Let's begin the shooting phase!\n")
    print(Fore.WHITE)

    covered_board_player_1 = init_board(grid)
    covered_board_player_2 = init_board(grid)

    turns = grid * grid
    turns = [1, 2] * turns
    for turn in turns:
        if turn ==  1:
            print("\n\nPlayer 1 turn")
            shot = ask_shooting_input(grid)
            covered_board_player_1, board_2 = edit_boards_during_game(covered_board_player_1, board_2, shot)
            print_boards_during_game(covered_board_player_1, board_2)

    #         # 2 update player 2 covered board, 
    #         # 3 update player 2 ship board: so player 2 will be able to see the other players shoots
    #         # 4 give feedback if it is a match or not

            # if has_won(board_2):
            #     # need to check the appropiate ship board
            #     # if there is no more x on the board then we have a winner
            #     print("Player 1 wins!")

        if turn == 2:
            print("\n\nPlayer 2 turn")
            shot = ask_shooting_input(grid)
            covered_board_player_2, board_1 = edit_boards_during_game(covered_board_player_2, board_1, shot)

            print_boards_during_game(covered_board_player_2, board_1)
    #         # should show player 2 ship board: showing the other player's shoots
    #         # and player 1 covered board: showing only the player's shoots+

    #         # 1 ask for user input - the coordinate where player two wants to shoot
    #         # 2 update player 1 covered board
    #         # 3 update player 1 ship board
    #         # 4 give feedback if it is a match or not

            # if has_won(board_1):
            #     print("Player 2 wins!")

if __name__ == "__main__":
    the_game()
