from src.field import Field


class Hand(Field):
    def __init__(self, cards_list: list | None = None):
        self.cards_list = cards_list
        if self.cards_list == None:
            self.cards_list = [None] * 4
