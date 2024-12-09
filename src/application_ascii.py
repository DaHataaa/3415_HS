from src.gameserver import GameServer
from src.resource import RESOURCE as res


class Application:
    def __init__(self):
        self.game = GameServer()
        self.game.create_deck_phase()

    def run(self):
        running = True
        while running():
            pass #Доделать игру