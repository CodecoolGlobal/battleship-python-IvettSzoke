from colorama import Fore
import re
import tkinter as tk
from tkinter import *
import time

PLAYER_1_COORDINATES=[]
PLAYER_2_COORDINATES=[]
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

def place_ships(board, turn):
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
        if turn==1:
            PLAYER_1_COORDINATES.append(collect_ship_coordinates(ship, direction, row_index, col_index))
            # # print(PLAYER_1_COORDINATES)
        elif turn==2:
            PLAYER_2_COORDINATES.append(collect_ship_coordinates(ship, direction, row_index, col_index))
            # # print(PLAYER_2_COORDINATES)
        mark_ship(board, ship, direction, row_index, col_index)
        print_board(board)
  
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


def edit_boards_during_game(covered_board, ship_board, shot, turn):

    ship_sign = 'X'
    missed = Fore.RED + 'M' + Fore.WHITE
    hit = Fore.GREEN + 'H' + Fore.WHITE
    sunk = Fore.BLUE + 'S' + Fore.WHITE
    row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    row, column = row_letters.index(shot[0].upper()), shot[1] - 1

    # place missed shots if:
    if ship_board[row][column] != ship_sign:
        ship_board[row][column] = missed
        covered_board[row][column] = missed
        print("\nYou've missed!\n")

    if turn == 1:
        coordinates = PLAYER_2_COORDINATES
    elif turn == 2:
        coordinates = PLAYER_1_COORDINATES
    # shoot = ask_shooting_input(len(ship_board))

    shoot = (row, column)

    # place hits if:
    if ship_board[row][column] == ship_sign:
        ship_board[row][column] = hit
        covered_board[row][column] = hit
        print("\nYou've hit a ship!\n")

        #find coordinates of the ship that had just been hit
        shot_ship_coordinate_list = []
        for ship in coordinates:
            for coo in ship:
                if coo[0] == row and coo[1] == column:
                    shot_ship_coordinate_list = ship
                    break
        #check if the ship coordinates are all hit
        is_sunk = True
        for coo in shot_ship_coordinate_list:
            if ship_board[coo[0]][coo[1]] != hit:
                is_sunk = False
        
        #if sunk, mark all coordinates of the ship with S
        if is_sunk:
            for coo in shot_ship_coordinate_list:
                ship_board[coo[0]][coo[1]] = sunk

    return covered_board, ship_board

def the_game():
    print(Fore.RED + "\nWelcome Players! This is the famous BATTLESHIP game!\n")
    grid = ask_board_size()
    turn = 1
    board_1 = init_board(grid)
    print_board(board_1)
    board_1 = place_ships(board_1, turn)
    time.sleep(2.4)
    app = Window()
    time.sleep(2.4)
    print(Fore.RED + "\nNext player's placement phase:\n")
    print(Fore.WHITE)
    turn = 2
    board_2 = init_board(grid)
    board_2 = place_ships(board_2, turn)
    print(Fore.GREEN + "\nShips are placed. Let's play!\n")
    print(Fore.GREEN + "Let's begin the shooting phase!\n")
    print(Fore.WHITE)

    covered_board_player_1 = init_board(grid)
    covered_board_player_2 = init_board(grid)
    
    turn = 1
    while True:
        if turn == 1:
            print("\n\nPlayer 1 turn")
            print_boards_during_game(covered_board_player_1, board_1)
            shot = ask_shooting_input(grid)
            covered_board_player_1, board_2 = edit_boards_during_game(covered_board_player_1, board_2, shot, turn)
            turn =  2
            
            if has_won(PLAYER_2_COORDINATES, board_2):
                print(Fore.GREEN + "\nPlayer 1 wins!\n")
                return

        input(f"Player {turn}'s turn. Press any button when ready.")

        if turn == 2:
            print("\n\nPlayer 2 turn")
            print_boards_during_game(covered_board_player_2, board_2)
            shot = ask_shooting_input(grid)
            covered_board_player_2, board_1 = edit_boards_during_game(covered_board_player_2, board_1, shot, turn)
            turn = 1

            if has_won(PLAYER_1_COORDINATES, board_1):
                print(Fore.GREEN + "\nPlayer 2 wins!\n")
                return
        
        input(f"Player {turn}'s turn. Press any button when ready.")

if __name__ == "__main__":
    the_game()
