from src.field import Field

class Hand(Field):

    def __init__(self, cards_list=None):
        if cards_list == None:
            self.cards_list = [None] * 4
        else:
        	self.cards_list = cards_list