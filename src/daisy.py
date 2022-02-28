import math
from random import randint
import pygame


class Daisy:
    def __init__(self, screen, x, y, max_size):
        self.screen = screen
        self.x = x
        self.y = y

        self.max_size = max_size  # controls how big the daisy can become
        self.size = 0  # controls how big the daisy currently is
        self.growth = 0.001

        self.img = pygame.image.load('./assets/daisy.png').convert_alpha()

        self.img = pygame.transform.rotate(
            self.img, randint(0, 360))

        self.img_rect = self.img.get_rect()
        self.scaled_img = self.img

    def move(self, x, y):
        self.x = x
        self.y = y

    def colliding(self, rect):
        """check collision with rect, usually player's collision rect"""
        # shrink rect's colliding box by just a bit
        colliding_rect = self.scaled_img.get_rect().inflate(-20, -20)

        return colliding_rect.colliderect(rect)

    def update(self):
        self.scaled_img = pygame.transform.scale(
            self.img, (round(self.img_rect.w * self.size), round(self.img_rect.h * self.size)))

        scaled_rect = self.scaled_img.get_rect(center=(self.x, self.y))
        self.screen.blit(
            self.scaled_img, scaled_rect)

        self.growth = max(self.growth * 0.999,
                          0.00001)
        self.size = min(self.size + self.growth * self.max_size, self.max_size)
