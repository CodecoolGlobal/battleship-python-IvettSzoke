# placement phase

import re
from tkinter import *

occupied_coordinates = 0
placement_area = 10

def ask_board_size():
    is_board_size_valid = False
    while not is_board_size_valid:
        board_size = input("Please choose the board size between (5-10)!\n")
        try:
            board_size = int(board_size)
            if board_size <= 10 or board_size >= 5:
                is_board_size_valid = True
        except:
            print("\nInvalid input! (must be between 5-10)")
    return board_size

def init_board(grid):
    board = [['0']*grid]*grid
    return board

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


def is_input_valid():
    # error msg when too close
    # error msg when out of range (nem lehet 3 hosszu, G5 sem valid input)
    # error wrong input (a-a)
    # error msg for occupied coordinates
    # call the input function
    # Nóra
    
def available_ships_at_start(board_size):
    ship_config = {
        5 : [1,1,2],
        6 : [1,1,2,2]
    }
    return ship_config[board_size]

def place_ships(boards):
    player=0
    board_size = len(boards[0])
    ships= available_ships_at_start(board_size)
    print ('Available ships to place:', ships)
    # for ship in ships
        # add coordinate
        # validate
        # ship mark on the player1 board 
    
    player=1
    # info about number of ships
    # for ship in ships
        # add coordinate
        # validate
        # ship mark on the player2 board 
    

def display_waiting_screen():
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title("Battleship - Next player's placement phase.")

    def print_this():
        return print('This will be the next function rolling.')

    button = Button(tkWindow,
        text = 'Ready', command = print_this)  
    button.pack()  
    
    tkWindow.mainloop()
    # exit after button was pressed
    # deal with X

display_waiting_screen()
    
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

def ask_shooting_input():
    # 2 for the coordinates
    # Eszter

def show_player_one_board():

def show_player_two_board():

def has_won():
    won = True
    # if S betu annyi mint a hajoink akkor nyert
    # Eszter

 def ask_shooting_input():
    guess_row = input('Give me a row!')
    guess_col = input('Give me a col!')
    guessed_pos = guess_row + guess_col
    is_input_valid(guessed_pos)
    for sub_list in board:                      #bordban a kis listák
        num_of_x = num_of_x + sub_list.count('X')  
        y = 0     
    while num_of_x > y:                                     # y = ahány x van
        guess_row = input('Give me a row!')
        guess_col = input('Give me a col!')
    if guess_row == ship_row and guess_col == ship_col:
        y +=1
        print("You've hit a ship!")
    elif(board[guess_row][guess_col] == "X"):
        print('You guessed that one already.')
    else:
        print("You've missed!") 
        board[guess_row][guess_col] = "X"

    
def is_input_valid(guessed_pos):
    print(guessed_pos)
    

def has_won(guessed_pos, n):
    for sub_list in board:              #bordban a kis listák
        num_of_x = num_of_x + sub_list.count('X')       
    if num_of_x == 0:
        won = True
    print(f"Player {n} wins!")

    return(won)
   
ask_shooting_input()


    # num_of_h = 0   
def the_game():
    grid = ask_board_size()
    board = init_board(grid)
    # print(board)
    ask_user_input_for_ship_placement(grid)
if __name__ == "__main__":
