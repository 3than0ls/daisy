import pygame

from src.daisy import Daisy


class Game:
    def __init__(self, screen):
        self.screen = screen

        self.WIDTH, self.HEIGHT = screen.get_size()
        self.daisy1 = Daisy(self.screen, 150, 150, 0.5)
        self.daisy2 = Daisy(self.screen, 250, 150, 1)
        self.daisy3 = Daisy(self.screen, 350, 150, 1.5)

    def draw_background(self):
        """draw a background and create a border by drawing a smaller white square on top of a black background"""
        border_width = 4
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (border_width, border_width, self.WIDTH-border_width*2, self.HEIGHT-border_width*2))

    def update(self):
        self.draw_background()
        self.daisy1.update()
        self.daisy2.update()
        self.daisy3.update()
