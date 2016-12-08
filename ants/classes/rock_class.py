import pygame
from random import randint
import misc
import logger
import pixel_perfect

number_of_rocks = 0  # Number is incremented when new rocks are added


class Rock(pygame.sprite.Sprite):
    def __init__(self, ant_list, rock_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "images/rocks/rock_{}.png".format(
                str(randint(1, 4)))).convert_alpha()
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 40, pos[1] - 40
        if pygame.sprite.spritecollide(self, ant_list, False):
            raise ValueError("Rock cannot be placed on an ant.")
        if pygame.sprite.spritecollide(self, rock_list, False):
            raise ValueError("Rock cannot be placed on other rock.")
        global number_of_rocks
        number_of_rocks += 1
        logger.log("Added a rock")
        self.hitmask = pixel_perfect\
            .get_colour_key_and_alpha_hitmask(self.image, self.rect)
