from random import randint
import pygame

from src.daisy import Daisy


class Game:
    def __init__(self, screen):
        self.screen = screen

        self.WIDTH, self.HEIGHT = screen.get_size()

        self.daisies = []
        self.ticker = 0

    def draw_background(self):
        """draw a background and create a border by drawing a smaller white square on top of a black background"""
        border_width = 4
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (border_width, border_width, self.WIDTH-border_width*2, self.HEIGHT-border_width*2))

    def update(self):
        self.draw_background()

        if self.ticker % 10000 == 0 and len(self.daisies) < 3:
            margin = 100
            daisy = Daisy(self.screen, randint(margin, self.WIDTH-margin),
                          randint(margin, self.HEIGHT-margin), 1 + randint(-4, 4) / 10)

            self.daisies.append(daisy)

        for daisy in self.daisies:
            daisy.update()

        self.ticker += 1
