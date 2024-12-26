from player import *
from players.players_stats import stats as res
from enum import Enum
from field import Field, FieldNames


class GameState:
    def __init__(self, p1=None, p2=None):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()
        self.skipped_turn = True


    def update_hand(self, player: Player):
        player.form_hand()

    def deck_created(self):
        self.defender.form_stack()
        self.defender.form_hand()
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

    def next_turn(self):
        self.defender.change_mana(FieldNames.PLAYER, res['mana_add_per_turn'])
        self.attacker.change_mana(FieldNames.PLAYER, res['mana_add_per_turn']*(2 if self.skipped_turn else 1))
        self.skipped_turn = True
        self.swap_players()

    def card_info(self, area, index):
        return (self.attacker if area in (1, 2) else self.defender).get_card_info(area, index)