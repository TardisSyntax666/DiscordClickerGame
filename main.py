import pygame

WIDTH, HEIGHT = 1000, 800
ICON = pygame.image.load("ICON.ico")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DiscordClicker")
pygame.display.set_icon(ICON)

WHITE = (255, 255, 255)


def window_draw():
    WINDOW.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window_draw()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
