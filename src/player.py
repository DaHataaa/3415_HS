from cards import *
from enum import Enum

from field import Field
from hand import Hand
from stack import Stack



class Player:

    def __init__(self, field, hand, stack):
        self.field = field
        self.hand = hand
        self.stack = stack

    def get_card_dmg(self, index):
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
            if (
                i_to < Field.FieldNames.PLAYER
                and card_to != None
                and card_to.fract == card_from.fract
            ):
                return True
        elif isinstance(card_from, Event):
            1

        return False

    def play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)

        self.hand.remove_card(i_from)
        self.hand.place_card(self.stack.pop())

        if self.field.get_card(i_to) == None:
            self.field.place_card(card_from, i_to)
        else:
            self.field.cards_list[i_to].recieve_item(card_from)

        self.field.cards_list[PLAYER].change_mana(-card_from.mn)