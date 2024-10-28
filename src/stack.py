from enum import Enum



class Stack:

    def __init__(self, cards_list=None):
        if cards_list == None:
            self.cards_list = []
        else:
        	self.cards_list = cards_list

    def get_top_card(self):
        return self.cards_list[-1]

    def push(self, card):
        self.cards_list.insert(0, card)

    def pop(self):
        return self.cards_list.pop()  # todo: pop from empty stack!!!