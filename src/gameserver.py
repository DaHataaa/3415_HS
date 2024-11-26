from src.gamestate import GameState
from src.hand import Hand
from src.field import Field, FieldNames
from src.stack import Stack


class GamePhase(enum.StrEnum):
    CREATE_DECK = "Create deck"
    CURRENT_TURN = "Current turn"
    SWAP_PLAYERS = "Swap players"
    GAME_END = "Game end"


class GameServer:
    def __init__(self, state: GameState | None = None, phase: GamePhase | None = None):
        self.game_state: GameState = state
        if self.game_state == None:
            self.game_state = GameState()

        self.current_phase = phase
        if self.current_phase == None:
            self.current_phase = GamePhase.CREATE_DECK

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.CREATE_DECK: self.create_deck_phase,
            GamePhase.CURRENT_TURN: self.current_turn_phase,
            GamePhase.SWAP_PLAYERS: self.swap_players_phase,
        }
        self.current_phase = phases[self.current_phase]()

    def create_deck_phase(self):
        pass

    def current_turn_phase(self):
        pass

    def switch_players_phase(self):
        GameState.swap_players()
