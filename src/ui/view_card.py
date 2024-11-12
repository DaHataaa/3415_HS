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


	@property
	def card(self):
		return self.__card


	@card.setter
	def card(self, value):
		if not isinstance(value, Card):
			raise TypeError(f'NOT A CARD! {type(value)} GIVEN!')
		self.__card = value
		img = pygame.image.load(f'img/{self.card.id}.png')

		self.img_front = pygame.transform.scale(img, (ViewCard.WIDTH, ViewCard.HEIGHT))


	def select(self):
		self.selected = not self.selected

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
