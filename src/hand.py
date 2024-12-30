from field import Field
from players.players_stats import stats


class Hand(Field):
    def __init__(self, cards_list: list | None = None):
        self.cards_list = cards_list if cards_list != None else [None] * stats['hand_size']

    def __repr__(self):
        return self.cards_list

    def __str__(self):
        return ' '.join(map(str,self.cards_list))
    
    def remove_card(self, index):
        self.cards_list[index] = None

    def get_card(self, index):
        return self.cards_list[index]