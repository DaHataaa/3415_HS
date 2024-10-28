import pytest
from src.stack import Stack
from src.cards import *



cards = [Unit('nikolaev', 'Николаев', 'PHYS', 11, 1, 14, []),
		 Unit('nikolaev', 'Николаев', 'PHYS', 11, 2, 14, []),
		 Unit('nikolaev', 'Николаев', 'PHYS', 11, 3, 14, []),
		 Location('toilet', 'Центральный толкан', 'MATH', 20, 5, 13)]


def test_init():
	s = Stack(cards)
	assert s.cards_list == cards

def test_get_top_card():
	s = Stack(cards)
	assert s.get_top_card() == cards[-1]


def test_push():
	s = Stack(cards)
	s.push(cards[0])
	assert s.cards_list[0] == cards[0]

def test_pop():
	s = Stack(cards)
	s2 = Stack(cards.copy())

	popped_element = s.pop()
	
	assert popped_element == s2.get_top_card() and popped_element != s.get_top_card()
