import pytest
from src.field import Field
from src.cards import *


cards = [
    Unit("nikolaev", "Николаев", "PHYS", 11, 1, 14, []),
    None,
    Unit("nikolaev", "Николаев", "PHYS", 11, 2, 14, []),
    Unit("nikolaev", "Николаев", "PHYS", 11, 3, 14, []),
    PlayerUnit(99, 99, 1),
    Location("toilet", "Центральный толкан", "MATH", 20, 5, 13),
]


def test_init():
    f = Field(cards)
    assert f.cards_list == cards


def test_get_card():
    f = Field(cards)
    assert f.get_card(0) == cards[0]


def test_place_card():
    f = Field(cards)
    f.place_card(cards[0], 0)
    assert f.get_card(0) == cards[0]


def test_remove_card():
    f = Field(cards)
    f.remove_card(0)
    assert f.get_card(0) == None
