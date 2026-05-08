"""Interactive console UI for the Gomoku game."""

from gomoku.game import Game


def clear_screen():
    """Clear the terminal screen."""
    print("\033[2J\033[H", end="")


def display_board(board, size=15):
    """Display the 15x15 game board with row and column numbers."""
    print("    " + " ".join(f"{i:2d}" for i in range(size)))
    print("   " + " +" + "- " * size + "+")
    for row_idx, row in enumerate(board):
        print(f"{row_idx:2d} | " + " ".join(f"{cell:2s}" for cell in row) + " |")
    print("   " + " +" + "- " * size + "+")


def display_game_state(game, size=15):
    """Display the current game state including board and turn."""
    clear_screen()
    print("=" * 40)
    print("           GOMOKU GAME")
    print("=" * 40)
    print()
    display_board(game.board, size)
    print()
    print(f"Current turn: {game.current_player}")
    print()


def get_user_input():
    """Get and parse user input for move coordinates."""
    user_input = input("Enter your move (row col): ").strip()
    return user_input


def parse_move(input_str):
    """Parse the input string into row and column coordinates."""
    parts = input_str.split()
    if len(parts) != 2:
        raise ValueError("Input must be in format 'row col'")
    
    try:
        row = int(parts[0])
        col = int(parts[1])
    except ValueError:
        raise ValueError("Row and column must be integers")
    
    return row, col


def display_message(message):
    """Display a message to the user."""
    print()
    print(message)
    print()


def play_game():
    """Main game loop for interactive play."""
    game = Game()
    
    while not game.is_game_over:
        display_game_state(game)
        
        try:
            user_input = get_user_input()
            row, col = parse_move(user_input)
            
            if not game.is_valid_move(row, col):
                display_message("Invalid move! Position is out of bounds or already occupied.")
                continue
            
            game.make_move(row, col)
            
        except ValueError as e:
            display_message(f"Invalid input: {e}. Please use format 'row col' with integers 0-14.")
            continue
        except EOFError:
            display_message("\nGame interrupted. Exiting...")
            return
    
    display_game_state(game)
    
    if game.winner:
        display_message(f"Player {game.winner} wins!")
    else:
        display_message("It's a draw! The board is full.")


if __name__ == "__main__":
    play_game()
