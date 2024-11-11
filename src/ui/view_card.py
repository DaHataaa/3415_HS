import pygame

from src.card import Card
from src.resource import RESOURCE as res


class ViewCard:
    WIDTH = res["card_width"]
    HEIGHT = res["card_height"]
    SELECTED_COLOR = res["selected_color"]

    def __init__(self, card, x, y):
        self.card = card
        self.x = x
        self.y = y
        self.selected = False

    def redraw(self, display):
        1

    def event_processing(self, event):
        1

    def select(self):
        self.selected = not self.selected


class move:
    def __init__(self, vcard):
        self.vcard = vcard
        self.pos_from = (0, 0)
        self.pos_to = (0, 0)
        self.ticks_need = 0
