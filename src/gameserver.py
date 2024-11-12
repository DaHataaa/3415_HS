from src.gamestate import *


class GameServer:
<<<<<<< HEAD
	def __init__(self, state: GameState):
		if isinstance(state, GameState):
			self.state = state
		else:
			p1 = Player(Field(), Hand(), Stack())
			p2 = Player(Field(), Hand(), Stack())
			state = GameState(p1, p2)
=======
    def __init__(self, state: GameState):
        if isinstance(state, GameState):
            self.state = state
        else:
            p1 = Player(Field(), Hand(), Stack())
            p2 = Player(Field(), Hand(), Stack())
            state = GameState(p1, p2)
>>>>>>> origin/main
