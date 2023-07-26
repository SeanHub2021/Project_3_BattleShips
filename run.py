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

# Global variable to define the board itself, 
def print_board():
    print ('  A B C D E F G H I J K L M N O') #15 by 15, so 15 letters = A-O, with a blank at the start for row
    print ('-------------------------------') #top line of the board to seperate letters
    board = [['~']*15 for _ in range(15)] #create the board with ~ wave symbol to represent water
    
    row_number = 1 #first row = 1
    for row in board: 
        print(row_number, end=' ')

        if row_number < 10:
            print(end='  ') #for single digit rows, an extra space is needed to align correctly

        for column in row: #each cell in the row
            print(column, end=' ') #print, but dont move onto the next row

        print() #move to next row

        row_number += 1 #increase the row number by 1
    
    print_board() #print the board
