from cards import *

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


