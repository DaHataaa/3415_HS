import json
import random


cards_repo = "cards/"
errs = dict()
errs["W-DF"] = ["WARN - DifFract"]

#################################################

class Player:

    def __init__(self, p_id, hp, mp, stack):
        self.hp = hp
        self.mp = mp
        self.stack = Stack(stack, {})
        self.hand = Hand(stack[:4])
        self.field = Field("", ["","","",""])
        self.p_id = p_id
        self.e_id = 3 - p_id

    def get_dmg(self, dmg):
        self.hp -= dmg

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


class Stack(Player):

    def __init__(self, cards_in_game: dict, picked_stack: dict):
        self.cing = cards_in_game
        self.p_stack = picked_stack

    def pop_card(self, card):
        super().hand.h_deck.pop(card.name)
        self.cing[card.name] = card
        
    def add_card(self):
        if self.cing != super().stack:
            added_c = random.choice(super().stack - self.cing)
            super().hand.h_deck.append(added_c)
            self.cing[added_c.name] = added_c
        else:
            print('Все доступные карты уже в игре. На руки не выдаются новые.')#nr


class Field(Player):

    def __init__(self, location_part, unit_part):
        self.unit_part = unit_part
        self.loc_part = location_part

    def place_unit(self, slot, card):
        if self.unit_part[slot] == "":
            self.unit_part[slot] = card
            super().mp -= card.mn
            super().stack.pop_card(card)
        else:
            print("Здесь уже есть юнит!")
            
    def kill_unit(self, card):
        super().stack.cing.pop(card.name)
        self.unit_part[self.unit_part.index(card)] = ""


class Hand(Player):

    def __init__(self, h_deck):
        self.h_deck = h_deck

    def play_card(self, card, slot):
        if super().mp >= card.mn:
            match type(card):
                case Unit:
                    Field.place_unit(slot, card)
                
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
        
    def get_dmg(self, dmg, player):
        self.hp -= dmg
        if self.hp <= 0:
           player.field.kill_unit(self)


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

#################################################

cards_e, cards_list = load_cards(cards_repo)
cards_p = cards_e
deck = [cards_e[cards_list[i]] for i in range(8)]


players = {"p1" : Player(1, 50, 50, deck), "p2" : Player(2, 50, 50, deck)}