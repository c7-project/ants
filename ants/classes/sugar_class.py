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
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 57, pos[1] - 57
