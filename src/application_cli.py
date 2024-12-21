from src.players.cli import CLI
from src.gameserver import GameServer
from src.resource import RESOURCE as res

class application_cli:
    def __init__(self):
        self.game_cli = CLI()
        self.game_server = GameServer()
    
    def run(self, running = True):
        running = True
        while running:
            self.game_cli.choose_current_turn(self.game_server)

app = application_cli()

app.run()