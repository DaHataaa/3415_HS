import json
from src.players.players_stats import stats as s


class Card:

    def __init__(self, id, name, fract, mn):
        self.id = id
        self.name = name
        self.fract = fract
        self.mn = mn

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.fract == other.fract
            and self.mn == other.mn
        )

    @classmethod
    def load(cls, file):
        return cls(id=file["id"], name=file["name"], fract=file["fract"], mn=file["mn"])


class Item(Card):

    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    def __eq__(self, other):
        return (
            Card.__eq__(self, other)
            and self.dmg_boost == other.dmg_boost
            and self.hp_boost == other.hp_boost
        )

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg_boost=file["dmg_boost"],
            hp_boost=file["hp_boost"],
        )


class Unit(Card):

    def __init__(self, id, name, fract, mn, dmg, hp, items):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg = dmg
        self.hp = hp
        self.items = items

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg=file["dmg"],
            hp=file["hp"],
            items=file["items"],
        )

    def can_recieve_item(self, item):
        return item.fract == self.fract

    def recieve_item(self, item: Item):
        self.items.append(item)
        self.hp += item.hp_boost
        self.dmg += item.dmg_boost

    def change_dmg(self, d_dmg):
        self.dmg += d_dmg

    def change_hp(self, d_hp):
        self.hp += d_hp

    def change_mp(self, d_mn):
        self.mn += d_mn


class Location(Card):
    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    def __eq__(self, other):
        return (
            Card.__eq__(self, other)
            and self.dmg_boost == other.dmg_boost
            and self.hp_boost == other.hp_boost
        )

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg_boost=file["dmg_boost"],
            hp_boost=file["hp_boost"],
        )


class Event(Card):
    def __init__(self, id, name, fract, mn):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)

    @classmethod
    def load(cls, file):
        return cls(id=file["id"], name=file["name"], fract=file["fract"], mn=file["mn"])


class PlayerUnit(Unit):
    def __init__(self, id = s['id'], name = s['name'], fract = s['fract'], mn = s['mn'], dmg = s['dmg'], hp = s['hp'], items = s['items']):
        self.id = id
        self.name = name
        self.fract = fract
        self.mn = mn
        self.dmg = dmg
        self.hp = hp
        self.items = items

    def __str__(self):
        return str(self.id)
    
    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg=file["dmg"],
            hp=file["hp"],
            items=file["items"],
        )

@staticmethod
def load_cards(cards_repo):
    cards_list = open(cards_repo + "cards_list.txt").readlines()
    cards = dict()

    for i in range(len(cards_list)):
        cards_list[i] = cards_list[i].replace("\n", "")
        f = json.load(open(cards_repo + cards_list[i] + ".json", encoding="utf8"))
        f["id"] = cards_list[i]

        lookup_table = {
            "unit": Unit.load,
            "item": Item.load,
            "location": Location.load,
            "event": Event.load,
        }

        card = lookup_table[f["class"]](f)
        cards[cards_list[i]] = card

    return cards, cards_list
