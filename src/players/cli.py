import os
from src.cards import load_cards
from field import FieldNames

class CLI():
    def __init__(self):
        self.action = None
        self.chose = None


    def choose_cards(self):
        loaded = load_cards('cards/')
        self.chose = input(f''' Введите номера карт, которые хотите 
                                видеть в колоде через пробел
                                (в колоду попадут первые 8):
                           
{'\n'.join([f'{i}. {loaded[1][i]}' for i in range(len(loaded[1]))])}

''').split(' ')
        self.chose = [0,1,2,3,4,5,6,7] #####
        self.chose = list(map(int, self.chose[:8]))
        return dict(zip([loaded[1][i] for i in self.chose],[loaded[0][loaded[1][i]] for i in self.chose]))


    def choose_card_to_play(self):
        self.chose = input("""
                        Введите номер карты на руке и номер ячейки через пробел
                      1-4 - Индекс карты
                      1-4 - Индекс ячейки
                      
                    """)
        if self.chose[0] in ('1','2','3','4') and self.chose[2] in ('1','2','3','4'): return True


    def choose_unit_to_attack(self):
        self.chose = input("""
                        Введите номер своего юнита и номер карты противника через пробел
                      1-4 - Юниты
                      5   - Игрок
                    
                      """)
        if self.chose[0] in ('1','2','3','4') and self.chose[2] in ('1','2','3','4','5'): return True


    def choose_current_turn(self, hand, d_f, a_f):
        while True:
            os.system('cls')
            print(f"""
                            Здоровье противника: {d_f.cards_list[FieldNames.PLAYER].hp} 
                  
                            Поле противника:  {d_f}     
                            Ваше поле:        {a_f}

                            На руках есть:   {hand}
                            """)
            self.action = input("""
                            Действие:
                        1. Сыграть карту с руки
                        2. Атаковать юнита
                        3. Закончить ход
                        """)
            match self.action:
                case '1': 
                    if self.choose_card_to_play(): return (self.action, int(self.chose[0])-1, int(self.chose[2])-1)
                case '2': 
                    if self.choose_unit_to_attack(): return (self.action, int(self.chose[0])-1, int(self.chose[2])-1)
                case '3': 
                    return (self.action, None)
                case _: continue

    def end_game(self):
        os.system('cls')
        print('Вы победили!')