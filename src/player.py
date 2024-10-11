from cards import *

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
            cards_list = [None] * 5

    def get_card(self, index):
        return self.cards_list[index]

    def get_card_index(self, card):
        return self.cards_list.index(card)

    def place_card(self, card, index):
        self.cards_list[index] = card
            
    def remove_card(self, card):
        self.cards_list[self.get_card_index(card)] = None


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


