

from __future__ import annotations

from core.match import Match

from games.tictactoe.game import TicTacToeGame
from games.tictactoe.state import TicTacToeState

from players.human.cli_ttt import HumanCLITicTacToePlayer
from players.ai.games.tictactoe.random import RandomTicTacToePlayer
from ui.cli.tictactoe import render_board
from typing import Dict
from core.types import PlayerID
from core.player import Player
def choose_player(player_id: PlayerID):
    """
    Ask user which type of player to create for a given PlayerID.
    """

    while True:
        print(f"\nSelect player type for '{player_id}':")
        print("  1 → Human (CLI)")
        print("  2 → Random AI")
        print("  3 → Minimax AI")

        choice = input("Enter choice (1, 2, or 3): ").strip()

        # ------------------------------------------------------------
        # Human
        # ------------------------------------------------------------
        if choice == "1":
            from players.human.cli_ttt import HumanCLITicTacToePlayer
            return HumanCLITicTacToePlayer(player_id)

        # ------------------------------------------------------------
        # Random AI
        # ------------------------------------------------------------
        if choice == "2":
            from players.ai.games.tictactoe.random import RandomTicTacToePlayer
            return RandomTicTacToePlayer(player_id)

        # ------------------------------------------------------------
        # Minimax AI (with depth selection)
        # ------------------------------------------------------------
        if choice == "3":
            from players.ai.games.tictactoe.minimax import MinimaxTicTacToePlayer

            depth_input = input(
                "Enter depth (press Enter for perfect play): "
            ).strip()

            depth = None if depth_input == "" else int(depth_input)

            return MinimaxTicTacToePlayer(player_id, depth=depth)

        print("Invalid choice. Please enter 1, 2, or 3.")

def main() -> None:
    game = TicTacToeGame()

    players:Dict[PlayerID,Player] = {
        game.PLAYER_X: choose_player(game.PLAYER_X),
        game.PLAYER_O: choose_player(game.PLAYER_O),
    }

    match = Match(game=game, players=players)

    result, history = match.run()

    final_state = history[-1]
    assert isinstance(final_state, TicTacToeState)

    print("\n=== Final Board ===")
    render_board(final_state)

    print("=== Result ===")
    for pid, reward in result.items():
        print(f"Player {pid}: {reward}")



if __name__ == "__main__":
    main()
