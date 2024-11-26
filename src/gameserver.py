from src.gamestate import GameState
from src.hand import Hand
from src.field import Field,FieldNames
from src.stack import Stack


class GameServer:
	def __init__(self, state: GameState):
		self.game_state = state

	@classmethod
	def new_game(self):
		p1 = 
