

from __future__ import annotations

from core.match import Match

from games.tictactoe.game import TicTacToeGame
from games.tictactoe.state import TicTacToeState

from players.human.cli_ttt import HumanCLITicTacToePlayer
from ui.cli.tictactoe import render_board
from typing import Dict
from core.types import PlayerID
from core.player import Player

def main() -> None:
    game = TicTacToeGame()

    players:Dict[PlayerID,Player] = {
        game.PLAYER_X: HumanCLITicTacToePlayer(game.PLAYER_X),
        game.PLAYER_O: HumanCLITicTacToePlayer(game.PLAYER_O),
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
