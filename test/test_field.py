import pytest
from src.field import Field
from src.cards import *



cards = [Unit('nikolaev', 'Николаев', 'PHYS', 11, 5, 14, []),
		 None,
		 Item('ram', 'Плашка оперативы', 'EVM', 12, 5, 2),
		 Location('toilet', 'Центральный толкан', 'MATH', 20, 5, 13)]

def test_init():
	f = Field(cards)
	assert f.cards_list == cards

#def test_get_card():
