from src.player import *


class GameState:
    def __init__(self, p1=None, p2=None):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()

    def desk_created(self):
        self.defender.change_mana(4, 3)  # Возможно нужно что-то добавить

    def attack(self, i_from, i_to):
        if self.defender.can_play_card(i_from, i_to):
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
        (self.defender.change_mana(4, 3)) if is_skipped else 1
        self.swap_players()
