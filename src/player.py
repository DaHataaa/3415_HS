from cards import *
from enum import Enum

class Player:

    def __init__(self, max_mp, field, hand, stack):
        self.max_mp = max_mp
        self.field = field
        self.hand = hand
        self.stack = stack

    def play_card(self, i_from, i_to):
        mana_need = self.field[i_from].mn

        if mana_need <= self.field[PLAYER].mana:
            self.field[PLAYER].change_mana(-mana_need)
            self.field.place_card(self.hand[i_from],i_to)


    def play_item(self, i_from, i_to):
        mana_need = self.field[i_from].mn

        if mana_need <= self.field[PLAYER].mana:
            self.field[i_to].recieve_item(self.hand[i_from])



class Field:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = [None] * 6

    class FieldNames(Enum):
        UNIT1 = 0
        UNIT2 = 1
        UNIT3 = 2
        UNIT4 = 3
        LOCATION = 4
        PLAYER = 5


    def get_card(self, index):
        return self.cards_list[index]

    def place_card(self, card, index):
        self.cards_list[index] = card
            
    def remove_card(self, index):
        old_card = self.cards_list[index]
        self.cards_list[index] = None
        new_card = DECK[old_card.id].copy()
        return new_card


class Hand(Field):

    def __init__(self, cards_list = None):
        if cards_list == None:
            cards_list = [None] * 4


class Stack:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = []

    def get_top_card(self):
        return self.cards_list[-1]

    def push(self, card):
        self.cards_list.insert(0, card)

    def pop(self):
        return self.cards_list.pop()


