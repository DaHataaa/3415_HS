from src.gamestate import GameState
from src.hand import Hand
from src.field import Field, FieldNames
from src.stack import Stack
import enum
import random

class GamePhase(enum.StrEnum):
    CREATE_DECK = "Create deck"
    CURRENT_TURN = "Current turn"
    SWAP_PLAYERS = "Swap players"
    GAME_END = "Game end"


class GameServer:
    def __init__(self, state: GameState | None = None, phase: GamePhase | None = None):
        self.game_state = state if state != None else GameState()
        self.current_phase = phase if phase != None else GamePhase.CREATE_DECK
        self.phases = {
            GamePhase.CREATE_DECK: self.create_deck_phase,
            GamePhase.CURRENT_TURN: self.current_turn_phase,
            GamePhase.SWAP_PLAYERS: self.swap_players_phase,
            GamePhase.GAME_END: self.end_game
        }

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        #print(self.current_phase) #для проверки
        self.phases[self.current_phase]()

    def create_deck_phase(self):
        self.game_state = GameState()
        self.current_phase = GamePhase.CURRENT_TURN

    def current_turn_phase(self):
        self.current_phase = GamePhase.SWAP_PLAYERS

    def swap_players_phase(self):
        self.game_state.swap_players()
        self.current_phase = GamePhase.CURRENT_TURN


    def end_game():
        pass
