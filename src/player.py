from cards import *
from enum import Enum

class Player:

    def __init__(self, max_mp, field, hand, stack):
        self.max_mp = max_mp
        self.field = field
        self.hand = hand
        self.stack = stack


    def get_dmg(self, index):
        return self.field.get_card(index).get_dmg()


    def change_card_hp(self, index, d_hp):
        self.field[index].change_card_hp(d_hp)

    def change_card_dmg(self, index, d_dmg):
        self.field[index].change_card_dmg(d_dmg)
        


    def can_play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)
        card_to = self.hand.get_card(i_to)
        if card_from == None:
            return 1
        
        mana_need = card_from.mn

        if isinstance(card_from, Location):
            if i_to == Field.FieldNames.LOCATION and card_to == None:
                return True
        elif isinstance(card_from, Unit):
            if i_to < Field.FieldNames.PLAYER and card_to == None:
                return True
        elif isinstance(card_from, Item):
            if i_to < Field.FieldNames.PLAYER and card_to != None and card_to.fract == card_from.fract:
                return True
        elif isinstance(card_from, Event):
            1

        return False



    def play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)

        self.hand.remove_card(i_from)
        self.hand.place_card(self.stack.pop())

        if self.field.get_card(i_to) == None:
            self.field.place_card(card_from,i_to)
        else:
            self.field[i_to].recieve_item(card_from)


        self.field[PLAYER].change_mana(-card_from.mn)


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
            cards_list = [None] * len(FieldNames)
        


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
        return self.cards_list.pop() #todo: pop from empty stack!!!


