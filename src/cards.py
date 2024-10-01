import json
import random


cards_repo = "../cards/"

#################################################


class Player:

    def __init__(self, hp, mp, field, hand, stack):
        self.hp = hp
        self.mp = mp
        self.field = field
        self.hand = hand
        self.stack = stack

    def change_hp(self, delta_hp):
        self.hp += delta_hp

    def change_dmg(self, delta_dmg):
        self.dmg += delta_dmg

    """
    def attack_with_a_unit(self, pl_slot, en_slot):
        dmg_to_en = self.field.unit_part[pl_slot].dmg
        en = players["p"+str(self.e_id)]
        match en_slot:
            case 0:
                if en.field.unit_part[pl_slot] == "":
                    en.get_dmg(dmg_to_en)
                else:
                    print("Перед игроком стоит преграда!")
            case _:
                en.field.unit_part[en_slot].get_dmg(dmg_to_en)
    """


class Field:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = [None] * 5
        self.cards_list = cards_list

    def get_card(self, index):
        return self.cards_list[index]

    def place_card(self, card, index):
        self.cards_list[index] = card

    def remove_card(self, index):
        self.cards_list[index] = None


class Hand(Field):

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = [None] * 4
        self.cards_list = cards_list


class Stack:

    def __init__(self, cards_list=None):
        if cards_list == None:
            cards_list = []
        self.cards_list = cards_list

    def get_card(self):
        return self.cards_list[-1]

    def push(card):
        self.cards_list.insert(0, card)

    def pop():
        return self.cards_list.pop()


#################################################


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

    def place_item(self, item):
        if item.fract == self.fract:
            self.items.append(item)
            self.hp += item.hp_boost
            self.dmg += item.dmg_boost
            return True
        else:
            return False

    # def get_dmg(self, dmg, player):
    # self.hp -= dmg
    # if self.hp <= 0:
    # player.field.kill_unit(self)


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


#################################################

cards_e, cards_list = load_cards(cards_repo)
cards_p = cards_e
deck = [cards_e[cards_list[i]] for i in range(8)]
