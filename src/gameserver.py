from gamestate import GameState
from field import FieldNames
from players.cli import CLI
from enum import StrEnum


class GamePhase(StrEnum):
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
        GamePhase.CREATE_DECK: self.create_deck,
        GamePhase.CURRENT_TURN: self.current_turn,
        GamePhase.SWAP_PLAYERS: self.swap_players,
        GamePhase.GAME_END: self.end_game}

    def run(self):
        while 'run':
            self.run_one_step()

    def run_one_step(self):
        self.phases[self.current_phase]()

    def create_deck(self):
        self.game_state = GameState()
        self.game_state.deck_created()
        self.current_phase = GamePhase.CURRENT_TURN

    def current_turn(self):
        self.current_phase = GamePhase.SWAP_PLAYERS
        while True:
            inp = self.cli.choose_current_turn(self.game_state.attacker.get_hand(), self.game_state.defender.get_field(), self.game_state.attacker.get_field())

            match int(inp[0]):
                case 1:
                    self.game_state.play_card(inp[1], inp[2])
                    self.game_state.skipped_turn = False

                case 2:
                    self.game_state.attack(inp[1], inp[2])
                    if self.game_state.defender.kill_check(inp[2]) and self.game_state.defender.field.get_card(FieldNames.PLAYER) is None:
                        self.current_phase = GamePhase.GAME_END
                        break

                case 3:
                    info = self.game_state.card_info(2 - inp[1]%2, inp[2])
                    self.cli.write(20, ([f'{i} = {info[i]}' for i in(list(info))]+['\nПрожмите enter для продолжения игры'] if not isinstance(info, str) else info), 1)

                case 4:
                    break

    def swap_players(self):
        self.game_state.next_turn()
        self.game_state.update_hand(self.game_state.attacker)
        self.game_state.update_hand(self.game_state.defender)
        self.current_phase = GamePhase.CURRENT_TURN

    def end_game(self):
        self.cli.end_game()
        exit()