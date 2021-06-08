import pygame

WIDTH, HEIGHT = 1000, 800
ICON = pygame.image.load("ICON.ico")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DiscordClicker")
pygame.display.set_icon(ICON)


class Main:

    def __init__(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
        quit()


if __name__ == "__main__":
    main = Main()
