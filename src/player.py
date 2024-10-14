from cards import *
from enum import Enum

class Player(Card):

    def __init__(self, hp, mp, max_mp, field, hand, stack):
        self.hp = hp
        self.mp = mp
        self.max_mp = max_mp
        self.field = field
        self.hand = hand
        self.stack = stack

    def change_hp(self, delta_hp):
        self.hp += delta_hp

    def change_mp(self, delta_mp):
        self.mp += delta_mp


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


