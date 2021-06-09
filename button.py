import pygame


class Button:

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
