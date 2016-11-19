import pygame
import misc


class Sugar(pygame.sprite.Sprite):
    """
    Sugar for the ants to eat
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.initial_image = pygame.image.load("images/sugar/6.png")
        self.image = self.initial_image
        self.image_value = 1
        self.remaining_sugar = 30
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
            self.image = pygame.image.load("images/sugar/{}.png".format(str(value)))
        return True

