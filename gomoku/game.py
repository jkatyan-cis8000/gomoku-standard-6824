from gomoku.board import Board
from gomoku.winner import Winner


class Game:
    """Main game controller for Gomoku.

    Orchestrates the game flow by managing the board, tracking player turns,
    validating moves, and detecting wins.
    """

    def __init__(self):
        """Initialize a new Gomoku game with a 15x15 board."""
        self._board = Board()
        self._winner = Winner(self._board)
        self._game_over = False
        self._winner_player = None

    def get_current_player(self) -> str:
        """Get the current player's color.

        Returns:
            The current player's color ("black" or "white").
        """
        return self._board.get_current_player()

    def make_move(self, row: int, col: int) -> bool:
        """Make a move at the given position.

        Args:
            row: Row index (0-14)
            col: Column index (0-14)

        Returns:
            True if the move was successful, False otherwise.
        """
        if self._game_over:
            return False

        if not self._board.is_valid_move(row, col):
            return False

        if not self._board.place_stone(row, col):
            return False

        if self._winner.check_winner(row, col):
            self._game_over = True
            self._winner_player = self._board.get_current_player()
            return True

        if self._board.is_board_full():
            self._game_over = True

        return True

    def get_game_state(self) -> dict:
        """Get the current game state.

        Returns:
            A dictionary containing:
                - current_player: The current player's color
                - board: The 15x15 board state (list of lists)
                - winner: The winner's color if the game is over, None otherwise
                - game_over: True if the game has ended
        """
        return {
            "current_player": self.get_current_player(),
            "board": self._board._board,
            "winner": self._winner_player,
            "game_over": self._game_over,
        }

    def is_game_over(self) -> bool:
        """Check if the game has ended.

        Returns:
            True if the game is over (win or draw), False otherwise.
        """
        return self._game_over

    def get_winner(self) -> str | None:
        """Get the winner of the game.

        Returns:
            The winner's color ("black" or "white") if there's a winner,
            None if the game is not over or ended in a draw.
        """
        return self._winner_player
