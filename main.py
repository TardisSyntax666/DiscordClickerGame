import pygame
import button as b
import generator as g
import os
from PIL import Image, ImageFilter

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 800
ICON = pygame.image.load("ICON.ico")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DiscordClicker")
pygame.display.set_icon(ICON)
dir_path = str(os.path.realpath("assets"))
dir_path_buttons = str(os.path.join(os.path.realpath("assets"), "buttons"))

WHITE = (255, 255, 255)
COLOUR = (54, 57, 63)
FADE_ONE = (214, 214, 216)
FADE_TWO = (173, 173, 176)
FADE_THREE = (132, 132, 137)
FADE_FOUR = (91, 91, 97)
FONT = pygame.font.Font(str(os.path.join(dir_path, 'Caramel Sweets.ttf')), 40)
SMALL_FONT = pygame.font.Font(os.path.join(dir_path, 'Caramel Sweets.ttf'), 25)

CLOCK = pygame.time.Clock()
FPS = 60

CLICKER_IMAGE_SIZE = (200, 200)
CLICKER_IMAGE = pygame.image.load(
    os.path.join(dir_path_buttons, 'DiscordClicker_asset_MiniDiscord.png')).convert_alpha()
CLICKER_IMAGE = pygame.transform.smoothscale(CLICKER_IMAGE, CLICKER_IMAGE_SIZE)
CLICKER_BUTTON_LOCATION = (400, 200)
SHADOW_IMAGE = pygame.image.load(os.path.join(dir_path_buttons, 'shadow.png')).convert_alpha()
SHADOW_IMAGE = pygame.transform.smoothscale(SHADOW_IMAGE, (210, 210))
NOT_SHADOW_IMAGE = pygame.image.load(os.path.join(dir_path_buttons, 'not_shadow.png')).convert_alpha()
NOT_SHADOW_IMAGE = pygame.transform.smoothscale(NOT_SHADOW_IMAGE, (210, 210))

TIER_IMAGE_SIZE = (100, 100)
TIER_ONE = pygame.image.load(os.path.join(dir_path_buttons, 'tier_1.png')).convert_alpha()
TIER_TWO = pygame.image.load(os.path.join(dir_path_buttons, 'tier_2.png')).convert_alpha()
TIER_THREE = pygame.image.load(os.path.join(dir_path_buttons, 'tier_3.png')).convert_alpha()
TIER_FOUR = pygame.image.load(os.path.join(dir_path_buttons, 'tier_4.png')).convert_alpha()
TIER_FIVE = pygame.image.load(os.path.join(dir_path_buttons, 'tier_5.png')).convert_alpha()
TIER_SIX = pygame.image.load(os.path.join(dir_path_buttons, 'tier_6.png')).convert_alpha()
TIER_SEVEN = pygame.image.load(os.path.join(dir_path_buttons, 'tier_7.png')).convert_alpha()
TIER_EIGHT = pygame.image.load(os.path.join(dir_path_buttons, 'tier_8.png')).convert_alpha()
TIER_NINE = pygame.image.load(os.path.join(dir_path_buttons, 'tier_9.png')).convert_alpha()
TIER_TEN = pygame.image.load(os.path.join(dir_path_buttons, 'tier_10.png')).convert_alpha()
TIER_SHADOW = pygame.image.load(os.path.join(dir_path_buttons, 'tier_shadow.png')).convert_alpha()
TIER_NOT_SHADOW = pygame.image.load(os.path.join(dir_path_buttons, 'tier_not_shadow.png')).convert_alpha()
TIER_LOCKED = pygame.image.load(os.path.join(dir_path_buttons, 'tier_locked.png')).convert_alpha()

MENU_IMAGE_SIZE = (150, 100)
PLAY = pygame.image.load(os.path.join(dir_path_buttons, 'play.png')).convert_alpha()
RESUME = pygame.image.load(os.path.join(dir_path_buttons, 'resume.png')).convert_alpha()
SAVE = pygame.image.load(os.path.join(dir_path_buttons, 'save.png')).convert_alpha()
LOAD = pygame.image.load(os.path.join(dir_path_buttons, 'load.png')).convert_alpha()
QUIT = pygame.image.load(os.path.join(dir_path_buttons, 'quit.png')).convert_alpha()
MENU_SHADOW = pygame.image.load(os.path.join(dir_path_buttons, 'menu_shadow.png')).convert_alpha()
MENU_NOT_SHADOW = pygame.image.load(os.path.join(dir_path_buttons, 'menu_not_shadow.png')).convert_alpha()

TITLE = pygame.image.load(os.path.join(dir_path, 'title.png')).convert_alpha()
BUTTON_CLICK_SOUND = pygame.mixer.Sound(os.path.join(dir_path, 'click_sound.wav'))
pygame.mixer.music.load(os.path.join(dir_path, 'background_track.mp3'))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)
BACKGROUND_IMAGE = pygame.image.load(os.path.join(dir_path, 'background.png')).convert_alpha()
BACKGROUND_IMAGE = pygame.transform.smoothscale(BACKGROUND_IMAGE, (1050, 850))
INFO_BAR_IMAGE = pygame.image.load(os.path.join(dir_path, 'info_bar.png')).convert_alpha()


def game_menu_window_draw(buttonlist, background_image):
    WINDOW.blit(background_image, (0, 0))
    for button in buttonlist:
        WINDOW.blit(button.current_shadow, (button.current_x - 5, button.current_y - 5))
        WINDOW.blit(button.current_surface, (button.current_x, button.current_y))

    pygame.display.update()


def game_menu(screenshot_path):
    run = True
    quit = False
    menu_buttons_list = []

    resume_button = b.Button(MENU_IMAGE_SIZE, (225, 550), RESUME, MENU_SHADOW, MENU_NOT_SHADOW)
    save_button = b.Button(MENU_IMAGE_SIZE, (425, 550), SAVE, MENU_SHADOW, MENU_NOT_SHADOW)
    quit_button = b.Button(MENU_IMAGE_SIZE, (625, 550), QUIT, MENU_SHADOW, MENU_NOT_SHADOW)

    menu_buttons_list.append(resume_button)
    menu_buttons_list.append(save_button)
    menu_buttons_list.append(quit_button)

    image = Image.open(screenshot_path)
    image = image.filter(ImageFilter.GaussianBlur(8))
    image.save(screenshot_path)
    image = pygame.image.load(screenshot_path).convert_alpha()

    while run:
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_buttons_list[0].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    run = False

                if menu_buttons_list[1].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    pass

                if menu_buttons_list[2].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    quit = True
                    run = False

        for button in menu_buttons_list:
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

        game_menu_window_draw(menu_buttons_list, image)
    os.remove(screenshot_path)
    return quit


def start_window_draw(buttonlist, images_list=None):
    WINDOW.fill(COLOUR)
    for button in buttonlist:
        WINDOW.blit(button.current_shadow, (button.current_x - 5, button.current_y - 5))
        WINDOW.blit(button.current_surface, (button.current_x, button.current_y))
    if images_list is not None:
        for image in images_list:
            WINDOW.blit(image[0], image[1])

    pygame.display.update()


def start_menu():
    run = True
    quit = False
    menu_buttons_list = []

    play_button = b.Button(MENU_IMAGE_SIZE, (225, 550), PLAY, MENU_SHADOW, MENU_NOT_SHADOW)
    load_button = b.Button(MENU_IMAGE_SIZE, (425, 550), LOAD, MENU_SHADOW, MENU_NOT_SHADOW)
    quit_button = b.Button(MENU_IMAGE_SIZE, (625, 550), QUIT, MENU_SHADOW, MENU_NOT_SHADOW)

    menu_buttons_list.append(play_button)
    menu_buttons_list.append(load_button)
    menu_buttons_list.append(quit_button)
    while run:
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_buttons_list[0].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    run = False

                if menu_buttons_list[1].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    pass

                if menu_buttons_list[2].is_over(pos):
                    BUTTON_CLICK_SOUND.play()
                    quit = True
                    run = False

        for button in menu_buttons_list:
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

        images_list = [(TITLE, (125, 50))]

        start_window_draw(menu_buttons_list, images_list)
    if not quit:
        main()
    else:
        pygame.mixer.music.stop()
        pygame.quit()


def main_window_draw(buttonlist, textlist, mouse_pos):
    if 1001 > mouse_pos[0] > -1 and 801 > mouse_pos[1] > -1:
        x_var = 500 - mouse_pos[0]
        y_var = 400 - mouse_pos[1]
        if x_var >= 500:
            offx = int((x_var - 500) / 500 * 25)
        else:
            offx = int(x_var / 500 * 25)

        if y_var >= 400:
            offy = int((y_var - 400) / 400 * 25)
        else:
            offy = int(y_var / 400 * 25)
    else:
        offx = 0
        offy = 0

    WINDOW.blit(BACKGROUND_IMAGE, (-25 + offx, -25 + offy))
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
    run = True
    members = 0
    per_second_counter = 0
    message_queue = (None, 0, 0)
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

    tier_one_gen = g.Generator(10, 1.10, 1.20, 1, "Created a text channel!")
    tier_two_gen = g.Generator(200, 5, 1.10, 2.5, "Created a voice channel!")
    tier_three_gen = g.Generator(5000, 10, 1.10, 5, "Created a role!")
    tier_four_gen = g.Generator(40000, 150, 1.10, 10, "Added a bot!")
    tier_five_gen = g.Generator(1000000, 300, 1.10, 400, "Hired a mod!")
    tier_six_gen = g.Generator(80000000, 1500, 1.10, 800, "Baned a trouble maker!")
    tier_seven_gen = g.Generator(1000000000, 20000, 1.10, 1000, "Got mentioned by an influencer!")
    tier_eight_gen = g.Generator(20000000000, 300000, 1.10, 2700, "Created a pay to win role!")
    tier_nine_gen = g.Generator(100000000000, 2700000, 1.10, 3600, "Hacked discord for members!")
    tier_ten_gen = g.Generator(20000000000000, 27000000, 1.10, 36000, "Got God to bless server!")

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
        CLOCK.tick(FPS)
        pos = pygame.mouse.get_pos()
        mouse_button_state = pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_list[0].is_over(pos):
                    members += 1

                for i in range(1, len(button_list)):
                    button = button_list[i]
                    if button.is_over(pos):
                        BUTTON_CLICK_SOUND.play()
                        if not button.locked:
                            if int(generator_list[i - 1].cost) <= members:
                                members = int(float(members) - generator_list[i - 1].cost)
                                generator_list[i - 1].upgrade()

                                if message_queue[0] is None or message_queue[0] == str(generator_list[i - 1].message):
                                    message_queue = (str(generator_list[i - 1].message), message_queue[1] + 1, 300)
                                else:
                                    message_queue = (str(generator_list[i - 1].message), 1, 300)
                            else:
                                message_queue = (f"That costs {str(int(generator_list[i - 1].cost))} members", 1, 300)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE] or not pygame.key.get_focused():
            screenshot_path = os.path.join(dir_path, 'temp.png')
            pygame.image.save(WINDOW, screenshot_path)
            if game_menu(screenshot_path):
                run = False

        if members >= 10 and button_list[1].locked:
            button_list[1].unlock()
        for gen in generator_list:
            i = generator_list.index(gen) + 2
            if gen.owned >= 10 and button_list[i].locked:
                button_list[i].unlock()

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
                cost_label = (gen_cost_label_surface, (120, button.y + 16), False)
                product_label = (gen_product_label_surface, (120, button.y + 42), False)
                owned_label = (gen_owned_label_surface, (120, button.y + 68), False)
                textlist.append(cost_label)
                textlist.append(product_label)
                textlist.append(owned_label)
            if not button.locked and button_num > 5:
                gen_cost_label_surface = SMALL_FONT.render("{:,} :Cost".format(int(gen.cost)), False, WHITE)
                gen_product_label_surface = SMALL_FONT.render("{:,} :Revenue".format(int(gen.production)), False, WHITE)
                gen_owned_label_surface = SMALL_FONT.render("{:,} :Owned".format(gen.owned), False, WHITE)
                cost_label = (
                    gen_cost_label_surface, (880 - gen_cost_label_surface.get_rect().size[0], button.y + 16), False)
                product_label = (
                    gen_product_label_surface, (880 - gen_product_label_surface.get_rect().size[0], button.y + 42),
                    False)
                owned_label = (
                    gen_owned_label_surface, (880 - gen_owned_label_surface.get_rect().size[0], button.y + 68), False)
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

        if message_queue[0] is not None:
            if message_queue[2] == 0:
                message_queue = (None, 0, 0)
            else:
                if message_queue[2] in range(241, 300):
                    colour = WHITE
                elif message_queue[2] in range(181, 240):
                    colour = FADE_ONE
                elif message_queue[2] in range(121, 180):
                    colour = FADE_TWO
                elif message_queue[2] in range(61, 120):
                    colour = FADE_THREE
                else:
                    colour = FADE_FOUR

                if message_queue[1] != 1:
                    info_label_surface = SMALL_FONT.render(str(str(message_queue[0])+ f" x{str(message_queue[1])}"), False, colour)
                    info_text_label = (info_label_surface, (500, 750), True)
                else:
                    info_label_surface = SMALL_FONT.render(str(message_queue[0]), False, colour)
                    info_text_label = (info_label_surface, (500, 750), True)
                textlist.append(info_text_label)
                message_queue = (message_queue[0], message_queue[1], message_queue[2]-1)

        textlist.append(main_counter)
        textlist.append(main_counter_label)


        main_window_draw(button_list, textlist, pos)

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    start_menu()
