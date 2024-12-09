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

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.CREATE_DECK: self.create_deck_phase,
            GamePhase.CURRENT_TURN: self.current_turn_phase,
            GamePhase.SWAP_PLAYERS: self.swap_players_phase,
            GamePhase.GAME_END: self.end_game
        }
        self.current_phase = phases[self.current_phase]()

    def create_deck_phase(self):
        self.game_state = GameState()
        self.current_phase = GamePhase.CURRENT_TURN

    def current_turn_phase(self, TOG): #Временно переделана под асцу, не доделал
        
        match TOG:
            case 0: #Ascii режим
                match int(input('''
                                Действие:
                            1. Атаковать карту
                            2. Посмотреть колоду
                            3. 
                            ''')):
                    case 0:
                        input('Введите индекс карты атаки и индекс карты врага ([0:3] - карты, 4 - игрок)')
                    case 0:
                        pass
                    case 0:
                        pass
                    case 0:
                        pass
                    case 0:
                        pass
            case 1: #Режим с графикой
                pass

    def switch_players_phase(self):
        GameState.swap_players()

    def end_game():
        pass