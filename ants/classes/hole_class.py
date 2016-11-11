import pygame
from random import randint, choice

# List of the [x, y] coordinates of existing holes
hole_locations = []

def holes_manager(n):
    """
    Distributes the holes across evenly-sized
    x_values = 875//n
    y_values = 575//n
    cx = 0
    cy = 0
    while True:
        if cx >= 875 and cy <= 575:
            break
        cx += x_values
        cy += y_values
        x = rantint(1,cx)
        y = randint(1,cy)
        hole_locations.append([x, y])


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
        coordinates = choice(hole_locations)
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
        
        

