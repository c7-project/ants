import pygame
from random import randint
import misc


class Rock(pygame.sprite.Sprite):
    def __init__(self, ant_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "images/rocks/rock_{}.png".format(
                str(randint(1, 3)))).convert_alpha()
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 40, pos[1] - 40
        if pygame.sprite.spritecollide(self, ant_list, False):
            raise ValueError("Rock cannot be placed on an ant.")
