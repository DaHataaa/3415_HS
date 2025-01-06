import os
from cards import load_cards
from field import FieldNames
from random import choices
from interrupts import Interrupt as I, int_ind as ii
from players.players_stats import stats

class CLI():

    def __init__(self):
        self.action = None
        self.chose = None
        self.I = I(0)



    def write(self, tabs, msg, PoI):
        (input if PoI else print)('\n' + ' '*tabs+ (msg if isinstance(msg, str) else ('\n' + ' '*tabs).join(msg)))



    def choose_cards(self):

        loaded = load_cards('cards/')
        os.system('cls')
        self.chose = input(f''' 
            Введите номера карт, которые хотите 
            видеть в колоде через пробел
            (в колоду попадут первые 8):

{'\n'.join([f'{i}. {loaded[1][i]}' for i in range(len(loaded[1]))])}

        ''').split(' ')

        if len(self.chose) < stats['stack_size']:
            input(f'Добавлено {stats['stack_size'] - len(self.chose) + int(not bool(self.chose[0]))} случайных недостающих карт')
            self.chose = choices(range(len(loaded[1])), k = 9 - len(self.chose))
        self.chose = list(map(int, self.chose[:8]))

        return [loaded[0][loaded[1][i]] for i in self.chose], dict(zip([loaded[1][i] for i in self.chose], [loaded[0][loaded[1][i]] for i in self.chose]))



    def choose_current_turn(self, hand, d_f, a_f):
        while True:

            os.system('cls')
            print(f"""      
                        {self.I.ind[ii.WR_INP]()}
                            Здоровье противника: {d_f.cards_list[FieldNames.PLAYER].hp} 
                            Мана противника: {d_f.cards_list[FieldNames.PLAYER].mn}

                            Ваше здоровье: {a_f.cards_list[FieldNames.PLAYER].hp}
                            Ваша мана: {a_f.cards_list[FieldNames.PLAYER].mn}
                  
                            Поле противника:        {d_f}
                            Ваше поле:              {a_f}

                            На руках есть:       {hand}
                            """)
            
            self.action = input("""
                            Действие:
                        1. Сыграть карту с руки
                        2. Атаковать юнита
                        3. Узнать информацию по карте
                        4. Закончить ход
                                
                       """)

            match self.action:
                case '1':
                    if self.choose_card_to_play(): return (self.action, int(self.chose[0]) - 1, int(self.chose[-1]) - 1)
                case '2':
                    if self.choose_unit_to_attack(): return (self.action, int(self.chose[0]) - 1, int(self.chose[-1]) - 1)
                case '3':
                    if self.check_card_info(): return (self.action, int(self.chose[0]), int(self.chose[-1]) - 1)
                case '4':
                    return (self.action, None)
                case _: self.I.flag = 1; continue



    def choose_card_to_play(self):

        self.chose = input("""
                        Введите номер карты на руке и номер ячейки через пробел
                      1-4 - Индекс карты
                      1-4 - Индекс ячейки | 5 - Игрока | 6 - Локации
                
                    """).split(' ')
        
        if self.chose[0] in tuple(map(str, range(1, stats['hand_size']+1))) and self.chose[-1] in tuple(map(str, range(1, stats['field_size']+1))): return True
        else: self.I.flag = 1



    def choose_unit_to_attack(self):

        self.chose = input("""
                        Введите номер своего юнита и номер карты противника через пробел
                      1-4 - Юниты
                      5   - Игрок
                
                      """).split(' ')
        
        if self.chose[0] in tuple(map(str, range(1, stats['hand_size']+1))) and self.chose[-1] in tuple(map(str, range(1, stats['field_size']))): return True
        else: self.I.flag = 1



    def check_card_info(self):

        self.chose = input("""
                        Введите область выбора и номер ячейки через пробел
                      1|2|3|4 - Карта на вашей руке|вашем поле|руке противника|поле противника
                      1-4 - Индекс ячейки | 5 - Игрока | 6 - Локации
                
                    """).split(' ')
        
        if self.chose[0] in ('1','3') and self.chose[-1] in tuple(map(str, range(1, stats['hand_size']+1))) or self.chose[0] in ('2', '4') and self.chose[-1] in tuple(map(str, range(1, stats['field_size']+1))): return True
        else: self.I.flag = 1



    def end_game(self):
        os.system('cls')
        input('Противник отчислен!\nВы победили!')