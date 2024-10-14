from player import*
from cards import*

class GameServer:
	def __init__(self,players):
		self.players = players
		self.turn = 0


	def attack(self, i_from, i_to):
		self.players[self.turn^1].field[i_to].recieve_dmg(self.players[self.turn].field[i_from].dmg)


	def play_card(self, i_from, i_to):
		self.players[self.turn].play_card(i_from, i_to)


	def play_item(self, i_from, i_to):
		self.players[self.turn].play_item(i_from, i_to)


	def swap(self):
		self.turn ^= 1


	def next_turn(self):
		self.swap()

		self.players[self.turn].recieve_mana()
