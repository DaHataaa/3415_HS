import json


cards_repo = "../cards/"

#################################################

class Player(Card):

    def __init__(self, hp, mp, max_mp, field, hand, stack):
        self.hp = hp
        self.mp = mp
        self.max_mp = max_mp
        self.field = field
        self.hand = hand
        self.stack = stack

    def change_hp(self, delta_hp):
        self.hp += delta_hp

    def change_mp(self, delta_mp):
        self.mp += delta_mp


class Field:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = [None] * 5

    def get_card(self, index):
        return self.cards_list[index]

    def get_card_index(self, card):
        return self.cards_list.index(card)

    def place_card(self, card, index):
        self.cards_list[index] = card
            
    def remove_card(self, card):
        self.cards_list[self.get_card_index(card)] = None


class Hand(Field):

    def __init__(self, cards_list = None):
        if cards_list == None:
            cards_list = [None] * 4


class Stack:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = []

    def get_top_card(self):
        return self.cards_list[-1]

    def push(self, card):
        self.cards_list.insert(0, card)

    def pop(self):
        return self.cards_list.pop()


#################################################
            

class Card:

    def __init__(self, f):
        id=f.["id"],
        name=f["name"],
        fract=f["fract"],
        mn=f["mn"]

    @staticmethod
    def load_cards(cards_repo):
        cards_list = open(cards_repo + "cards_list.txt").readlines()
        cards = dict()

        for i in range(len(cards_list)):
            cards_list[i] = cards_list[i].replace("\n", "")
            card_id = cards_list[i]
            f = json.load(open(cards_repo + card_id + ".json", encoding="utf8"))
            
            lookup_table = {
                "unit": Unit.load,
                "item": Item.load,
                "location": Location.load,
                "event": Event.load,
                            }

            card = lookup_table[f["class"]](f)
            cards[card_id] = card

        return cards, cards_list


class Unit(Card):

    def __init__(self, f):
        Card.__init__(self, f)
        self.dmg = f["dmg"]
        self.hp = f["hp"]
        self.items = []


    def place_item(self, item):
        if item.fract != self.fract:
            return False
        self.items.append(item)
        self.hp += item.hp_boost
        self.dmg += item.dmg_boost
        return True
        
    def recieve_dmg(self, dmg) -> bool:
        self.hp -= dmg
        if self.hp <= 0:
            return True
        return False


class Item(Card):

    def __init__(self, f):
        Card.__init__(self, f)
        self.dmg_boost = f["dmg_boost"]
        self.hp_boost = f["hp_boost"]


class Location(Card):
    def __init__(self, f):
        Card.__init__(self, f)
        self.dmg_boost = f["dmg_boost"]
        self.hp_boost = f["hp_boost"]


class Event(Card):
    def __init__(self, f):
        Card.__init__(self, f)



