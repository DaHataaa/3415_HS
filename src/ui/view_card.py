import pygame

from src.card import Card
from src.resource import RESOURCE as res


class ViewCard:
    WIDTH = res["card_width"]
    HEIGHT = res["card_height"]
    SELECT_ADD_SIZE = res["select_add_size"]
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
        if self.selected:
        	w = ViewCard.WIDTH + ViewCard.SELECT_ADD_SIZE
        	h = ViewCard.HEIGHT + ViewCard.SELECT_ADD_SIZE

        	add = ViewCard.SELECT_ADD_SIZE // 2
        	img_to_draw = pygame.transform.scale(img, (w,h))
        else:
        	img_to_draw = img
        	add = 0

        display.blit(img_to_draw, (self.x - add, self.y - add))

    def event_processing(self, event):
        1


class move:
    def __init__(self, vcard):
        self.vcard = vcard
        self.pos_from = (0, 0)
        self.pos_to = (0, 0)
        self.ticks_need = 0
