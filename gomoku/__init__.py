"""Gomoku package - a 15x15 board game where players win by forming 5 in a row."""

from gomoku.game import Game
from gomoku.board import Board
from gomoku.winner import Winner

__all__ = ["Game", "Board", "Winner"]
