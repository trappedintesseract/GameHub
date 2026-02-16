

from __future__ import annotations
from typing import Tuple, Iterable

from games.tictactoe.state import TicTacToeState


Move = Tuple[int, int]


def render_board(state: TicTacToeState) -> None:
    symbol_map = {
        1: "X",
        -1: "O",
        0: ".",
    }

    print("\nBoard:")

    for row in state.board:
        print(" ".join(symbol_map[cell] for cell in row))

    print()  # blank line for spacing


def prompt_move(legal_moves: Iterable[Move]) -> Move:
    """
    Ask the user for a move until a valid one is entered.
    """
    legal_moves = set(legal_moves)  # fast membership check

    while True:
        try:
            raw = input("Enter move as 'row col': ").strip()
            r_str, c_str = raw.split()

            move = (int(r_str), int(c_str))

            if move in legal_moves:
                return move

            print("Invalid move. Try again.")

        except ValueError:
            print("Invalid format. Please enter two numbers like: 1 2")
        except Exception:
            print("Unexpected error. Try again.")
