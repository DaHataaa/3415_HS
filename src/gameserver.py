from src.gamestate import GameState
from src.hand import Hand
from src.field import Field, FieldNames
from src.stack import Stack
from src.players.cli import CLI
import enum
import random


class GamePhase(enum.StrEnum):
    CREATE_DECK = "Create deck"
    CURRENT_TURN = "Current turn"
    UNIT_ATTACK = "Unit attack"
    CHOOSE_CARD = "Choose card"
    SWAP_PLAYERS = "Swap players"
    GAME_END = "Game end"


class GameServer:
    def __init__(self, state: GameState | None = None, phase: GamePhase | None = None, cli: CLI | None = None):
        self.cli = cli if cli is not None else CLI()
        self.game_state = state if state is not None else GameState()
        self.current_phase = phase if phase is not None else GamePhase.CREATE_DECK
        self.phases = {
        GamePhase.CREATE_DECK: self.create_deck_phase,
        GamePhase.CURRENT_TURN: self.current_turn,
        GamePhase.SWAP_PLAYERS: self.swap_players_phase,
        GamePhase.GAME_END: self.end_game,
        }

    def get_def_hand(self):
        return self.game_state.defender.get_hand()

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        self.phases[self.current_phase]()

    def create_deck_phase(self):
        self.game_state = GameState()
        self.current_phase = GamePhase.CURRENT_TURN

    def current_turn(self):
        while True:
            inp = self.cli.choose_current_turn(self.get_def_hand())
            match int(inp[0]):
                case 1:
                    self.game_state.play_card(inp[1], inp[2])
                case 2:
                    self.game_state.attack(inp[1], inp[2])
                case 3:
                    break
        self.current_phase = GamePhase.SWAP_PLAYERS

    def swap_players_phase(self):
        self.game_state.swap_players()
        self.current_phase = GamePhase.CURRENT_TURN

    def end_game():
        exit()

    