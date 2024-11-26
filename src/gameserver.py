from src.gamestate import GameState
from src.hand import Hand
from src.field import Field, FieldNames
from src.stack import Stack


class GameServer:
    def __init__(self, state: GameState):
        self.game_state = state

    @classmethod
    def new_game(cls):
        p1 = Player(Field(), Hand(), Stack())
        p2 = Player(Field(), Hand(), Stack())
        state = GameState(p1, p2)
        return cls(state)
