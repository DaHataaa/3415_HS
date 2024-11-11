from abc import ABC, abstractmethod

from player import Player

class IPlayerInput(ABC):
    @abstractmethod
    def choose_card(self, player: Player, position: int) -> bool:
        """
            Выбираем карту, которую пользователь хочет сыграть, и проверяем, что её туда можно сыграть
        """
        pass

    @abstractmethod
    def play_card(self, player: Player, position: int):
        """
            Играет карту на выбранный индекс
        """
        pass


