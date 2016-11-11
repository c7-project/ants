import pygame
from random import randint, choice

# List of the [x, y] coordinates of existing holes
hole_locations = []

def holes_manager(n):
    # Distributes the holes across evenly-sized 
    # squares whose area is the result of dividing
    # the pixels by the desired number of holes
    x_values = 875//n
    y_values = 575//n
    cx = 0 # The value is increased as holes are placed within the squares
    cy = 0 # The same variable for the possible y values
    tx = 1 # a possible solution to the problem, the variable is increased by 
           # the previous cx value in order to determine an appropriate value for the location of holes
           # within the random function
    ty = 1 # The same variable for the possible y values
    randomness_constant = randint(1,5) #The logical distribution of the holes on the screen, makes them form a diagonal line,
                                        # as the number of holes increases they tend to clash, this value moves them back and forth
                                        # reducing the change that that might happen, the randomness_constant can be modified to adjust
                                        # the distribution of the holes at will
    while True:
        if cx >= 875 and cy <= 575:
            break
        cx += x_values
        cy += y_values
        x = rantint(t1,cx)
        y = randint(t2,cy)
        t1 += x_values
        t2 += y_valus
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
        
        

