import pygame
from random import randint

# List of the [x, y] coordinates of existing holes
hole_locations = [[900, 600]]


class Hole(pygame.sprite.Sprite):
    """
    Holes: The ants' door to the underworld
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/hole01a.png").convert_alpha()
        self.rect = self.image.get_rect()
        if len(hole_locations) > 60:
            raise ValueError("Exceeded maximum number of holes: 60")
        valid_location = False
        global hole_locations
        x = 0
        y = 0
        while not valid_location:
            valid_count = 0
            x = randint(1, 838)
            y = randint(1, 538)
            for hole_loc in hole_locations:
                if x < hole_loc[0] - 61 or y < hole_loc[1] - 61:
                    valid_count += 1
                elif not (x < hole_loc[0] + 61 and y < hole_loc[1] + 61):
                    valid_count += 1
            if valid_count == len(hole_locations):
                valid_location = True
        hole_locations.append([x, y])
        self.rect.x, self.rect.y = x, y
