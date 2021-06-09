import pygame
import button as b
import os

pygame.font.init()
pygame.mixer.init()

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
TIER_SIX = pygame.image.load(os.path.join('assets', 'tier_6.png')).convert_alpha()
TIER_SEVEN = pygame.image.load(os.path.join('assets', 'tier_7.png')).convert_alpha()
TIER_EIGHT = pygame.image.load(os.path.join('assets', 'tier_8.png')).convert_alpha()
TIER_NINE = pygame.image.load(os.path.join('assets', 'tier_9.png')).convert_alpha()
TIER_TEN = pygame.image.load(os.path.join('assets', 'tier_10.png')).convert_alpha()
TIER_SHADOW = pygame.image.load(os.path.join('assets', 'tier_shadow.png')).convert_alpha()
TIER_NOT_SHADOW = pygame.image.load(os.path.join('assets', 'tier_not_shadow.png')).convert_alpha()
TIER_LOCKED = pygame.image.load(os.path.join('assets', 'tier_locked.png')).convert_alpha()

BUTTON_CLICK_SOUND = pygame.mixer.Sound(os.path.join('assets', 'click_sound.wav'))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.png')).convert_alpha()
INFO_BAR_IMAGE = pygame.image.load(os.path.join('assets', 'info_bar.png')).convert_alpha()


def window_draw(buttonlist, textlist):
    WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
    WINDOW.blit(INFO_BAR_IMAGE, (0, 600))
    for button in buttonlist:
        WINDOW.blit(button.current_shadow, (button.current_x - 5, button.current_y - 5))
        WINDOW.blit(button.current_surface, (button.current_x, button.current_y))
    for text in textlist:
        textobj = text[0]
        text_pos = text[1]
        WINDOW.blit(textobj, (text_pos[0] - (textobj.get_rect().size[0]) / 2, text_pos[1]))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    members = 0
    buttonlist = []

    clicker_button = b.Button(CLICKER_IMAGE_SIZE, CLICKER_BUTTON_LOCATION, CLICKER_IMAGE, SHADOW_IMAGE, NOT_SHADOW_IMAGE)
    tier_one_button = b.Button(TIER_IMAGE_SIZE, (10, 16), TIER_ONE, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_two_button = b.Button(TIER_IMAGE_SIZE, (10, 131), TIER_TWO, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_three_button = b.Button(TIER_IMAGE_SIZE, (10, 247), TIER_THREE, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_four_button = b.Button(TIER_IMAGE_SIZE, (10, 363), TIER_FOUR, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_five_button = b.Button(TIER_IMAGE_SIZE, (10, 479), TIER_FIVE, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_six_button = b.Button(TIER_IMAGE_SIZE, (890, 16), TIER_SIX, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_seven_button = b.Button(TIER_IMAGE_SIZE, (890, 131), TIER_SEVEN, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_eight_button = b.Button(TIER_IMAGE_SIZE, (890, 247), TIER_EIGHT, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_nine_button = b.Button(TIER_IMAGE_SIZE, (890, 363), TIER_NINE, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)
    tier_ten_button = b.Button(TIER_IMAGE_SIZE, (890, 479), TIER_TEN, TIER_SHADOW, TIER_NOT_SHADOW, TIER_LOCKED)

    buttonlist.append(clicker_button)
    buttonlist.append(tier_one_button)
    buttonlist.append(tier_two_button)
    buttonlist.append(tier_three_button)
    buttonlist.append(tier_four_button)
    buttonlist.append(tier_five_button)
    buttonlist.append(tier_six_button)
    buttonlist.append(tier_seven_button)
    buttonlist.append(tier_eight_button)
    buttonlist.append(tier_nine_button)
    buttonlist.append(tier_ten_button)

    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clicker_button.is_over(pos):
                    members += 1
                    print(members)
                if tier_one_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_one_button.locked:
                        print("Add a text channel")
                if tier_two_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_two_button.locked:
                        print("Add a voice channel")
                if tier_three_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_three_button.locked:
                        print("Add a role")
                if tier_four_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_four_button.locked:
                        print("Add a bot")
                if tier_five_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_five_button.locked:
                        print("Heir an admin")
                if tier_six_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_six_button.locked:
                        print("Ban a trouble maker")
                if tier_seven_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_seven_button.locked:
                        print("Get mentioned by an Influencer")
                if tier_eight_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_eight_button.locked:
                        print("Add a pay to win role")
                if tier_nine_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_nine_button.locked:
                        print("Hack discord for members")
                if tier_ten_button.is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_ten_button.locked:
                        print("Get god to bless server")
        if members >= 10 and tier_one_button.locked:
            tier_one_button.unlock()

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

        textlist = []
        members_text_surface = FONT.render(str(members), False, WHITE)
        main_counter = (members_text_surface, (500, 650))

        label_surface = FONT.render("Server Member Count:", False, WHITE)
        main_counter_label = (label_surface, (500, 610))

        textlist.append(main_counter)
        textlist.append(main_counter_label)

        window_draw(buttonlist, textlist)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
