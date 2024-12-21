from src.player_interface import IPlayerInput
from src.field import FieldNames
from src.gameserver import GameServer as gs
import os

class CLI(IPlayerInput):

    def choose_cards(self, all_cards: dict):
        pass

    def choose_card_to_play(self) -> tuple[int, FieldNames]:
        chose = input(
                """
                        Действие:
                    ret - Вернуться к выбору действий
                    1-4 - Использовать карту с руки
                    """)
        match chose:
            case 'ret': pass
            case _: pass

    def choose_unit_to_attack(self) -> tuple[FieldNames, FieldNames]:
        pass

    def turn_end(self):
        pass

    def choose_current_turn(self, game_server):
        os.system('cls')
        print(f"""
                    На руках есть: {game_server.get_def_hand()}
                    """)
        match int(
            input(
                """
                        Действие:
                    1. Сыграть карту с руки
                    2. Атаковать юнита
                    3. Закончить ход
                    """
            )
        ):
            case 1: self.choose_card_to_play()
            case 2: self.choose_unit_to_attack()
            case 3: self.turn_end()

