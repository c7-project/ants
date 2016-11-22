import pygame
import misc

active_sugar = 0
eaten_sugar = 0


class Sugar(pygame.sprite.Sprite):
    """
    Sugar for the ants to eat
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/sugar/6.png")
        self.image_value = 1
        self.remaining_sugar = 30
        global active_sugar
        active_sugar += self.remaining_sugar
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 57, pos[1] - 57

    def image_switch(self):
        value = (self.remaining_sugar + 4) // 5
        if value == 0:
            self.kill()
            return False
        elif self.image_value != value:
            self.image_value = value
            self.image = pygame.image.load(
                "images/sugar/{}.png".format(str(value)))
        return True
