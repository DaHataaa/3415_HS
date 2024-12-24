import os
from cards import load_cards
from field import FieldNames
from random import choices
from interrupts import Interrupt as I, int_ind as ii

class CLI():



    def __init__(self):
        self.action = None
        self.chose = None
        self.I = I()



    def choose_cards(self):

        loaded = load_cards('cards/')
        os.system('cls')
        self.chose = input(f''' Введите номера карт, которые хотите 
                                видеть в колоде через пробел
                                (в колоду попадут первые 8):
                           
{'\n'.join([f'{i}. {loaded[1][i]}' for i in range(len(loaded[1]))])}

''').split(' ')

        if len(self.chose) < 8:
            print(f'Добавлено {9 - len(self.chose)} случайных недостающих карт')
            self.chose = choices(range(len(loaded[1])), k = 9 - len(self.chose))
        self.chose = list(map(int, self.chose[:8]))
        print(self.chose)
        print(dict(zip([loaded[1][i] for i in self.chose], [loaded[0][loaded[1][i]] for i in self.chose])))
        return [loaded[0][loaded[1][i]] for i in self.chose], dict(zip([loaded[1][i] for i in self.chose], [loaded[0][loaded[1][i]] for i in self.chose]))



    def choose_card_to_play(self):

        self.chose = input("""
                        Введите номер карты на руке и номер ячейки через пробел
                      1-4 - Индекс карты
                      1-4 - Индекс ячейки | 5 - Игрока | 6 - Локации
                      
                    """).split(' ')
        
        if self.chose[0] in ('1','2','3','4') and self.chose[-1] in ('1','2','3','4','5','6'): return True
        else: self.I.flag = 1


    def choose_unit_to_attack(self):

        self.chose = input("""
                        Введите номер своего юнита и номер карты противника через пробел
                      1-4 - Юниты
                      5   - Игрок
                    
                      """).split(' ')
        
        if self.chose[0] in ('1','2','3','4') and self.chose[-1] in ('1','2','3','4','5'): return True
        else: self.I.flag = 1



    def choose_current_turn(self, hand, d_f, a_f):
        while True:

            os.system('cls')
            print(f"""      
                        {self.I.ind[ii.WR_INP]()}
                            Здоровье противника: {d_f.cards_list[FieldNames.PLAYER].hp} 
                  
                            Поле противника:        {d_f}     
                            Ваше поле:              {a_f}

                            На руках есть:       {hand}
                            """)
            
            self.action = input("""
                            Действие:
                        1. Сыграть карту с руки
                        2. Атаковать юнита
                        3. Закончить ход
                        """)

            match self.action:
                case '1': 
                    if self.choose_card_to_play(): return (self.action, int(self.chose[0])-1, int(self.chose[-1])-1)
                case '2': 
                    if self.choose_unit_to_attack(): return (self.action, int(self.chose[0])-1, int(self.chose[-1])-1)
                case '3': 
                    return (self.action, None)
                case _: self.I.flag = 1; continue



    def end_game(self):
        os.system('cls')
        print('Противник отчислен!\nВы победили!')