import pygame
import sys

from src.game import Game


(WIDTH, HEIGHT) = (600, 600)


def main():
    pygame.init()

    # initialize screen display
    display = pygame.display
    display.set_icon(pygame.image.load('./assets/daisy.png'))
    screen = display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    display.set_caption("Daisy")

    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
