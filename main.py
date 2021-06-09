import pygame
import os

WIDTH, HEIGHT = 1000, 800
ICON = pygame.image.load("ICON.ico")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DiscordClicker")
pygame.display.set_icon(ICON)

WHITE = (255, 255, 255)

FPS = 60

CLICKER_IMAGE_SIZE = (200, 200)
CLICKER_IMAGE = pygame.image.load(os.path.join('assets', 'DiscordClicker_asset_MiniDiscord.png')).convert_alpha()
CLICKER_IMAGE = pygame.transform.smoothscale(CLICKER_IMAGE, CLICKER_IMAGE_SIZE)
CLICKER_BUTTON_LOCATION = (400, 200)

members = 0


class ClickerButton:

    def __init__(self, size, pos):
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


CLICKER_BUTTON = ClickerButton(CLICKER_IMAGE_SIZE, CLICKER_BUTTON_LOCATION)


def window_draw():
    WINDOW.fill(WHITE)
    WINDOW.blit(CLICKER_IMAGE, CLICKER_BUTTON_LOCATION)
    pygame.display.update()


def main(members):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLICKER_BUTTON.is_over(pos):
                    members += 1
                    print(members)

        window_draw()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(members)
