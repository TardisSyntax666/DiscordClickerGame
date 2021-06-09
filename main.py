import pygame
import button as b
import generator as g
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
SMALL_FONT = pygame.font.SysFont(os.path.join('assets', 'Caramel Sweets.ttf'), 30)

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
        is_middle = text[2]
        if is_middle:
            WINDOW.blit(textobj, (text_pos[0] - (textobj.get_rect().size[0]) / 2, text_pos[1]))
        else:
            WINDOW.blit(textobj, (text_pos[0], text_pos[1]))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    members = 0
    per_second_counter = 0
    button_list = []
    generator_list = []

    clicker_button = b.Button(CLICKER_IMAGE_SIZE, CLICKER_BUTTON_LOCATION, CLICKER_IMAGE, SHADOW_IMAGE,
                              NOT_SHADOW_IMAGE)
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

    tier_one_gen = g.Generator(10, 1.67, 1.07, 1)

    button_list.append(clicker_button)
    button_list.append(tier_one_button)
    button_list.append(tier_two_button)
    button_list.append(tier_three_button)
    button_list.append(tier_four_button)
    button_list.append(tier_five_button)
    button_list.append(tier_six_button)
    button_list.append(tier_seven_button)
    button_list.append(tier_eight_button)
    button_list.append(tier_nine_button)
    button_list.append(tier_ten_button)

    generator_list.append(tier_one_gen)

    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_list[0].is_over(pos):
                    members += 1
                if button_list[1].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_one_button.locked:
                        if generator_list[0].cost <= members:
                            members -= generator_list[0].cost
                            generator_list[0].upgrade()
                            print("Add a text channel")
                        else:
                            print(f"this costs {generator_list[0].cost}")
                if button_list[2].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_two_button.locked:
                        print("Add a voice channel")
                if button_list[3].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_three_button.locked:
                        print("Add a role")
                if button_list[4].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_four_button.locked:
                        print("Add a bot")
                if button_list[5].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_five_button.locked:
                        print("Heir an admin")
                if button_list[6].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_six_button.locked:
                        print("Ban a trouble maker")
                if button_list[7].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_seven_button.locked:
                        print("Get mentioned by an Influencer")
                if button_list[8].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_eight_button.locked:
                        print("Add a pay to win role")
                if button_list[9].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_nine_button.locked:
                        print("Hack discord for members")
                if button_list[10].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not tier_ten_button.locked:
                        print("Get god to bless server")
        if members >= 10 and button_list[1].locked:
            button_list[1].unlock()
        if generator_list[0].owned >= 10 and button_list[2].locked:
            button_list[2].unlock()

        textlist = []

        for gen in generator_list:
            if gen.owned >= 1:
                per_second_counter += 1
                if per_second_counter == 60:
                    per_second_counter = 0
                    members += gen.production
            button_num = generator_list.index(gen) + 1
            button = button_list[button_num]
            if not button.locked:
                gen_cost_label_surface = SMALL_FONT.render("Cost: {:,}".format(gen.cost), False, WHITE)
                gen_product_label_surface = SMALL_FONT.render("Revenue: {:,}".format(gen.production), False, WHITE)
                gen_owned_label_surface = SMALL_FONT.render("Owned: {:,}".format(gen.owned), False, WHITE)
                cost_label = (gen_cost_label_surface, (120, 32), False)
                product_label = (gen_product_label_surface, (120, 58), False)
                owned_label = (gen_owned_label_surface, (120, 84), False)
                textlist.append(cost_label)
                textlist.append(product_label)
                textlist.append(owned_label)

        for button in button_list:
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

        members_text_surface = FONT.render("{:,}".format(members), False, WHITE)
        main_counter = (members_text_surface, (500, 650), True)

        label_surface = FONT.render("Server Member Count:", False, WHITE)
        main_counter_label = (label_surface, (500, 610), True)

        textlist.append(main_counter)
        textlist.append(main_counter_label)

        window_draw(button_list, textlist)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
