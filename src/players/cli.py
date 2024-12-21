from src.field import FieldNames
import os

class CLI():
    def __init__(self):
        self.action = None
        self.chose = None

    def choose_cards(self, all_cards: dict):
        pass

    def __repr__(self):
        return

    def choose_card_to_play(self):
        self.chose = input("""
                        Введите номер карты на руке и номер ячейки через пробел
                      1-4 - Индекс карты
                      1-4 - Индекс ячейки
                      
                    """)
        match self.chose[0]:
            case '1'|'2'|'3'|'4': 
                match self.chose[2]:
                    case '1'|'2'|'3'|'4': return True


    def choose_unit_to_attack(self):
        self.chose = input("""
                        Введите номер своего юнита и номер карты противника через пробел
                      1-4 - Юниты
                      5 - Игрок
                    
                      """)
        match self.chose[0]:
            case '1'|'2'|'3'|'4': 
                match self.chose[2]:
                    case '1'|'2'|'3'|'4'|'5': return True


    def choose_current_turn(self, hand):
        while True:
            os.system('cls')
            print(f"""
                            На руках есть: {hand}
                            """)
            self.action = input("""
                            Действие:
                        1. Сыграть карту с руки
                        2. Атаковать юнита
                        3. Закончить ход
                        """)
            match self.action:
                case '1': 
                    if self.choose_card_to_play(): return (self.action, int(self.chose[0]), int(self.chose[2]))
                case '2': 
                    if self.choose_unit_to_attack(): return (self.action, int(self.chose[0]), int(self.chose[2]))
                case '3': 
                    return (self.action, None)
                case _: continue