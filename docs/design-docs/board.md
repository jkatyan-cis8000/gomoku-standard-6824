# Board Module Design Doc

## Overview

The `board.py` module implements the `Board` class, which manages the 15x15 Gomoku game board state, player turns, and stone placement.

## Architecture

### Board Class

The `Board` class is responsible for:

1. **Board Representation**: A 15x15 grid (indices 0-14) implemented as a list of lists
2. **Stone Placement**: Placing black or white stones on the board
3. **Position Validation**: Ensuring moves are within bounds and on empty cells
4. **Player Tracking**: Maintaining the current player (black or white)
5. **Move Counting**: Tracking total moves for draw detection

### Key Methods

#### `place_stone(row, col) -> bool`
Attempts to place a stone at the given position. Returns `True` on success, `False` if the position is invalid or occupied.

#### `is_valid_move(row, col) -> bool`
Checks if a move at the given position would be valid without modifying the board.

#### `get_cell(row, col)`
Returns the stone at the given position (None if empty).

#### `get_current_player() -> str`
Returns the current player's color ("black" or "white").

#### `is_board_full() -> bool`
Returns `True` if all 225 cells are occupied.

#### `get_moves_count() -> int`
Returns the total number of stones placed on the board.

### State Management

- **Initial State**: Empty board, black player starts
- **Turn Alternation**: After each successful move, the current player switches
- **Move Validation**: Two checks - position bounds and cell emptiness

## Design Decisions

### 1. Board Representation

**Decision**: Use a simple 2D list (`list[list[None | str]]`)

**Rationale**: 
- Simple and efficient for a fixed-size 15x15 board
- Direct indexing without complex calculations
- Python lists provide O(1) access time

### 2. Player Representation

**Decision**: Use strings "black" and "white" instead of enums or integers

**Rationale**:
- More readable for debugging and logging
- No need for external dependencies (enum)
- Easy to serialize/deserialize

### 3. Turn Switching

**Decision**: Switch player immediately after placing a stone

**Rationale**:
- Ensures the current player is always correct
- Simplifies the API - callers don't need to track turns

### 4. Validation

**Decision**: Separate `is_valid_move()` from `place_stone()`

**Rationale**:
- Allows checking moves before making them
- Useful for UI validation and game logic

## Constraints

1. **Fixed Size**: Board is hardcoded to 15x15
2. **No Undo**: Once a stone is placed, it cannot be removed
3. **No History**: Board doesn't track move history

## Usage Example

```python
from gomoku.board import Board

board = Board()
board.place_stone(7, 7)  # Black places at center
board.get_current_player()  # Returns "white"
board.is_valid_move(7, 8)  # Returns False (occupied)
board.is_board_full()  # Returns False
```
