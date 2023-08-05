# BATTLESHIPS GAME



## Introduction

Hello there! Welcome to my Python program that serves as a command-line interface (CLI) rendition of the timeless board game Battleships. In this interactive arena, it's you (the user) squaring off against the computer (the enemy), making strategic moves, and guessing the locations of each other's ships.

Both you (as the player) and the computer get your own boards to place your ships, after which the fun truly begins! The objective is simple yet compelling: Be the first to hit all of your opponent's ships, and victory is yours.

So come aboard, brace for some classic naval warfare, and let's see who can outwit the other. Ready to set sail? Let's dive right in!


## Installation

You can run this game on any system that has Python 3 installed. No additional packages are required. You can execute the game by running the command:
python3 run.py

## Features

User Input Validation

*I've built-in some handy input validation checks in the game. 
If the user attempts to place a ship or fire a shot outside of the board, or at a location you've already shot at (or a ship is already placed), the game will prompt you to enter a valid location.

*Computer Opponent
You'll be facing off against a computer opponent who 'thinks'... and then randomly places their ships and fires shots!

*Dual Board Display
The game prints both your board and the computer's board after every turn, so you can keep track of all your hits and misses. The computer's board will only display the locations where you've fired shots, not the locations of the computer's ships. The computers board placement is stored on a 'hidden' board that is not printed. 

## Code Description

*The game is coded in Python, and the game loop runs in the main function. The board setup, ship placement, turns, and checks for wins are all handled within this loop.

*Each function is properly documented.

*This diagram shows the logic of the game
![Flowchart](./readme_images/Flow Diagram.png)


### User Stories

User stories that informed the design and functionality of the game

# 	User Stories
* 	I want to be welcomed by a start screen with name of the game.
* 	I want to see familiar battleships board designs.
* 	I want to see my boat.
* 	I want to see where my missed shots are. 
* 	I want to see the computers missed shots.
* 	I dont want to see the computers ships unless i hit them.
* 	I want some helpful prompts for bugs.
* 	I want to know if i have won or lost the game!

User stories for future developments:
* 	I want to choose the board size.
* 	I want to see a running score.
* 	I would like to see a better interface.
* 	I want the option to play another human.
*   I want different ship sizes.

### Test Cases

*   Game start function loops until user enters valid input
![Testcase_1](.readme_images/Test1_gamestartloop.PNG)

*   User input validation checks if the users ship placement is off the board and prompts user to try again.
![Testcase_2](.readme_images/Test2_shipplacementoffboard.PNG)

*   User input validation checks if user submission is blank and prompts to enter again with explanation "Oh no! You entered nothing!
![Testcase_3](.readme_images/Test3_shipplacementblank.PNG)

*   User input validation checks if user submission for ship placement is not valid (not letter, then number 1-10) and prompts user to enter again with explanation "Oh no! Thats not a letter and number within the board!"
![Testcase_4](.readme_images/Test4_shipplacementnotvalid.PNG)

*   User input validation check after letter & number validation is passed, if user submission for ship placement is within the limits of the board. If user enters letter & number combination that is not, prompts user to resubmit with explanation "Oh no! Thats outside the board!"
![Testcase_5](.readme_images/Test5_shipplacementoffboard.PNG)

*   The same user input validation checks are re-used for the users shots, with the same explanations. 
![Testcase_6](.readme_images/Test6_usershotvalidation.PNG)


### Future Development plans
For future developments in this project, I will be looking to;
* remove the unused function in line 171.
* add the option for users to choose a board size
* add different ship sizes
* add the ability for users to play against other users
* add more graphical elements to the menu & win/lose screens