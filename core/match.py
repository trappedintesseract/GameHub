from __future__ import annotations
from typing import Dict, List, Tuple
from .game import Game
from .player import Player
from .state import State
from .types import PlayerID, JointAction, Result

class Match:

    def __init__(self, game: Game, players: Dict[PlayerID, Player]):
        self.game = game
        self.players = players


    def run(self) -> Tuple[Result, List[State]]:
        state = self.game.initial_state()
        history: List[State] = [state]

        while not self.game.is_terminal(state):

            active = self.game.active_players(state)

            joint_action: JointAction = {}

            for pid in active:
                player = self.players[pid]

                legal = self.game.legal_actions(state, pid)

                action = player.select_action(state, legal)

                joint_action[pid] = action

            state = self.game.next_state(state, joint_action)
            history.append(state)
        result = self.game.result(state)
        return result, history
