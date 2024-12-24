from enum import StrEnum

class int_ind(StrEnum):
    WR_INP = 'Wrong input'

class Interrupt:
    
    def __init__(self, flag: None | int = None):
        self.flag = flag
        self.ind = {
            int_ind.WR_INP: self.wrong_input
        }

    def __str__(self):
        return ''
    
    def wrong_input(self):
        if self.flag:
            self.flag = False
            return 'Неккоректный ввод'
        else:
            return ''
    
    