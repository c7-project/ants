import pygame
from random import randint
import misc

rocks = ["Rock_1", "Rock_2", "Rock_3"]

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/rocks/Rock_{}.png".format(str(randint(1, 3))))
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 40, pos[1] - 40


