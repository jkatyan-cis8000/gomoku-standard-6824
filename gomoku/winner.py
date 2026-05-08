class Winner:
    """Win detection for Gomoku game.

    Checks for five consecutive stones of the same color in any direction
    after a move is made. A player wins by forming an unbroken line of
    exactly five stones horizontally, vertically, or diagonally.
    """

    def __init__(self, board):
        """Initialize the Winner class with a board reference.

        Args:
            board: The Board instance to check for wins.
        """
        self._board = board

    def check_winner(self, row: int, col: int) -> bool:
        """Check if the last move at (row, col) resulted in a win.

        Args:
            row: Row index of the last placed stone
            col: Column index of the last placed stone

        Returns:
            True if five consecutive stones of the same color exist,
            False otherwise.
        """
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            return False

        player = self._board.get_cell(row, col)
        if player is None:
            return False

        directions = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal (bottom-right)
            (1, -1),  # anti-diagonal (bottom-left)
        ]

        for dr, dc in directions:
            if self._check_line(row, col, dr, dc, player):
                return True

        return False

    def _check_line(self, row: int, col: int, dr: int, dc: int, player: str) -> bool:
        """Check for five consecutive stones in a specific direction.

        Args:
            row: Starting row index
            col: Starting column index
            dr: Row direction increment
            dc: Column direction increment
            player: The player's color to check for

        Returns:
            True if five consecutive stones of the player's color exist,
            False otherwise.
        """
        count = 1

        for i in range(1, 5):
            r, c = row + dr * i, col + dc * i
            if r < 0 or r >= 15 or c < 0 or c >= 15:
                break
            if self._board.get_cell(r, c) != player:
                break
            count += 1

        if count >= 5:
            return True

        for i in range(1, 5):
            r, c = row - dr * i, col - dc * i
            if r < 0 or r >= 15 or c < 0 or c >= 15:
                break
            if self._board.get_cell(r, c) != player:
                break
            count += 1

        return count >= 5
