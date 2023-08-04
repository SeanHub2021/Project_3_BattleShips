#BATTLESHIPS GAME

##Introduction

Hello there! Welcome to my Python program that serves as a command-line interface (CLI) rendition of the timeless board game Battleships. In this interactive arena, it's you (the user) squaring off against the computer (the enemy), making strategic moves, and guessing the locations of each other's ships.

Both you (as the player) and the computer get your own boards to place your ships, after which the fun truly begins! The objective is simple yet compelling: Be the first to hit all of your opponent's ships, and victory is yours.

So come aboard, brace for some classic naval warfare, and let's see who can outwit the other. Ready to set sail? Let's dive right in!


##Installation

You can run this game on any system that has Python 3 installed. No additional packages are required. You can execute the game by running the command:
python3 run.py

##Features

User Input Validation

*I've built-in some handy input validation checks in the game. 
If the user attempts to place a ship or fire a shot outside of the board, or at a location you've already shot at (or a ship is already placed), the game will prompt you to enter a valid location.

*Computer Opponent
You'll be facing off against a computer opponent who 'thinks'... and then randomly places their ships and fires shots!

*Dual Board Display
The game prints both your board and the computer's board after every turn, so you can keep track of all your hits and misses. The computer's board will only display the locations where you've fired shots, not the locations of the computer's ships. The computers board placement is stored on a 'hidden' board that is not printed. 

#Code Description

*The game is coded in Python, and the game loop runs in the main function. The board setup, ship placement, turns, and checks for wins are all handled within this loop.

*Each function is properly documented, up to scale . Whether you're playing the game or studying the code, there's plenty to learn!