import pygame


class Button:

    def __init__(self, size, pos, button_surface, shadow_surface, not_shadow_surface, locked_surface=None):
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]
        self.current_x = self.x
        self.current_y = self.y
        self.shrink_distance = int((self.width - int(self.width * 0.9)) / 2)
        self.locked = False
        self.locked_surface = locked_surface
        self.real_surface = button_surface
        if locked_surface is not None:
            self.surface = self.locked_surface
            self.locked = True
        else:
            self.surface = button_surface
        self.pressed_surface = pygame.transform.smoothscale(self.surface,
                                                            (int(self.width * 0.9), int(self.height * 0.9)))
        self.current_surface = self.surface
        self.shadow = shadow_surface
        self.not_shadow = not_shadow_surface
        self.pressed_shadow = pygame.transform.smoothscale(shadow_surface, (
        int(shadow_surface.get_rect().size[0] * 0.9), int(shadow_surface.get_rect().size[1] * 0.9)))
        self.pressed_not_shadow = pygame.transform.smoothscale(not_shadow_surface, (
        int(shadow_surface.get_rect().size[0] * 0.9), int(shadow_surface.get_rect().size[1] * 0.9)))
        self.current_shadow = self.shadow
        self.is_pressed = False

    def unlock(self):
        self.locked = False
        self.surface = self.real_surface
        self.pressed_surface = pygame.transform.smoothscale(self.surface,
                                                            (int(self.width * 0.9), int(self.height * 0.9)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
