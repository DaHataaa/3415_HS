from src.player_interface import IPlayerInput, FieldNames

class CLI(IPlayerInput):
    def choose_cards(self, all_cards: dict):
        pass

    def choose_current_turn(self):
        match int(input('''
                        Действие:
                    1. Посмотреть карты на руке
                    2. Сыграть карту с руки
                    3. Атаковать юнита
                    4. Закончить ход
                    ''')):
            case 1:
                pass
            case 2: # try_play_card()
                pass
            case 3: # unit_attack()
                pass
            case 4: # turn_end()
                pass
        return

    def try_play_card(self, player, ifrom: int, ito: FieldNames):
        pass

    def unit_attack(self, server, ifrom: FieldNames, ito: FieldNames):
        pass

    def turn_end(self):
        pass
 

