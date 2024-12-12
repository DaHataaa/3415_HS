import pygame

from src.card import Card
from src.resource import RESOURCE as res
from view_card import ViewCard as vcard


class ViewHand:
    def __init__(self, player):
        self.hand = player.get_hand()

    def redraw(self, side, display):
        if side == "defender":
            y = 100
        elif side == "attacker":
            y = res["height"] - 100
        for i in range(4):
            card = vcard(self.hand.get_card(i), i * 80, y)
            card.redraw(display)
