from enum import Enum
from typing import Type

from src.cards import *
from src.field import Field, FieldNames
from src.hand import Hand
from src.stack import Stack
from src.players.cli import CLI



class Player:

    def __init__(
        self,
        field: Field | None = None,
        hand: Hand | None = None,
        stack: Stack | None = None
    ):
        self.field = field if field is not None else Field()
        self.hand = hand if hand is not None else Hand()
        self.stack = stack if stack is not None else Stack()
        self.cli = CLI()

    def form_hand(self):
        self.hand.cards_list = self.cli.choose_cards()

    def get_hand(self):
        return self.hand

    def push_to_stack(self, card):
        self.stack.push(card)

    def remove_from_field(self, index):
        self.field.remove_card(index)

    def get_card_dmg(self, index):
        return self.field.get_card(index).get_dmg()

    def get_card_hp(self, index):
        return self.field.get_card(index).get_hp()

    def change_card_hp(self, index, d_hp):
        self.field.cards_list[index].change_hp(d_hp)

    def change_mana(self, index, d_mhp):
        self.field.change_mp(index, d_mhp)

    def change_card_dmg(self, index, d_dmg):
        self.field.cards_list[index].change_dmg(d_dmg)
        if self.get_card_hp(index) <= 0:
            for item in self.field.cards_list[index].items:
                self.push_to_stack(item)

            self.push_to_stack(self.field.cards_list[index])
            self.remove_from_field(index)

    def can_be_attacked(self, i_to):
        return bool(self.field.get_card(i_to))


    def can_play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)
        card_to = self.field.get_card(i_to)

        if card_from is None:
            return False
        if self.men_hp < card_from.mn:
            return False

        if isinstance(card_from, Location):
            return i_to == FieldNames.LOCATION and card_to is None
        elif isinstance(card_from, Unit):
            return i_to < FieldNames.PLAYER and card_to is None
        elif isinstance(card_from, Item):
            return (
                i_to < FieldNames.PLAYER
                and not (card_to is None)
                and i_to.can_recieve_item(card_from)
            )
        elif isinstance(card_from, Event):
            pass

        return False

    def play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)

        self.hand.remove_card(i_from)
        self.hand.place_card(self.stack.pop(), i_from)

        if self.field.get_card(i_to) == None:
            self.field.place_card(card_from, i_to)
        else:
            self.field.cards_list[i_to].recieve_item(card_from)

        self.field.cards_list[FieldNames.PLAYER].change_mana(-card_from.mn)
