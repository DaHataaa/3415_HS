from src.gameserver import GameServer
from src.resource import RESOURCE as res

class application_cli:
    def __init__(self):
        self.game_server = GameServer()
    

app = application_cli()

app.game_server.run()