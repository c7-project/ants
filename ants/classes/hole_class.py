import pygame
from random import randint

hole_locations = []  # List of the [x, y] coordinates of existing holes


class Hole(pygame.sprite.Sprite):
    """
    Holes: The ants' door to the underworld
    """
    # Creates holes randomly spread across the arena, making sure they don't appear twice at the same point.
    previous_coordinates = {}
    keys = previous_coordinates.keys()
    values = previous_coordinates.values()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/hole01a.png").convert_alpha()
        self.rect = self.image.get_rect()
        x = randint(1, 838)
        y = randint(1, 538)
        if x not in Hole.keys and y not in Hole.values:
            self.rect.x = x
            self.rect.y = y
            Hole.previous_coordinates[self.rect.x] = self.rect.y
        else:
            self.__init__()