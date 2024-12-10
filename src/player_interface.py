from abc import ABC, abstractmethod

from src.field import FieldNames


class IPlayerInput(ABC):
    #CREATE_DECK
    @abstractmethod
    def choose_cards(self, all_cards: dict):
        """
        Просит игрока выбрать 8 карт из всех доступных карт
        """
        pass

    #CURRENT_TURN
    @abstractmethod
    def choose_current_turn(self):
        """
        Выбрать, какое действие вы хотите сделать за ход.
        Можно:
            попробовать сыграть карту,
            атаковать юнитом,
            закончить ход.
        """
        pass


    @abstractmethod
    def try_play_card(self, player, ifrom: int, ito: FieldNames):
        """
        Попытаться сыграть карту из слота ifrom руки в слоте ito поля
        """
        pass

    @abstractmethod
    def unit_attack(self, server, ifrom: FieldNames, ito: FieldNames):
        """
        Атакуем юнитом вражеского юнита
        """
        pass

    @abstractmethod
    def turn_end(self):
        """
        Закончить свой ход
        """
        pass