from enum import Enum


class Field:

    class FieldNames(Enum):
        UNIT1 = 0
        UNIT2 = 1
        UNIT3 = 2
        UNIT4 = 3
        PLAYER = 4
        LOCATION = 5

    def __init__(self, cards_list=None):
        if cards_list == None:
            self.cards_list = [None] * len(FieldNames)
        else:
            self.cards_list = cards_list

    def __eq__(self, other):
        for i in range(len(self.cards_list)):


            if self.cards_list[i] != other.cards_list[i]:
                return False
        return True

    def get_card(self, index):
        return self.cards_list[index]

    def place_card(self, card, index):
        self.cards_list[index] = card

    def remove_card(self, index):
        self.cards_list[index] = None