import pygame

from src.card import Card
from src.resource import RESOURCE as res
from view_card import ViewCard as vcard


class ViewHand:
	def __init__(self, player):
		self.hand = player.get_hand()


	def redraw(self, side, display):
		for i in range(4):
			card = vcard(self.hand.get_card(i),i*80,res["height"]-100)
			card.redraw(display)
