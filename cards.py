import json
import random

cards_repo = "cards/"
errs = dict()
errs["W-DF"] = ["WARN - DifFract"]


class Card:

    def __init__(self, id, name, fract, mn):
        self.id = id
        self.name = name
        self.fract = fract
        self.mn = mn

    @staticmethod
    def load(obj, file):
        obj.name = file["name"]
        obj.fract = file["fract"]
        obj.mn = file["mn"]


class Unit(Card):

    def __init__(self, id, name, fract, mn, dmg, hp):
        Card.__init__(self, id, name, fract, mn)
        self.dmg = dmg
        self.hp = hp
        self.items = []

    @classmethod
    def load(cls, file):
        obj = cls.__new__(cls)
        super().load(obj, file)
        obj.dmg = file["dmg"]
        obj.hp = file["hp"]
        obj.items = []
        return obj

    def add_item(self, item):
        if item.fract == self.fract:
            self.items.append(item)
            self.hp += item.hp_boost
            self.dmg += item.dmg_boost
            return True
        else:
            return False


class Item(Card):

    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id, name, fract, mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    @classmethod
    def load(cls, file):
        obj = cls.__new__(cls)
        super().load(obj, file)
        obj.dmg_boost = file["dmg_boost"]
        obj.hp_boost = file["hp_boost"]
        return obj


class Location(Card):

    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id, name, fract, mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    @classmethod
    def load(cls, file):
        obj = cls.__new__(cls)
        super().load(obj, file)
        obj.dmg_boost = file["dmg_boost"]
        obj.hp_boost = file["hp_boost"]
        return obj


class Event(Card):

    def __init__(self, id, name, fract, mn):
        Card.__init__(self, id, name, fract, mn)

    @classmethod
    def load(cls, file):
        obj = cls.__new__(cls)
        super().load(obj, file)
        return obj


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

            
class Player:

    def __init__(self, hp, mp, stack):
        self.hp = hp
        self.mp = mp
        self.stack = Stack(stack, {}, )
        self.hand = Hand(self, stack[:4])

    def get_dmg(self, dmg):
        self.hp -= dmg#nr


class Stack(Player):

    def __init__(self, cards_in_game: dict, picked_stack: dict):
        self.cing = cards_in_game
        self.p_stack = picked_stack

    def pop_card(self, card: Card):
        super().hand.h_deck.pop(card.name)
        
    def add_card(self):
        if self.cing != super().stack:
            super().hand.h_deck.append(random.choice(super().stack - self.cing))
        else:
            print('Все доступные карты уже в игре. На руки не выдаются новые.')#nr


class Field(Player):

    def __init__(self, upper_part, lower_part):
        self.upper_part = upper_part
        self.lower_part = lower_part

    def place_unit(self, slot, card: Card):
        if self.lower_part[slot] == '':
            self.lower_part[slot] = card
            super().mp -= card.mn  
            super().stack.add_card()
            super().stack.pop_card(card)
        else:
            print("Здесь уже есть юнит")#nr


class Hand(Player):

    def __init__(self, owner, h_deck: dict):
        self.owner = owner
        self.h_deck = h_deck

    def play_card(self, card: Card, slot):
        if super().mp >= card.mn:
            match type(card):
                case Unit:
                    Field.place_unit(slot, card)#nr
                
            

cards_e, cards_list = load_cards(cards_repo)
cards_p = cards_e

f = Field(["", "", "", ""], ["", "", "", ""])
deck = [cards_e[cards_list[i]] for i in range(8)]


p1 = Player(50, 50, deck)
p2 = Player(50, 50, deck)
