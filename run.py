import random
import time

player_board = [['~']*10 for _ in range(10)]
computer_board_hidden = [['~']*10 for _ in range(10)]
computer_board_display = [['~']*10 for _ in range(10)]


def print_game_menu():
    """
    GAME MENU SCREEN SECTION
    creates a menu 'screen' before the board is printed.
    """
    print("Welcome to BATTLESHIPS!")
    print("Submit Y in the terminal to proceed to the game.")


def menu_input():
    """
    prompts user to input their selection, as per the menu print instructions
    converts user input to lower case, checks for match
    """
    user_input = input("Enter your selection: ")
    if user_input.lower() == 'y':
        return True
    else:
        return False


def print_board(board_title, game_board):
    """
    define the board itself. Now displaying two boards.
    10 by 10, so 10 letters = A-J, with a blank at the start for row
    print a line of dashes to outline the board
    print ten lines of rows, and fill the board with waves ~
    for single digit rows an extra space is needed to be printed for alignement
    """
    print(board_title)
    print('   A B C D E F G H I J')
    print('-----------------------')

    row_number = 1
    for row in game_board:
        print(row_number, end=' ')
        if row_number < 10:
            print(end=' ')
        for column in row:
            print(column, end=' ')
        print()
        row_number += 1
    print()


def place_player_ships(board, ship_count):
    """
    Player ship placement
    Loop the logic until a proper board position is entered.
    Input validation checks users input is;
    - not blank
    - is first a letter, then a number between 1-10
    - is within the length and height of the board
    Change the cell in the board to an "O" for ship
    to get the column of the board, convert letter to uppercase,
    ord function converts the unicode letter value to unicode integer
    to get the row of the board;
    take the int (integer) from user input, and subtract 1 (we count from 0)
    """
    for i in range(ship_count):
        while True:
            print("Place ship number", i+1)
            ship_position = input("Enter a ship position "
                                  "(EG: C5), press Enter: ")
            if not ship_position:
                print("Oh no! You entered nothing!")
                print("Try to type it again!")
                print("just a letter and number, like c5: ")
                continue
            if (not ship_position[0].isalpha() or
                    not ship_position[1:].isdigit() or
                    not 1 <= int(ship_position[1:]) <= 10):
                print("Oh no! Thats not a letter and number within the board")
                print("Try to type it again!")
                print("just a letter and number, like c5: ")
                continue
            column = ord(ship_position[0].upper()) - ord('A')
            row = int(ship_position[1:]) - 1

            if not (0 <= column < len(board) and 0 <= row < len(board)):
                print("Oh no! Thats outside the board!")
                print("Try to type it again!")
                print("just a letter and number, like c5: ")
                continue
            board[row][column] = 'O'
            print("Column:", column, "Row:", row)
            print_board("PLAYER BOARD", board)
            break


def place_computer_ships(board, ship_count):
    """
    Computers turn at ship placement
    Check the 2d list of the board for the 'length' of rows in the board,
    generate a random integer within it
    Check the first row of the board to count the number of columns, and
    generate a random integer within it
    Check if the random board location is ~ (no ship placement)
    Of it is ~, change it to 0 to 'place' the ship
    #convert the column integer/letter
    """
    for _ in range(ship_count):
        while True:
            row = random.randint(0, len(board) - 1)
            column = random.randint(0, len(board[0]) - 1)
            if board[row][column] == '~':
                board[row][column] = 'O'
                print("Computer has placed: ", row+1, chr(column + ord('A')))
            break


def player_shoot(cpu_board_display, cpu_board_display_hidden):
    """
    # Players Shot
    prompt user for their move
    Input validation checks users input is;
    - not blank
    - is first a letter, then a number between 1-10
    - is within the length and height of the board
    to get the column of the board, convert letter to uppercase.
    ord function converts the unicode letter value to unicode integer
    row of the board, take the int from user input, subtract 1
    Check if the row has already been shot at, if it has then reprompt the user
    Check if shot hits a ship on hidden board, change display board to hit 'X'
    if the shot misses, change the display board wave ~ to M for 'Miss'
    """
    while True:
        shot_position = input("Your turn to fire at the enemy! "
                              "Please enter a col and row (for example; C1): ")

        if not shot_position:
            print("Oh no! you entered nothing!")
            print("Try to type it again, just a letter and number, like c5: ")
            continue

        if (not shot_position[0].isalpha() or
                not shot_position[1:].isdigit() or
                not 1 <= int(shot_position[1:]) <= 10):
            print("Oh no! Thats not a letter and number within the board!")
            print("Type it again, just a letter and number like c5: ")
            continue

        column = ord(shot_position[0].upper()) - ord('A')
        row = int(shot_position[1:]) - 1   
        if not (0 <= column < len(cpu_board_display) or
                not (0 <= row < len(cpu_board_display))):
            print("Oh no! Thats outside of the board!")
            print("Try to type it again, just a letter and number, like c5: ")
            continue
        if cpu_board_display[row][column] in ['M', 'X']:
            print("You've already shot at this position! Try again!")
            continue

        if cpu_board_display_hidden[row][column] == 'O':

            cpu_board_display[row][column] = 'X'
            print("YOU HAVE HIT AN ENEMY BATTLESHIP!")
        else:

            cpu_board_display[row][column] = 'M'
            print("YOU MISSED!")
        break


def computer_shoot(player_board):
    """
    User timer to give computer thinking time
    select random position within the player board table for the computers go
    checks board position has not already been 'guessed'
    #has prints to test code is working, function needs to fix
    #if the computer guess hits a ship
    #or its a miss, change ~ to M on the player board
    """
    print('Computer thinking about their shot...!')
    time.sleep(3)

    while True:
        column = random.randint(0, 9)
        row = random.randint(0, 9)

        if player_board[row][column] not in ['X', 'M']:
            if player_board[row][column] == 'O':
                player_board[row][column] = 'X'
                print("Computer has shot at position: "
                      + chr(column + ord('A'))
                      + str(row + 1))
                print("The enemy has hit your Battleship!")
                print_board("PLAYER BOARD", player_board)
                print_board("COMPUTER BOARD", computer_board_display)
                break
            else:
                player_board[row][column] = 'M'
                print("The enemy has missed your ships!")
                print_board("PLAYER BOARD", player_board)
                print_board("COMPUTER BOARD", computer_board_display)
                break


def count_hits(board):
    """
    #count the number of 'X' (direct) hit in board
    """
    return sum(row.count('X') for row in board)


def main():
    """
    While statement that checks if the menu input returns True.
    if it does, breaks the menu loop, proceeds to the board
    Print the boards for testing
    place 3 ships on the player board
    place 3 computer ships
    Print the boards for testing
    after players go, check computer boards for 3 X's, if so game over
    after computer go, check player board for 3 X's, if so game over
    """
    while True:
        print_game_menu()
        if menu_input():
            break

    print_board("PLAYER BOARD", player_board)
    print_board("COMPUTER BOARD", computer_board_display)

    place_player_ships(player_board, 3)
    print_board("PLAYER BOARD", player_board)

    place_computer_ships(computer_board_hidden, 3)

    print_board("PLAYER BOARD", player_board)
    print_board("COMPUTER BOARD", computer_board_display)

    while True:
        player_shoot(computer_board_display, computer_board_hidden)

        if count_hits(computer_board_display) == 3:
            print("VICTORY! You sank all enemy Battleships!")
            print("GAME OVER - you are the winner!")
            break

        computer_shoot(player_board)
        if count_hits(player_board) == 3:
            print("YOU SUFFER DEFEAT AT THE HANDS OF THE ENEMY!")
            print("GAME OVER - you have lost the game.")
            break


if __name__ == '__main__':
    main()
