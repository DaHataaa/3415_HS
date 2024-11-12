import pytest
from src.hand import Hand
from src.cards import *


cards = [
    Unit("nikolaev", "Николаев", "PHYS", 11, 1, 14, []),
    None,
    Unit("nikolaev", "Николаев", "PHYS", 11, 2, 14, []),
    Unit("nikolaev", "Николаев", "PHYS", 11, 3, 14, []),
    Location("toilet", "Центральный толкан", "MATH", 20, 5, 13),
]


def test_init():
    h = Hand(cards)
    assert h.cards_list == cards


def test_get_card():
    h = Hand(cards)
    assert h.get_card(0) == cards[0]


def test_place_card():
    h = Hand(cards)
    h.place_card(cards[0], 0)
    assert h.get_card(0) == cards[0]


def test_remove_card():
    h = Hand(cards)
    h.remove_card(0)
    assert h.get_card(0) == None
