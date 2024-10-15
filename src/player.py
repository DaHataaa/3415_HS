from cards import *
from enum import Enum

class Player:

    def __init__(self, max_mp, field, hand, stack):
        self.max_mp = max_mp
        self.field = field
        self.hand = hand
        self.stack = stack


    def change_card_hp(self, index, d_hp):
        self.field[index].change_card_hp(d_hp)

    def change_card_dmg(self, index, d_dmg):
        self.field[index].change_card_dmg(d_dmg)


    def play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)
        if card_from == None:
            return 1
        
        mana_need = card_from.mn
        is_location = isinstance(card_from, Location)
        if is_location^1:
            is_item = isinstance(card_from, Item)
            if is_item^1:
                is_unit = isinstance(card_from, Unit)

        if mana_need <= self.field[PLAYER].mana:
            return 1

        condition_location = is_location and i_to == Field.FieldNames.LOCATION
        condition_to_first4 = i_to < Field.FieldNames.PLAYER
        condition_unit = is_unit and condition_to_first4
        condition_free_space = self.field.get_card(i_to) == None

        if condition_free_space:
            allow_placing = condition_location or condition_unit
        elif is_item and condition_to_first4:
            card_to = self.field.get_card(i_to)
            allow_equipping = card_to.fract == card_from.fract

        
        if allow_placing:
            self.hand.remove_card(i_from)
            self.hand.place_card(self.stack.pop())
            self.field.place_card(card_from,i_to)

            self.field[PLAYER].change_mana(-mana_need)


        elif allow_equipping:
            self.field[i_to].recieve_item(card_from)


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
        return self.cards_list.pop()


