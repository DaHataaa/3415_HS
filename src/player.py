from enum import Enum
from typing import Type

from cards import *
from field import Field, FieldNames
from hand import Hand
from stack import Stack
from players.cli import CLI
from random import choice



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

    def form_stack(self):
        self.stack.cards_list, self.stack.cards_origins = self.cli.choose_cards()

    def form_hand(self):
        for i in range(len(self.hand.cards_list)):
            if self.hand.cards_list[i] is None:
                self.hand.cards_list[i] = self.stack.get_top_card()
                self.stack.pop()

    def get_cIDed(self, ind_in_hand):
        return self.stack.cards_origins[self.hand.get_card(ind_in_hand)]
    
    def get_card_info(self, area, index):
        card = (self.hand if area == 1 else self.field).get_card(index)

        if card is not None: return card.__dict__
        else: return 'Карта отсутствует'

    def get_hand(self):
        return self.hand
    
    def get_field(self):
        return self.field

    def push_to_stack(self, card):
        self.stack.push(card)

    def remove_from_field(self, index):
        self.stack.push(self.field.get_card(index))
        self.field.remove_card(index)

    def get_card_dmg(self, index):
        return self.field.get_card(index).dmg

    def get_card_hp(self, index):
        return self.field.get_card(index).hp
    
    def get_pl_hp(self):
        return self.field.cards_list[FieldNames.PLAYER]

    def change_card_hp(self, index, d_hp):
        self.field.cards_list[index].change_hp(d_hp)

    def kill_check(self, index):
        if (not self.field.get_card(index).check_hp() if self.field.get_card(index) is not None else False):
            self.remove_from_field(index)
            return True
        else: return False

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
        return self.field.get_card(i_to) is not None


    def can_play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)
        card_to   = self.field.get_card(i_to)

        if card_from is None:
            return False
        if self.field.cards_list[FieldNames.PLAYER].mn < card_from.mn:
            return False

        if isinstance(card_from, Location):
            return i_to == FieldNames.LOCATION #and card_to is None
        elif isinstance(card_from, Unit):
            return i_to < FieldNames.PLAYER and card_to is None
        elif isinstance(card_from, Item):
            return (
                i_to < FieldNames.PLAYER
                and card_to is not None
                and card_to.can_recieve_item(card_from)
            )
        elif isinstance(card_from, Event):
            pass

        return False

    def play_card(self, i_from, i_to):
        card_from = self.hand.get_card(i_from)
        card_to   = self.field.get_card(i_to)

        if isinstance(card_from, Unit):
            self.field.place_card(card_from, i_to)
        elif isinstance(card_from, Item):
            card_to.recieve_item(card_from)
        elif isinstance(card_from, Location):
            self.field.place_card(card_from, i_to)
            for card in self.field.cards_list[:FieldNames.PLAYER]:
                if card is None: continue
                if card_from.fract == card.fract:
                    card.change_dmg(self, card_from.dmg_boost)
                    card.change_hp(self, card_from.hp_boost)
        elif isinstance(card_from, Event):
            pass

        self.field.cards_list[FieldNames.PLAYER].change_mp(-card_from.mn)
        self.hand.remove_card(i_from)
