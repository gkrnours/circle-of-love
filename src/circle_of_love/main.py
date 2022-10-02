from pathlib import Path

import pygame

ROOT = Path(__file__).parent


def main():
    pygame.init()

    logo = pygame.image.load(f"{ROOT}/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((320, 240))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    from circle_of_love.main import main
    main()
