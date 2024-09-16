import json
import abc


class card:

    def __init__(self):
        pass

    def __str__(self):
        return self.name
    
    @abc.abstractmethod
    def write_card(self, adress, stats): #функция записи абстрактна и для каждого подкласса будет отличаться
        pass

    def read_card(self, id): #функция чтения едина, чтобы учитывать подкласс для класса карты(т.е. какой класс будет у самой карты)
        
        with open('../cards/'+id+'.json','r') as f:
            temp = json.load(f)

            match temp["Class"]:
                case "<class '__main__.CUnit'>":
                    globals()[id] = CUnit(temp["Name"],temp["MN"],temp["DMG"],temp["HP"],temp["FRACTION"]) #создаём динамичную глобальную переменную
                case "<class '__main__.CItem'>":
                    globals()[id] = CItem(temp["Name"],temp["MN"],temp["DMG_BOOST"],temp["HP_BOOST"],temp["FRACTION"],temp["SPECIFIC_UNIT"])
                case "<class '__main__.CPlace'>":
                    globals()[id] = CPlace(temp["Name"],temp["MN"],temp["DMG_BOOST"],temp["HP_BOOST"],temp["FRACTION"],temp["SPECIFIC_UNIT"],temp["TIMER"])
                case "<class '__main__.CEvent>":
                    globals()[id] = CEvent(temp["Name"],temp["MN"],temp["EVENT"],temp["SIDE"])
                case _:
                    print('Класса нет')


class CUnit(card):

    def __init__(self, name, mn, dmg, hp, fract):
        self.name = name
        self.mn = mn
        self.dmg = dmg
        self.hp = hp
        self.fract = fract
    
    def write_card(self, id): #Пример функции записи для класса карты Юнит
        with open('../cards/'+id+'.json','w') as f:
            json.dump({
                "Class": str(type(self)),
                "Name": self.name,
                "MN": self.mn,
                "DMG": self.dmg,
                "HP": self.hp,
                "FRACTION": self.fract},f)
    
        
class CItem(card):

    def __init__(self, name, mn, dmg_boost, hp_boost, fract, spec_unit):
        self.name = name
        self.mn = mn
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost
        self.fract = fract
        self.spec_unit = spec_unit
        
    def write_card(self, id):
        with open('../cards/'+id+'.json','w') as f:
            json.dump({
                "Class": str(type(self)),
                "Name": self.name,
                "MN": self.mn,
                "DMG_BOOST": self.dmg_boost,
                "HP_BOOST": self.hp_boost,
                "FRACTION": self.fract,
                "SPECIFIC_UNIT": self.spec_unit},f)
        
        
class CPlace(card):

    def __init__(self, name, mn, dmg_boost, hp_boost, fract, spec_unit, timer):
        self.name = name
        self.mn = mn
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost
        self.fract = fract
        self.spec_unit = spec_unit
        self.timer = timer
        
    def write_card(self, id):
        with open('../cards/'+id+'.json','w') as f:
            json.dump({
                "Class": str(type(self)),
                "Name": self.name,
                "MN": self.mn,
                "DMG_BOOST": self.dmg_boost,
                "HP_BOOST": self.hp_boost,
                "FRACTION": self.fract,
                "SPECIFIC_UNIT": self.spec_unit,
                "TIMER": self.timer},f)


class CEvent(card):

    def __init__(self, name, mn, event, side):
        self.name = name
        self.mn = mn
        self.event = event
        self.side = side
        
    def write_card(self, id):
        with open('../cards/'+id+'.json','w') as f:
            json.dump({
                "Class": str(type(self)),
                "Name": self.name,
                "MN": self.mn,
                "EVENT": self.event,
                "SIDE": self.side},f)


Ustuk = CUnit('Ustuk',10,5,13,'EVM')#Создаём примерную карту

Ustuk.write_card("Ustuk_2023")#Записываем все данные в файл Ustuk_2023.json
Ustuk.read_card("Ustuk_2023")#Читаем из файла Ustuk_2023.json все данные и сразу же записываем в новую глобальную переменную для карты Ustuk_2023, которая будет иметь класс CUnit

print(globals()["Ustuk_2023"])#Смотрим результат

print(globals())
