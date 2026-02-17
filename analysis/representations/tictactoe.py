from __future__ import annotations
from typing import Tuple, Optional

from games.tictactoe.state import TicTacToeState
from core.types import PlayerID


# ---------------------------------------------------------------------------
# Canonical Tic-Tac-Toe bitboard layout
#
# Bit indices:
#
# 6 7 8   ← top row
# 3 4 5
# 0 1 2   ← bottom row
#
# Bit 0 = bottom-left corner.
# ---------------------------------------------------------------------------

WIN_MASKS: Tuple[int, ...] = (
    # rows
    0b000000111,  # bottom
    0b000111000,  # middle
    0b111000000,  # top
    # columns
    0b001001001,  # left
    0b010010010,  # middle
    0b100100100,  # right
    # diagonals
    0b100010001,  # main diagonal
    0b001010100,  # anti-diagonal
)


# ---------------------------------------------------------------------------
# Conversion: game state → bitboards
# ---------------------------------------------------------------------------


def state_to_bitboards(state: TicTacToeState) -> Tuple[int, int]:
    """
    Convert TicTacToeState board into (x_bits, o_bits)
    using the canonical bottom-origin bit layout.
    """
    x_bits = 0
    o_bits = 0

    for r in range(3):
        for c in range(3):
            bit = (2 - r) * 3 + c  # flip vertically

            cell = state.board[r][c]
            if cell == 1:
                x_bits |= 1 << bit
            elif cell == -1:
                o_bits |= 1 << bit

    return x_bits, o_bits


def bitboard_key(x_bits: int, o_bits: int) -> Tuple[int, int]:
    """Hashable key for transposition tables."""
    return x_bits, o_bits


# ---------------------------------------------------------------------------
# Core terminal logic
# ---------------------------------------------------------------------------


def is_win(bits: int) -> bool:
    """Return True if the bitboard contains any winning pattern."""
    return any((bits & mask) == mask for mask in WIN_MASKS)


def winner_from_bitboards(
    x_bits: int,
    o_bits: int,
    player_x: PlayerID,
    player_o: PlayerID,
) -> Optional[PlayerID]:
    """Return the winning player if a win exists."""
    if is_win(x_bits):
        return player_x
    if is_win(o_bits):
        return player_o
    return None


def is_draw(x_bits: int, o_bits: int) -> bool:
    """Return True if board is full and there is no winner."""
    full_mask = 0b111111111
    return (x_bits | o_bits) == full_mask and not (is_win(x_bits) or is_win(o_bits))


def is_terminal(x_bits: int, o_bits: int) -> bool:
    """Terminal state = win or draw."""
    return is_win(x_bits) or is_win(o_bits) or is_draw(x_bits, o_bits)
