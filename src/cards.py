import json
         
class Card:

    def __init__(self, f):
        id=f["id"],
        name=f["name"],
        fract=f["fract"],
        mn=f["mn"]

    @staticmethod
    def load_cards(cards_repo):
        cards_list = open(cards_repo + "cards_list.txt").readlines()
        cards = dict()

        for i in range(len(cards_list)):
            cards_list[i] = cards_list[i].replace("\n", "")
            f = json.load(open(cards_repo + cards_list[i] + ".json", encoding="utf8"))
            f["id"] = cards_list[i]
            
            lookup_table = {
                "unit": Unit,
                "item": Item,
                "location": Location,
                "event": Event,
                            }

            card = lookup_table[f["class"]](f)
            cards[cards_list[i]] = card

        return cards, cards_list


class Unit(Card):

    def __init__(self, f):
        Card.__init__(self, f)
        self.dmg = f["dmg"]
        self.hp = f["hp"]
        self.items = []


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

class PlayerUnit(Unit):
    def __init__(self, hp, mp, mana_delta):
        Unit.__init__(self)
        self.hp = hp
        self.mana = mp
        self.mana_delta = mana_delta

    def change_mana(self, dm = self.mana_delta):
        self.mana += dm





