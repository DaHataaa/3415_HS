import json



cards_repo = '../cards/'

errs = dict()
errs['W-DF'] = ['WARN - DifFract']



class Card:

    def __init__(self, ID, CLASS, name, fract, MN):
        self.ID = ID
        self.CLASS = CLASS
        self.name = name
        self.fract = fract
        self.MN = MN




class Unit(Card):

    def __init__(self, ID, CLASS, name, fract, MN, DMG, HP):
        Card.__init__(self, ID, CLASS, name, fract, MN)
        self.DMG = DMG
        self.HP = HP
        self.items = []

    def add_item(self, item):
        if item.fract == self.fract:
            self.items.append(item)
            self.HP += item.HP_BOOST
            self.DMG += item.DMG_BOOST

            return True
        else:
            return False


class Item(Card):

    def __init__(self, ID, CLASS, name, fract, MN, DMG_BOOST, HP_BOOST):
        Card.__init__(self, ID, CLASS, name, fract, MN)
        self.DMG_BOOST = DMG_BOOST
        self.HP_BOOST = HP_BOOST


class Location(Card):

    def __init__(self, ID, CLASS, name, fract, MN, DMG_BOOST, HP_BOOST):
        Card.__init__(self, ID, CLASS, name, fract, MN)
        self.DMG_BOOST = DMG_BOOST
        self.HP_BOOST = HP_BOOST


class Event(Card):

    def __init__(self, ID, CLASS, name, fract, MN):
        Card.__init__(self, ID, CLASS, name, fract, MN)



def load_cards(cards_repo):
    cards_list = open(cards_repo+'cards_list.txt').readlines()

    cards = dict()

    for i in range(len(cards_list)):
        cards_list[i] = cards_list[i].replace('\n','')
        card_id = cards_list[i]

        f = json.load(open(cards_repo+card_id+'.json',encoding='utf8'))

        match f['class']:
            case 'unit':
                card = Unit(card_id,f['class'],f['name'],f['fract'],f['MN'],f['DMG'],f['HP'])
            case 'item':
                card = Item(card_id,f['class'],f['name'],f['fract'],f['MN'],f['DMG_BOOST'],f['HP_BOOST'])
            case 'location':
                card = Location(card_id,f['class'],f['name'],f['fract'],f['MN'],f['DMG_BOOST'],f['HP_BOOST'])
            case 'event':
                card = Event(card_id,f['class'],f['name'],f['fract'],f['MN'])

        cards[card_id] = card

    return cards,cards_list


class Field:
    def __init__(self, upper_part, lower_part):
        self.upper_part = upper_part
        self.lower_part = lower_part

    def place_a_card(self, slot, card):
        self.lower_part[slot] = card


class Player:
    def __init__(self, HP, MP, deck):
        self.HP = HP
        self.MP = MP
        self.stack = deck
        self.hand = ['']*4
        for i in range(4):
            self.hand[i] = self.pop_from_stack()
            

    def pop_from_stack(self):
        return self.stack.pop()

    def add_to_stack(self, card):
        self.stack = [card] + self.stack

    
    def play_a_card(self, field, ifrom, ito):
        cfrom = self.hand[ifrom]
        if cfrom != '':
            if cfrom.CLASS == 'unit':
                if field.lower_part[ito] == '':
            
                    field.place_a_card(ito,cfrom)
                else:
                    pass

                    
            elif cfrom.CLASS == 'item':
                cto = field.lower_part[ito]
                if cto.add_item(cfrom) and self.MP >= cfrom.MN:
                    self.MP -= cfrom.MN

            self.hand[ifrom] = self.pop_from_stack()


    


cards_e,cards_list = load_cards(cards_repo)
cards_p = cards_e

f = Field(['','','',''],['','','',''])


deck = []


for i in range(8):
    deck.append(cards_e[cards_list[i]])


f = Field(['','','',''],['','','',''])

p1 = Player(50,50,deck)