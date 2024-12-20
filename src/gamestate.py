from src.player import *
from src.resource import RESOURCE as res
from enum import Enum
from src.field import Field as field


class GameState:
    def __init__(self, p1=None, p2=None):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()

    def desk_created(self):
        self.defender.change_mana(field.PLAYER, res['mana_add_per_turn'])  # Возможно нужно что-то добавить

    def attack(self, i_from, i_to):
        if self.defender.can_be_attacked(i_to):
            self.defender.change_card_hp(-self.attacker.get_card_dmg(i_from))
            self.defender  # Вроде надо проверку на ent_kill сделать
            return True
        return False  # По факту функция должна также возвращать состояние атаки(возможно переделать в gameserver)

    def play_card(self, i_from, i_to):
        if self.attacker.can_play_card(i_from, i_to):
            self.attacker.play_card(i_from, i_to)

    def swap_players(self):
        self.attacker, self.defender = self.defender, self.attacker

    def next_turn(self, is_skipped):
        self.defender.change_mana(field.PLAYER, res['mana_add_per_turn'])
        self.swap_players()
