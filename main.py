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

BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png')).convert_alpha()
SHADOW_IMAGE = pygame.image.load(os.path.join('assets', 'shadow.png')).convert_alpha()
SHADOW_IMAGE = pygame.transform.smoothscale(SHADOW_IMAGE, (210, 210))
NOT_SHADOW_IMAGE = pygame.image.load(os.path.join('assets', 'not_shadow.png')).convert_alpha()
NOT_SHADOW_IMAGE = pygame.transform.smoothscale(NOT_SHADOW_IMAGE, (210, 210))

members = 0
buttonlist = []


class ClickerButton:

    def __init__(self, size, pos, button_surface, shadow_surface, not_shadow_surface):
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]
        self.current_x = self.x
        self.current_y = self.y
        self.surface = button_surface
        self.pressed_surface = pygame.transform.smoothscale(button_surface, (180, 180))
        self.current_surface = self.surface
        self.shadow = shadow_surface
        self.not_shadow = not_shadow_surface
        self.pressed_shadow = pygame.transform.smoothscale(shadow_surface, (190, 190))
        self.pressed_not_shadow = pygame.transform.smoothscale(not_shadow_surface, (190, 190))
        self.current_shadow = self.shadow
        self.is_pressed = False

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


CLICKER_BUTTON = ClickerButton(CLICKER_IMAGE_SIZE, CLICKER_BUTTON_LOCATION,
                               CLICKER_IMAGE, SHADOW_IMAGE, NOT_SHADOW_IMAGE)
buttonlist.append(CLICKER_BUTTON)


def window_draw(buttonlist):
    WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
    for button in buttonlist:
        WINDOW.blit(button.current_shadow, (button.current_x - 5, button.current_y - 5))
        WINDOW.blit(button.current_surface, (button.current_x, button.current_y))
    pygame.display.update()


def main(members):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLICKER_BUTTON.is_over(pos):
                    members += 1
                    print(members)

        for button in buttonlist:
            if button.is_over(pos):
                button.current_shadow = button.not_shadow
                if mouse_button_state[0]:
                    button.current_surface = button.pressed_surface
                    button.current_shadow = button.pressed_not_shadow
                    button.current_x = button.x + 10
                    button.current_y = button.y + 10
                    button.is_pressed = True
                else:
                    button.current_surface = button.surface
                    button.current_shadow = button.not_shadow
                    button.current_x = button.x
                    button.current_y = button.y
                    button.is_pressed = False
            else:
                if button.is_pressed and mouse_button_state[0]:
                    button.current_shadow = button.pressed_shadow
                else:
                    button.current_surface = button.surface
                    button.current_shadow = button.shadow
                    button.current_x = button.x
                    button.current_y = button.y
                    button.is_pressed = False

        window_draw(buttonlist)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(members)
