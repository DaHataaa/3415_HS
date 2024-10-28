from field import Field

class Hand(Field):

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = [None] * 4