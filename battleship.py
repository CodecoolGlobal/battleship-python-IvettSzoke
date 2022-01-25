# placement phase
from colorama import Fore
import re
from tkinter import *

def ask_board_size():
    is_board_size_valid = False
    while not is_board_size_valid:
        board_size = int(input(Fore.WHITE +"Please choose the board size between (5-10)!\n"))
        if board_size <= 10 and board_size >= 5:
            is_board_size_valid = True
        else:
            print(Fore.RED +"\nInvalid input! (must be between 5-10)")
    return board_size

def init_board(grid):
    row = ['0']*grid
    board = []
    for i in range(grid) :
        board.append(row.copy())
    return board

def print_board(board): 
    for row in board:
        print(" ".join(row))
        

def ask_user_input_for_ship_placement(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_condition_letter_true = False
    while not is_condition_letter_true:
        coordinate_letter = input(f"\nPlease specify the letter from the coordinate ((A-{max_letter.upper()})")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", coordinate_letter):
            is_condition_letter_true = True
    
    is_condition_number_true = False
    while not is_condition_number_true:
        coordinate_number = input(f"\nPlease specify the column of the starting coordinate (1-{grid})")
        try:
            coordinate_number = int(coordinate_number)
            if coordinate_number <= grid and coordinate_number > 0:
                is_condition_number_true = True
        except:
            print(f"Please provide a number between 1 and {grid}!")
    
    is_condition_direction_true = False
    while not is_condition_direction_true:
        direction = input("\nPlease give me the direction! (horizontal - 'h' or vertical - 'v') ")
        try:
            direction = direction.lower()
            if direction == 'h' or direction == 'v':
                is_condition_direction_true = True
        except:
            'The direction has to be specified with the letters "h" or "v"!'

    return coordinate_letter, coordinate_number, direction


# def is_input_valid():
#     # error msg when too close
#     # error msg when out of range (nem lehet 3 hosszu, G5 sem valid input)
#     # error wrong input (a-a)
#     # error msg for occupied coordinates
#     # call the input function
#     # Nóra
    
def available_ships_at_start(board_size):
    ship_config = {
        5 : [1,2,2,3,3,3],
        6 : [1,2,2,2,3,3,4],
        7 : [1,1,1,2,3,3,3,4],
        8 : [1,1,1,1,2,2,3,3,3,4],
        9 : [1,1,1,1,2,2,2,3,3,3,4,5],
        10: [1,1,1,1,1,2,2,2,2,3,3,3,4,4,5]
    }
    return ship_config[board_size]

# # 10x10: (1x5, 2x4, 3x3, 4x2, 5x1)
# #   9x9: (1x5, 1x4, 3x3, 3x2, 4x1)
# #   8x8: (1x4, 3x3, 2x2, 4x1)
# #   7x7: (1x4, 3x3, 1x2, 3x1)
# #   6x6: (1x4, 2x3, 3x2, 1x1)
# #   5x5: (3x3, 1x2, 1x1)

def place_ships_player_0(board):
    player=0
    board_size = len(board[0])
    ships= available_ships_at_start(board_size)
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print ('Available ships to place:', ships)
    for ship in ships:
        row_letter, col_number, direction = ask_user_input_for_ship_placement(board_size)
        #validation

        row_index = rows.index(row_letter.upper())
        col_index = int(col_number) - 1
        board[row_index][col_index] = "X"
        print_board(board)

# def place_ships_player_1(board):
#     player=1
#     board_size = len(board[0])
#     ships= available_ships_at_start(board_size)
#     rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     print ('Available ships to place:', ships)
#     for ship in ships:
#         row_letter, col_number, direction = ask_user_input_for_ship_placement(board_size)
#         #validation

#         row_index = rows.index(row_letter)
#         col_index = int(col_number) - 1
        
#         board[row_index][col_index] = "X"
#         print(board)

def display_waiting_screen():
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title("Battleship - Next player's placement phase.")

    button = Button(tkWindow, text = 'Ready', command = lambda:[is_button_pressed(), quit()])
    button.pack()  

    tkWindow.mainloop()

def quit(tkWindow):
    tkWindow.root.destroy()

    # exit after button was pressed
    # deal with X
    
# def is_button_pressed():
#     # handle a character for starting - name a BUTTON
#     # True, False
#     # Derien

# is_button_pressed()

def ready_board(occupied_coordinates, placement_area):
    if occupied_coordinates == placement_area:
        return True
    else:
        False

ready_board(occupied_coordinates, placement_area)

# shooting phase

def ask_shooting_input(grid):
    letters = "abcdefghijklmnopqrstuvvwxyz"
    max_letter = letters[grid-1]

    is_shooting_letter_true = False
    while not is_shooting_letter_true:
        shooting_letter = input(f"\nPlease specify the letter from the coordinate ((A-{max_letter.upper()})")
        if re.match(f"[a-{letters[grid-1]}A-{letters[grid-1].upper()}]", shooting_letter):
            is_shooting_letter_true = True
    
    is_shooting_number_true = False
    while not is_shooting_number_true:
        coordinate_number = input(f"\nPlease specify the column of the shooting coordinate (1-{grid})")
        try:
            shooting_number = int(coordinate_number)
            if coordinate_number <= grid and shooting_number > 0:
                is_shooting_number_true = True
        except:
            print(f"Please provide a number between 1 and {grid}!")
    
    return shooting_letter, shooting_number

def show_player_one_board():

def show_player_two_board():

    
def is_shooting_input_valid(guessed_pos):
    print(guessed_pos)
    
 8
def has_won(guessed_pos, n):
    won = False
    num_of_x_list = []

    while not won:
  
        # current_player_index = 0 if current_player_index == 1 else 1
    for sub_list in board: 
        num_of_x_list.append(sub_list.count('X'))
    num_of_x = sum(num_of_x_list)
    y = 0

    for sub_list in board:              #bordban a kis listák
        num_of_x = num_of_x + sub_list.count('X')       
    if num_of_x == 0:

    print(f"Player {n} wins!")

    return(won)
   
ask_shooting_input()


    num_of_h = 0   
def the_game():
    grid = ask_board_size()
    board = init_board(grid)
    print_board(board)
    place_ships_player_0(board)
    occupied_coordinates = 0
    placement_area = sum(list(ship_config[board_size].values()))
if __name__ == "__main__":
    the_game()
