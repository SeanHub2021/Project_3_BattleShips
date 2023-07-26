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
player_board = [['~']*10 for _ in range(10)] #create the players board, 15 wide with ~ for water
computer_board = [['~']*10 for _ in range(10)] #create the computer board, 15 wide with ~ for water

#Print the boards for testing
print_board("PLAYER BOARD", player_board)
print_board("COMPUTER BOARD", computer_board)



