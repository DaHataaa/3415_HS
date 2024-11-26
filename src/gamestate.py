from src.player import *


class GameState:
    def __init__(self, p1, p2):
        self.attacker = p1
        if self.attacher == None:
            self.attacker = Player()

        self.defender = p2
        if self.defender == None:
            self.defender = Player

    def attack(self, i_from, i_to):
        self.defender.change_card_hp(-self.attacker.get_card_dmg(i_from))

    def play_card(self, i_from, i_to):
        if self.attacker.can_play_card(i_from, i_to):
            self.attacker.play_card(i_from, i_to)

    def swap_players(self):
        self.attacker, self.defender = self.defender, self.attacker

    def next_turn(self):
        self.defender.change_mana(defender.mana)
        self.swap_players()
