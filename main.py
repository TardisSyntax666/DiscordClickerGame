import pygame
import button as b
import os

pygame.init()

WIDTH, HEIGHT = 1000, 800
ICON = pygame.image.load("ICON.ico")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DiscordClicker")
pygame.display.set_icon(ICON)

WHITE = (255, 255, 255)
FONT = pygame.font.SysFont(os.path.join('assets', 'Caramel Sweets.ttf'), 50)

FPS = 60

CLICKER_IMAGE_SIZE = (200, 200)
CLICKER_IMAGE = pygame.image.load(os.path.join('assets', 'DiscordClicker_asset_MiniDiscord.png')).convert_alpha()
CLICKER_IMAGE = pygame.transform.smoothscale(CLICKER_IMAGE, CLICKER_IMAGE_SIZE)
CLICKER_BUTTON_LOCATION = (400, 200)
SHADOW_IMAGE = pygame.image.load(os.path.join('assets', 'shadow.png')).convert_alpha()
SHADOW_IMAGE = pygame.transform.smoothscale(SHADOW_IMAGE, (210, 210))
NOT_SHADOW_IMAGE = pygame.image.load(os.path.join('assets', 'not_shadow.png')).convert_alpha()
NOT_SHADOW_IMAGE = pygame.transform.smoothscale(NOT_SHADOW_IMAGE, (210, 210))

TIER_IMAGE_SIZE = (100, 100)
TIER_ONE = pygame.image.load(os.path.join('assets', 'tier_1.png')).convert_alpha()
TIER_TWO = pygame.image.load(os.path.join('assets', 'tier_2.png')).convert_alpha()
TIER_THREE = pygame.image.load(os.path.join('assets', 'tier_3.png')).convert_alpha()
TIER_FOUR = pygame.image.load(os.path.join('assets', 'tier_4.png')).convert_alpha()
TIER_FIVE = pygame.image.load(os.path.join('assets', 'tier_5.png')).convert_alpha()
TIER_SHADOW = pygame.image.load(os.path.join('assets', 'tier_shadow.png')).convert_alpha()
TIER_NOT_SHADOW = pygame.image.load(os.path.join('assets', 'tier_not_shadow.png')).convert_alpha()

BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png')).convert_alpha()
INFO_BAR_IMAGE = pygame.image.load(os.path.join('assets', 'info_bar.png')).convert_alpha()

members = 0
buttonlist = []

CLICKER_BUTTON = b.Button(CLICKER_IMAGE_SIZE, CLICKER_BUTTON_LOCATION,
                          CLICKER_IMAGE, SHADOW_IMAGE, NOT_SHADOW_IMAGE)
TIER_ONE_BUTTON = b.Button(TIER_IMAGE_SIZE, (10, 16), TIER_ONE, TIER_SHADOW, TIER_NOT_SHADOW)
TIER_TWO_BUTTON = b.Button(TIER_IMAGE_SIZE, (10, 131), TIER_TWO, TIER_SHADOW, TIER_NOT_SHADOW)
TIER_THREE_BUTTON = b.Button(TIER_IMAGE_SIZE, (10, 247), TIER_THREE, TIER_SHADOW, TIER_NOT_SHADOW)
TIER_FOUR_BUTTON = b.Button(TIER_IMAGE_SIZE, (10, 363), TIER_FOUR, TIER_SHADOW, TIER_NOT_SHADOW)
TIER_FIVE_BUTTON = b.Button(TIER_IMAGE_SIZE, (10, 479), TIER_FIVE, TIER_SHADOW, TIER_NOT_SHADOW)

buttonlist.append(CLICKER_BUTTON)
buttonlist.append(TIER_ONE_BUTTON)
buttonlist.append(TIER_TWO_BUTTON)
buttonlist.append(TIER_THREE_BUTTON)
buttonlist.append(TIER_FOUR_BUTTON)
buttonlist.append(TIER_FIVE_BUTTON)


def window_draw(buttonlist, members_text):
    WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
    WINDOW.blit(INFO_BAR_IMAGE, (0, 600))
    WINDOW.blit(members_text, (500 - (members_text.get_rect().size[0]) / 2, 650))
    label = FONT.render("Server Member Count:", False, WHITE)
    WINDOW.blit(label, (500 - (label.get_rect().size[0]) / 2, 610))
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
                    button.current_x = button.x + button.shrink_distance
                    button.current_y = button.y + button.shrink_distance
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

        members_text_surface = FONT.render(str(members), False, WHITE)

        window_draw(buttonlist, members_text_surface)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(members)
