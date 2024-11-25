# The Stones Game

Welcome to the "Stones Game", a strategic two-player board game implemented in Python. The goal is to form a straight line (three-in-a-row) with your pegs before your opponent does.


## Game Instructions
- Objective: Be the first player to align three of your pegs (horizontally, vertically, or diagonally) on a 3x3 board.
- How to Play: The game starts with a random draw to determine which player goes first. Each player alternates placing their three pegs ('x' for Player 1 and 'o' for Player 2) on empty positions on the board. Pegs 
  cannot form a line during this phase. Once all pegs are placed, players take turns moving one peg at a time to a neighboring empty space. The game continues until a player successfully forms a straight line with 
  their pegs.
- **Game End:** The game ends when one player aligns three pegs, and they are declared the winner.


## Implementation Details
- The game is implemented in Python as a command-line interface.
- The board is represented as a 3x3 grid, initialized with empty spaces.
- Game logic includes: Functions to handle peg placement and movement. Validation of moves to ensure they follow the rules. Continuous updates of the game state and board display.


## How to Run
- **Clone the Repository:**
  ```bash
  git clone https://github.com/ChristosGkovaris/The-Stones-Game.git
  cd The-Stones-Game
- Ensure you have Python installed: The game requires Python 3. Ensure it is installed on your system.
- Run the game: **stones.py**


## Collaboration
This project was a collaborative effort. Special thanks to [ChristosGkovaris](https://github.com/ChristosGkovaris) for their significant contributions to the development and improvement of the game.
