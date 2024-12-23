from src.player import *
from src.players.players_stats import stats as res
from enum import Enum
from src.field import Field, FieldNames


class GameState:
    def __init__(self, p1=None, p2=None):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()

    def deck_created(self):
        self.defender.change_mana(FieldNames.PLAYER, res['mana_add_per_turn'])
        self.defender.form_stack()
        self.defender.form_hand()
        self.attacker.change_mana(FieldNames.PLAYER, res['mana_add_per_turn'])
        self.attacker.form_stack()
        self.attacker.form_hand()

    def attack(self, i_from, i_to):
        if self.defender.can_be_attacked(i_to):
            self.defender.change_card_hp(i_to,-self.attacker.get_card_dmg(i_from))
                    

    def play_card(self, i_from, i_to):
        if self.attacker.can_play_card(i_from, i_to):
            self.attacker.play_card(i_from, i_to)
        else: 
            print('Карту не получается разыграть')

    def swap_players(self):
        self.attacker, self.defender = self.defender, self.attacker

    def next_turn(self, is_skipped):
        self.defender.change_mana(FieldNames.PLAYER, res['mana_add_per_turn'])
        self.swap_players()
