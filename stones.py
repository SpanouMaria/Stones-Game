import random

# Function to print the game board
def print_board(board):
    # Prints the current state of the game board with column numbers and row labels
    # Column headers
    print("  1   2   3")  
    for i, row in enumerate(board):
        # Print each row with A, B, C labels
        print(chr(65 + i), " | ".join(row))  
        
        # Add horizontal dividers between rows, except the last row
        if i < 2:  
            print("  ---+---+---")

# Function to validate board position input
def is_valid_position(pos):
    # Checks if the input position is valid (e.g., within "A1" to "C3")
    return len(pos) == 2 and pos[0] in "ABC" and pos[1] in "123"

# Function to convert a board position to row and column indices
def pos_to_index(pos):
    # Converts positions like "A1" into indices for the board array
    return ord(pos[0]) - 65, int(pos[1]) - 1

# Function to check if a player has won the game
def check_line_win(board, marker):
    # Checks rows, columns, and diagonals for three matching markers
    for row in board:  # Check each row for a win
        if all(cell == marker for cell in row):
            return True
    
    # Check each column for a win
    for col in range(3):  
        if all(row[col] == marker for row in board):
            return True
    
    # Check diagonals for a win
    if all(board[i][i] == marker for i in range(3)) or all(board[i][2 - i] == marker for i in range(3)):
        return True
    return False

# Function to validate a move during the game
def is_valid_move(board, from_pos, to_pos, player_marker):
    # Checks if the move from one position to another is valid
    if not (is_valid_position(from_pos) and is_valid_position(to_pos)):
        return False  # Both positions must be valid
    
    # Convert origin position
    from_row, from_col = pos_to_index(from_pos) 
    
    # Convert destination position 
    to_row, to_col = pos_to_index(to_pos)  
    
    # Check if the origin has the player's marker and destination is empty
    if board[from_row][from_col] != player_marker or board[to_row][to_col] != " ":
        return False
    
    # Ensure the move is to a neighboring position
    return abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1

# Main function to start the game
def play_game():
    # Initialize a 3x3 empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Symbols for Player 1 and Player 2
    players = ["x", "o"]

    # Randomly decide the starting player  
    random.shuffle(players)  
    print(f"Player 1 is '{players[0]}' and Player 2 is '{players[1]}'.")

    # Phase 1: Initial peg placement
    for i, player in enumerate(players):
        # Each player places three pegs
        for peg in range(3):  
            while True:
                # Display the board
                print_board(board)  
                pos = input(f"Player {i + 1} ('{player}'), place your peg {peg + 1}: ").upper()
                
                # Validate the input position
                if is_valid_position(pos):  
                    # Convert to board indices
                    row, col = pos_to_index(pos)  
                    
                    # Check if the position is empty
                    if board[row][col] == " ":  
                        # Place the player's peg
                        board[row][col] = player  
                        break
                    else:
                        print("Position already occupied. Try again.")
                else:
                    print("Invalid position. Try again.")

    # Phase 2: Alternate moves until someone wins
    # Keeps track of whose turn it is
    turn = 0  
    while True:
        # Determine the current player
        current_player = players[turn % 2]  
        
        # Display the board
        print_board(board)  
        while True:
            # Prompt the player to make a move
            move = input(f"Player {turn % 2 + 1} ('{current_player}'), enter your move (e.g., A1B2): ").upper()
            
            # Validate move format (e.g., "A1B2")
            if len(move) == 4:  
                # Split into origin and destination
                from_pos, to_pos = move[:2], move[2:]  
                
                # Validate the move
                if is_valid_move(board, from_pos, to_pos, current_player):  
                    # Get origin indices
                    from_row, from_col = pos_to_index(from_pos)  
                    
                    # Get destination indices
                    to_row, to_col = pos_to_index(to_pos)  
                    
                    # Remove the peg from the origin
                    board[from_row][from_col] = " "  
                    
                    # Place it at the destination
                    board[to_row][to_col] = current_player  
                    break
            
            # Ask again for invalid moves
            print("Invalid move. Try again.")  

        # Check if the current player has won
        if check_line_win(board, current_player):
            # Display the final board
            print_board(board)  
            
            # Announce the winner
            print(f"Player {turn % 2 + 1} ('{current_player}') wins!")  
            break
        
        # Switch turns
        turn += 1  

# Run the game if the script is executed
if __name__ == "__main__":
    play_game()
