from enum import IntEnum
from cards import *


class FieldNames(IntEnum):
    UNIT1 = 0
    UNIT2 = 1
    UNIT3 = 2
    UNIT4 = 3
    PLAYER = 4
    LOCATION = 5


class Field:
    def __init__(self, cards_list: list | None = None):
        self.cards_list = cards_list if cards_list != None else [None] * (len(FieldNames) - 2) + [PlayerUnit(), None]

    def __repr__(self):
        return self.cards_list

    def __str__(self):
        return ' '.join(list(map(str, self.cards_list)))
    
    def __eq__(self, other):

        for i in range(len(self.cards_list)):
            if self.cards_list[i] != other.cards_list[i]:
                return False
        return True

    def change_mp(self, ind, d_mn):
        self.cards_list[ind].change_mp(d_mn)

    def get_card(self, index):
        return self.cards_list[index]

    def place_card(self, card, index):
        self.cards_list[index] = card

    def remove_card(self, index):
        self.cards_list[index] = None