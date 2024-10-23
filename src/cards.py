import json


class Card:

    def __init__(self, id, name, fract, mn):
        self.id = id
        self.name = (name,)
        self.fract = (fract,)
        self.mn = mn

    @classmethod
    def load(cls, file):
        return cls(id=file["id"], name=file["name"], fract=file["fract"], mn=file["mn"])

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

    def recieve_item(self, item):
        if item.fract != self.fract:
            return False
        self.items.append(item)
        self.hp += item.hp_boost
        self.dmg += item.dmg_boost
        return True

    def change_dmg(self, d_dmg):
        self.dmg += d_dmg

    def change_hp(self, d_hp):
        self.hp += d_hp

    def get_dmg(self):
        return self.dmg

    def get_hp(self):
        return self.hp


class Item(Card):

    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

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


class Location(Card):
    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

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
    def __init__(self, hp, mp, mana_delta):
        Unit.__init__(self)
        self.hp = hp
        self.mana = mp
        self.mana_delta = mana_delta

    @classmethod
    def load(cls, file):
        # return cls() !? чё с init-ом тут творится
        pass

    def change_mana(self, dm=self.mana_delta):
        self.mana += dm
