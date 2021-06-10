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
dir_path = str(os.path.realpath("assets"))

WHITE = (255, 255, 255)
FONT = pygame.font.Font(str(os.path.join(dir_path, 'Caramel Sweets.ttf')), 40)
SMALL_FONT = pygame.font.Font(os.path.join(dir_path, 'Caramel Sweets.ttf'), 25)

FPS = 60

CLICKER_IMAGE_SIZE = (200, 200)
CLICKER_IMAGE = pygame.image.load(os.path.join(dir_path, 'DiscordClicker_asset_MiniDiscord.png')).convert_alpha()
CLICKER_IMAGE = pygame.transform.smoothscale(CLICKER_IMAGE, CLICKER_IMAGE_SIZE)
CLICKER_BUTTON_LOCATION = (400, 200)
SHADOW_IMAGE = pygame.image.load(os.path.join(dir_path, 'shadow.png')).convert_alpha()
SHADOW_IMAGE = pygame.transform.smoothscale(SHADOW_IMAGE, (210, 210))
NOT_SHADOW_IMAGE = pygame.image.load(os.path.join(dir_path, 'not_shadow.png')).convert_alpha()
NOT_SHADOW_IMAGE = pygame.transform.smoothscale(NOT_SHADOW_IMAGE, (210, 210))

TIER_IMAGE_SIZE = (100, 100)
TIER_ONE = pygame.image.load(os.path.join(dir_path, 'tier_1.png')).convert_alpha()
TIER_TWO = pygame.image.load(os.path.join(dir_path, 'tier_2.png')).convert_alpha()
TIER_THREE = pygame.image.load(os.path.join(dir_path, 'tier_3.png')).convert_alpha()
TIER_FOUR = pygame.image.load(os.path.join(dir_path, 'tier_4.png')).convert_alpha()
TIER_FIVE = pygame.image.load(os.path.join(dir_path, 'tier_5.png')).convert_alpha()
TIER_SIX = pygame.image.load(os.path.join(dir_path, 'tier_6.png')).convert_alpha()
TIER_SEVEN = pygame.image.load(os.path.join(dir_path, 'tier_7.png')).convert_alpha()
TIER_EIGHT = pygame.image.load(os.path.join(dir_path, 'tier_8.png')).convert_alpha()
TIER_NINE = pygame.image.load(os.path.join(dir_path, 'tier_9.png')).convert_alpha()
TIER_TEN = pygame.image.load(os.path.join(dir_path, 'tier_10.png')).convert_alpha()
TIER_SHADOW = pygame.image.load(os.path.join(dir_path, 'tier_shadow.png')).convert_alpha()
TIER_NOT_SHADOW = pygame.image.load(os.path.join(dir_path, 'tier_not_shadow.png')).convert_alpha()
TIER_LOCKED = pygame.image.load(os.path.join(dir_path, 'tier_locked.png')).convert_alpha()

BUTTON_CLICK_SOUND = pygame.mixer.Sound(os.path.join(dir_path, 'click_sound.wav'))
pygame.mixer.music.load(os.path.join(dir_path, 'background_track.mp3'))
pygame.mixer.music.play(-1, 0.0)
BACKGROUND_IMAGE = pygame.image.load(os.path.join(dir_path, 'background.png')).convert_alpha()
BACKGROUND_IMAGE = pygame.transform.smoothscale(BACKGROUND_IMAGE, (1050, 850))
INFO_BAR_IMAGE = pygame.image.load(os.path.join(dir_path, 'info_bar.png')).convert_alpha()


def window_draw(buttonlist, textlist, mouse_pos):
    if 1001 > mouse_pos[0] > -1 and 801 > mouse_pos[1] > -1:
        x_var = 500 - mouse_pos[0]
        y_var = 400 - mouse_pos[1]
        if x_var >= 500:
            offx = int((x_var - 500)/500*25)
        else:
            offx = int(x_var / 500 * 25)

        if y_var >= 400:
            offy = int((y_var - 400)/400*25)
        else:
            offy = int(y_var / 400 * 25)
    else:
        offx = 0
        offy = 0

    WINDOW.blit(BACKGROUND_IMAGE, (-25+offx, -25+offy))
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

    tier_one_gen = g.Generator(10, 1.10, 1.20, 1)
    tier_two_gen = g.Generator(200, 5, 1.10, 2.5)
    tier_three_gen = g.Generator(5000, 10, 1.10, 5)
    tier_four_gen = g.Generator(40000, 150, 1.10, 10)
    tier_five_gen = g.Generator(1000000, 300, 1.10, 400)
    tier_six_gen = g.Generator(80000000, 1500, 1.10, 800)
    tier_seven_gen = g.Generator(1000000000, 20000, 1.10, 1000)
    tier_eight_gen = g.Generator(20000000000, 300000, 1.10, 2700)
    tier_nine_gen = g.Generator(100000000000, 2700000, 1.10, 3600)
    tier_ten_gen = g.Generator(10000000000000, 27000000, 1.10, 36000)

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
    generator_list.append(tier_two_gen)
    generator_list.append(tier_three_gen)
    generator_list.append(tier_four_gen)
    generator_list.append(tier_five_gen)
    generator_list.append(tier_six_gen)
    generator_list.append(tier_seven_gen)
    generator_list.append(tier_eight_gen)
    generator_list.append(tier_nine_gen)
    generator_list.append(tier_ten_gen)

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
                    if not button_list[1].locked:
                        if int(generator_list[0].cost) <= members:
                            members = int(float(members) - generator_list[0].cost)
                            generator_list[0].upgrade()
                            print("Add a text channel")
                        else:
                            print(f"this costs {generator_list[0].cost}")

                if button_list[2].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[2].locked:
                        if generator_list[1].cost <= members:
                            members = int(float(members) - generator_list[1].cost)
                            generator_list[1].upgrade()
                            print("Add a voice channel")
                        else:
                            print(f"this costs {generator_list[1].cost}")

                if button_list[3].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[3].locked:
                        if generator_list[2].cost <= members:
                            members = int(float(members) - generator_list[2].cost)
                            generator_list[2].upgrade()
                            print("Add a role")
                        else:
                            print(f"this costs {generator_list[2].cost}")

                if button_list[4].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[4].locked:
                        if generator_list[3].cost <= members:
                            members = int(float(members) - generator_list[3].cost)
                            generator_list[3].upgrade()
                            print("Add a bot")
                        else:
                            print(f"this costs {generator_list[3].cost}")

                if button_list[5].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[5].locked:
                        if generator_list[4].cost <= members:
                            members = int(float(members) - generator_list[4].cost)
                            generator_list[4].upgrade()
                            print("Heir a mod")
                        else:
                            print(f"this costs {generator_list[4].cost}")

                if button_list[6].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[6].locked:
                        if generator_list[5].cost <= members:
                            members = int(float(members) - generator_list[5].cost)
                            generator_list[5].upgrade()
                            print("Ban a trouble maker")
                        else:
                            print(f"this costs {generator_list[5].cost}")

                if button_list[7].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[7].locked:
                        if generator_list[6].cost <= members:
                            members = int(float(members) - generator_list[6].cost)
                            generator_list[6].upgrade()
                            print("Get mentioned by an influencer")
                        else:
                            print(f"this costs {generator_list[6].cost}")

                if button_list[8].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[8].locked:
                        if generator_list[7].cost <= members:
                            members = int(float(members) - generator_list[7].cost)
                            generator_list[7].upgrade()
                            print("Add a pay to win role")
                        else:
                            print(f"this costs {generator_list[7].cost}")

                if button_list[9].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[9].locked:
                        if generator_list[8].cost <= members:
                            members = int(float(members) - generator_list[8].cost)
                            generator_list[8].upgrade()
                            print("Hack discord for members")
                        else:
                            print(f"this costs {generator_list[7].cost}")

                if button_list[10].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    if not button_list[10].locked:
                        if generator_list[9].cost <= members:
                            members = int(float(members) - generator_list[9].cost)
                            generator_list[9].upgrade()
                            print("Get god to bless server")
                        else:
                            print(f"this costs {generator_list[9].cost}")

        if members >= 10 and button_list[1].locked:
            button_list[1].unlock()
        if generator_list[0].owned >= 10 and button_list[2].locked:
            button_list[2].unlock()
        if generator_list[1].owned >= 10 and button_list[3].locked:
            button_list[3].unlock()
        if generator_list[2].owned >= 10 and button_list[4].locked:
            button_list[4].unlock()
        if generator_list[3].owned >= 10 and button_list[5].locked:
            button_list[5].unlock()
        if generator_list[4].owned >= 10 and button_list[6].locked:
            button_list[6].unlock()
        if generator_list[5].owned >= 10 and button_list[7].locked:
            button_list[7].unlock()
        if generator_list[6].owned >= 10 and button_list[8].locked:
            button_list[8].unlock()
        if generator_list[7].owned >= 10 and button_list[9].locked:
            button_list[9].unlock()
        if generator_list[8].owned >= 10 and button_list[10].locked:
            button_list[10].unlock()


        textlist = []
        if per_second_counter == 60:
            per_second_counter = 0
        per_second_counter += 1
        for gen in generator_list:
            if gen.owned >= 1:
                if per_second_counter == 60:
                    members = int(float(members) + gen.production)
            button_num = generator_list.index(gen) + 1
            button = button_list[button_num]
            if not button.locked and button_num < 6:
                gen_cost_label_surface = SMALL_FONT.render("Cost: {:,}".format(int(gen.cost)), False, WHITE)
                gen_product_label_surface = SMALL_FONT.render("Revenue: {:,}".format(int(gen.production)), False, WHITE)
                gen_owned_label_surface = SMALL_FONT.render("Owned: {:,}".format(gen.owned), False, WHITE)
                cost_label = (gen_cost_label_surface, (120, button.y+16), False)
                product_label = (gen_product_label_surface, (120, button.y+42), False)
                owned_label = (gen_owned_label_surface, (120, button.y+68), False)
                textlist.append(cost_label)
                textlist.append(product_label)
                textlist.append(owned_label)
            if not button.locked and button_num > 5:
                gen_cost_label_surface = SMALL_FONT.render("{:,} :Cost".format(int(gen.cost)), False, WHITE)
                gen_product_label_surface = SMALL_FONT.render("{:,} :Revenue".format(int(gen.production)), False, WHITE)
                gen_owned_label_surface = SMALL_FONT.render("{:,} :Owned".format(gen.owned), False, WHITE)
                cost_label = (gen_cost_label_surface, (880-gen_cost_label_surface.get_rect().size[0], button.y + 16), False)
                product_label = (gen_product_label_surface, (880-gen_product_label_surface.get_rect().size[0], button.y + 42), False)
                owned_label = (gen_owned_label_surface, (880-gen_owned_label_surface.get_rect().size[0], button.y + 68), False)
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

        window_draw(button_list, textlist, pos)

    pygame.mixer.music.stop()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
