import pytest
from src.player import Player
from src.field import Field
from src.hand import Hand
from src.stack import Stack
from src.cards import *



f = Field([Unit('nikolaev', 'Николаев', 'PHYS', 11, 1, 14, []),
					 None,
					 Unit('nikolaev', 'Николаев', 'PHYS', 11, 2, 14, []),
					 Unit('nikolaev', 'Николаев', 'PHYS', 11, 3, 14, []),
					 PlayerUnit(99, 99, 1),
					 Location('toilet', 'Центральный толкан', 'MATH', 20, 5, 13)])

h = Hand([Unit('nikolaev', 'Николаев', 'PHYS', 11, 1, 14, []),
			 None,
			 Unit('nikolaev', 'Николаев', 'PHYS', 11, 2, 14, []),
			 Unit('nikolaev', 'Николаев', 'PHYS', 11, 3, 14, []),
			 Location('toilet', 'Центральный толкан', 'MATH', 20, 5, 13)])

s = Stack([Unit('nikolaev', 'Николаев', 'PHYS', 11, 1, 14, []),
			 Unit('nikolaev', 'Николаев', 'PHYS', 11, 2, 14, []),
			 Unit('nikolaev', 'Николаев', 'PHYS', 11, 3, 14, []),
			 Location('toilet', 'Центральный толкан', 'MATH', 20, 5, 13)])

def test_init():
	p = Player(f,h,s)
	assert p.field == f
	assert p.stack == s
	assert p.hand == h

def test_get_card_dmg():
	p = Player(f,h,s)
	