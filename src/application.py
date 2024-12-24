import pygame

from gameserver import GameServer
from resource import RESOURCE as res


class Application:
    def __init__(self):
        pygame.init()
        self.size = (self.width, self.height) = (res["width"], res["height"])
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(res["width"])

        self.vgame = None

    def run(self):
        clock = pygame.time.Clock()
        running = True

        self.display.fill(res[font_color], (0, 0, self.width, self.height))
        pygame.display.update()

        while running:
            self.vgame.model_update()
            self.vgame.redraw(self.display)

            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT
                    or event.type == pygame.KEYDOWN
                    and event.key == pygame.K_q
                ):
                    running = False
                self.vgame.event_processing(event)

            clock.tick(res["FPS"])
