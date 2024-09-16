import json





cards_repo = '../cards/'





class Card:

    def __init__(self,CLASS,name,fract,MN):
        self.CLASS = CLASS
        self.name = name
        self.fract = fract
        self.MN = MN




class Unit(Card):

    def __init__(self,CLASS,name,fract,MN,DMG,HP):
        Card.__init__(self,CLASS,name,fract,MN)
        self.DMG = DMG
        self.HP = HP


class Item(Card):

    def __init__(self,CLASS,name,fract,MN,DMG_BOOST,HP_BOOST):
        Card.__init__(self,CLASS,name,fract,MN)
        self.DMF_BOOST = DMF_BOOST
        self.HP_BOOST = HP_BOOST


class Location(Card):

    def __init__(self,CLASS,name,fract,MN,DMG_BOOST,HP_BOOST):
        Card.__init__(self,CLASS,name,fract,MN)
        self.DMF_BOOST = DMF_BOOST
        self.HP_BOOST = HP_BOOST


class Event(Card):

    def __init__(self,CLASS,name,MN):
        Card.__init__(self,CLASS,name,fract,MN)



def load_cards(cards_repo):
    cards_list = open(cards_repo+'cards_list.txt').readlines()

    cards = dict()

    for i in range(len(cards_list)):
        card_id = cards_list[i].replace('\n','')

        f = json.load(open(cards_repo+card_id+'.json',encoding='utf8'))

        match f['class']:
            case 'unit':
                card = Unit(f['class'],f['name'],f['fract'],f['MN'],f['DMG'],f['HP'])
            case 'item':
                card = Item(f['class'],f['name'],f['fract'],f['MN'],f['DMG_BOOST'],f['HP_BOOST'])
            case 'location':
                card = Location(f['class'],f['name'],f['fract'],f['MN'],f['DMG_BOOST'],f['HP_BOOST'])
            case 'event':
                card = Event(f['class'],f['name'],f['MN'])

        cards[card_id] = card

    return cards



cards = load_cards(cards_repo)




