class Board:
    """A 15x15 game board for Gomoku.

    The board manages stone placement, tracks the current player,
    and provides methods for validating moves and checking board state.
    """

    def __init__(self):
        """Initialize an empty 15x15 board with black as the starting player."""
        self._board = [[None for _ in range(15)] for _ in range(15)]
        self._current_player = "black"
        self._moves_count = 0

    def place_stone(self, row: int, col: int) -> bool:
        """Place a stone on the board at the given position.

        Args:
            row: Row index (0-14)
            col: Column index (0-14)

        Returns:
            True if the stone was placed successfully, False otherwise.
        """
        if not self._is_valid_position(row, col):
            return False
        if self._board[row][col] is not None:
            return False
        self._board[row][col] = self._current_player
        self._moves_count += 1
        self._switch_player()
        return True

    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move at the given position is valid.

        Args:
            row: Row index (0-14)
            col: Column index (0-14)

        Returns:
            True if the position is valid and empty, False otherwise.
        """
        return self._is_valid_position(row, col) and self._board[row][col] is None

    def get_cell(self, row: int, col: int):
        """Get the stone at the given position.

        Args:
            row: Row index (0-14)
            col: Column index (0-14)

        Returns:
            The stone color ("black" or "white") or None if empty.
        """
        return self._board[row][col]

    def get_current_player(self) -> str:
        """Get the current player's color.

        Returns:
            The current player's color ("black" or "white").
        """
        return self._current_player

    def is_board_full(self) -> bool:
        """Check if the board is completely filled.

        Returns:
            True if all 225 cells are occupied, False otherwise.
        """
        return self._moves_count >= 225

    def get_moves_count(self) -> int:
        """Get the total number of moves made on the board.

        Returns:
            The number of stones currently on the board.
        """
        return self._moves_count

    def _is_valid_position(self, row: int, col: int) -> bool:
        """Check if the given position is within board bounds.

        Args:
            row: Row index to validate
            col: Column index to validate

        Returns:
            True if the position is within the 0-14 range, False otherwise.
        """
        return 0 <= row < 15 and 0 <= col < 15

    def _switch_player(self) -> None:
        """Switch the current player between black and white."""
        self._current_player = "white" if self._current_player == "black" else "black"
