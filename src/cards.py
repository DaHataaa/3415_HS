import json

cards_repo = "../cards/"

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


class Field:
    def __init__(self, upper_part, lower_part):
        self.upper_part = upper_part
        self.lower_part = lower_part

    def place_a_card(self, slot, card):
        self.lower_part[slot] = card


class Player:
    def __init__(self, hp, MP, deck):
        self.hp = hp
        self.MP = MP
        self.stack = deck
        self.hand = [""] * 4
        for i in range(4):
            self.hand[i] = self.pop_from_stack()

    def pop_from_stack(self):
        return self.stack.pop()

    def add_to_stack(self, card):
        self.stack = [card] + self.stack

    def play_a_card(self, field, ifrom, ito):
        cfrom = self.hand[ifrom]
        if cfrom != "":
            if cfrom.CLASS == "unit":
                if field.lower_part[ito] == "":

                    field.place_a_card(ito, cfrom)
                else:
                    pass

            elif cfrom.CLASS == "item":
                cto = field.lower_part[ito]
                if cto.add_item(cfrom) and self.MP >= cfrom.mn:
                    self.MP -= cfrom.mn

            self.hand[ifrom] = self.pop_from_stack()


cards_e, cards_list = load_cards(cards_repo)
cards_p = cards_e

f = Field(["", "", "", ""], ["", "", "", ""])


deck = []


for i in range(8):
    deck.append(cards_e[cards_list[i]])


f = Field(["", "", "", ""], ["", "", "", ""])

p1 = Player(50, 50, deck)
