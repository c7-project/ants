import pygame
from random import randint
import misc

# List of the [x, y] coordinates of existing holes
hole_locations = []


class Hole(pygame.sprite.Sprite):
    """
    Holes: The ants portal to the underworld
    """
    def __init__(self, at_mouse=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/hole01a.png")
        self.rect = self.image.get_rect()
        if at_mouse:  # Add hole at mouse location
            pos = misc.get_mouse_loc()
            # Set new top left coordinates
            self.rect.x, self.rect.y = pos[0] - 30, pos[1] - 30
        else:
            self.rect.x, self.rect.y = get_valid_hole_location()
        global hole_locations
        # Add new coordinates to list
        hole_locations.append([self.rect.x, self.rect.y])


def get_valid_hole_location():
    """
    Run through hole_locations in search for a new valid hole location
    :return: The valid x and y coordinates
    """
    valid_location = False  # First assume the location is not valid
    x = 0
    y = 0

    while not valid_location:  # Loop while coordinates not valid
        # Count to check the new hole is valid for all existing holes
        valid_count = 0
        x = randint(1, 838)  # Generate random x
        y = randint(1, 538)  # And random y
        for hole_loc in hole_locations:  # For each hole
            # If new hole is to the left of, or above the existing hole
            if x < hole_loc[0] - 61 or y < hole_loc[1] - 61:
                valid_count += 1
            # Else if new hole doesn't overlap existing hole
            elif not (x < hole_loc[0] + 61 and y < hole_loc[1] + 61):
                valid_count += 1
        # If coordinates are valid for every existing hole
        if valid_count == len(hole_locations):
            valid_location = True
    return x, y  # Return coordinates x and y
