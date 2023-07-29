# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" 
 Battleships game

    The ability for the user to set the grid size
    Warn the user if their guess is off-grid

Must show: Programming constructs; repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)

1. Implement a given algorithm as a computer program 
2. Adapt and combine algorithms to solve a given problem
3. Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.) 
4. Explain what a given program does 
5. Identify and repair coding errors in a program 
6. Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software 
7. Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain. 
8. Demonstrate and document the development process through a version control system such as GitHub 
9. Deploy a command-line application


V1; 
- A 15x15 grid; "~" for water. "#" for ship part. "X" for hit ship part. "o" for water that has been shot.
- 5 ships; length 2, length 3, length 4 length 5. 
- Randomise opponent placement
- Randomise opponent guess
- place ships only vertically or horizontally
- Input for user to choose grid reference to 'shoot'
- Score (ships remaining)

"""
import random #load python module 'ramdom'

### GAME MENU SCREEN SECTION ###
def print_game_menu(): #creates a menu 'screen' before the board is printed. Placeholder for inputs to add later.
    print("Welcome to BATTLESHIPS!")
    print("Submit Y in the terminal to proceed to the game.")

def menu_input():
    user_input = input("Enter your selection: ") #prompts user to input their selection, as per the menu print instructions
    if user_input.lower() == 'y': #converts user input to lower case, checks for match
        return True
    else:
        return False

while True: #While statement that checks if the menu input returns True, and if it does, breaks the menu loop, proceeds to the board
    print_game_menu()
    if menu_input():
        break 

### CREATE THE BOARD ###
# Global variable to define the board itself. Now displaying two boards.  
def print_board(board_title, game_board):
    print(board_title)
    print ('   A B C D E F G H I J') #10 by 10, so 10 letters = A-J, with a blank at the start for row
    print ('-----------------------') #top line of the board to seperate letters
    board = [['~']*10 for _ in range(10)] #create the board with ~ wave symbol to represent water
    
    row_number = 1 #first row = 1
    for row in game_board: 
        print(row_number, end=' ')

        if row_number < 10:
            print(end=' ') #for single digit rows, an extra space is needed to align correctly

        for column in row: #each cell in the row
            print(column, end=' ') #print, but dont move onto the next row

        print() #move to next row

        row_number += 1 #increase the row number by 1
    print()

#Create two board names
player_board = [['~']*10 for _ in range(10)] #create the players board, 10 wide with ~ for water
computer_board_hidden = [['~']*10 for _ in range(10)] #create the hidden computer board, 10 wide with ~ for water
computer_board_display = [['~']*10 for _ in range(10)] #the players view of the computers board

#Print the boards for testing
print_board("PLAYER BOARD", player_board)
print_board("COMPUTER BOARD", computer_board_display)

### PLACE BATTLESHIPS SECTION ###
#player ship placement
def place_player_ships(board, ship_count):
    for i in range(ship_count): #do this for as many ships are set to be placed
        while True: #loop until a proper board position is entered, so no positions off the board
            print("Place ship number", i+1)

            ship_position = input("Enter a ship position (For example: C5) and press Enter: ") # prompt user to input a ship position

            #bug/feature for later - need to rethink this validation if i add a user option to change board size
            #Input Validation: check users input is a letter, then a digit, and the digit is between 1-10
            if not ship_position[0].isalpha() or not ship_position[1:].isdigit() or not 1 <= int(ship_position[1:]) <=10:
                print("Oh no! Thats not quite right! Try to type it again, just a letter and number, like c5: ")
                continue

            # to get the column of the board, convert letter to uppercase, ord function converts the unicode letter value to unicode integer
            column = ord(ship_position[0].upper()) - ord('A') 

            #to get the row of the board, we take the int (integer) from user input, and subtract 1 (we count from 0)
            row = int(ship_position[1:]) - 1

            #change the cell in the player board to represent the placed ship using an "O" 
            board[row][column] = 'O'

            print("Column:", column, "Row:", row) #print to test these functions are working as intended
            print_board("PLAYER BOARD", board) #print the updated player board with the ship placement
            break

place_player_ships(player_board, 3) #place 3 ships on the player board
print_board("PLAYER BOARD", player_board)

#computer ship placement
def place_computer_ships(board, ship_count):
    for _ in range(ship_count):
        while True:
            row = random.randint(0, len(board) -1) #check the 2d list of the board for the 'length' of rows in the board, generate a random integer within it
            column = random.randint(0, len(board[0]) -1) #check the first row of the board to count the number of columns, and generate a random integer

            if board[row][column] == '~': #check if the random board location is ~ (no ship placement)
                board[row][column] = '0' #if it is ~, change it to 0 to 'place' the ship
                print("Computer has placed: ", row+1, chr(column + ord('A'))) #convert the column integer/letter
            break

place_computer_ships(computer_board_hidden, 3) #place 3 computer ships
print_board("COMPUTER BOARD (hidden)", computer_board_hidden)

### GAME FUNCTIONS SECTION ###
# Players Shot
def player_shoot(board_hidden, board_display):
    while True:
        shot_position = input("Your turn to fire at the enemy! Please enter a column and row (for example; C1): ") #prompt user for their move

        #Input Validation: check users input is a letter, then a digit, and the digit is between 1-26
            if not ship_position[0].isalpha() or not ship_position[1:].isdigit() or not 1 <= int(ship_position[1:]) <=10:
                print("Oh no! Thats not quite right! Try to type it again, just a letter and number, like c5: ")
                continue

