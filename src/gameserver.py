from player import*
from cards import*

class GameServer:
	def __init__(self,p1,p2):
		self.atacker = p1
		self.defender = p2


	def attack(self, i_from, i_to):
		self.defender.change_card_hp(self.attacker.field[i_from].dmg)


	def play_card(self, i_from, i_to):
		self.attacker.play_card(i_from, i_to)


	def swap(self):
		self.turn ^= 1


	def next_turn(self):
		self.defender.change_mana()

		self.attacker, self.defender = self.defender, self.attacker
