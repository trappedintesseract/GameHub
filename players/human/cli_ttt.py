
from __future__ import annotations
from typing import Iterable

from core.player import Player
from core.state import State
from core.types import Action, PlayerID

from games.tictactoe.state import TicTacToeState
from ui.cli.tictactoe import render_board, prompt_move


class HumanCLITicTacToePlayer(Player):

    def __init__(self, player_id: PlayerID):
        super().__init__(player_id)


    def select_action(
        self,
        state: State,
        legal_actions: Iterable[Action],
    ) -> Action:
        assert isinstance(state, TicTacToeState)

        print(f"\nPlayer {self.player_id}'s turn")

        render_board(state)
        move = prompt_move(legal_actions)

        return move
