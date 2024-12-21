from src.gameserver import GameServer
from src.resource import RESOURCE as res

class application_cli:
    def __init__(self):
        self.game_server = GameServer()
    
    def run(self, running = True):
        running = True
        while running:
            self.game_server.run_one_step()

app = application_cli()

app.run()