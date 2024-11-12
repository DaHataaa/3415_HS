from abc import ABC, abstractmethod

from player import Player
from field import FieldNames


class IPlayerInput(ABC):
    @abstractmethod
    def is_playable(self, player: Player, index: int) -> bool:
        """
        Выбираем карту (в руке), которую пользователь хочет сыграть, и проверяем, что её туда можно сыграть
        """
        pass

    @abstractmethod
    def play_card(self, player: Player, index: FieldNames):
        """
        Играет карту на выбранный индекс
        """
        pass

    @abstractmethod
    def unit_attack(self, player: Player, index_from: FieldNames, index_to: FieldNames):
        """
        Заставляем юнита атаковать
        """
        pass

    @abstractmethod
    def turn_end(self):
        """
        Закончить свой ход
        """
        pass
