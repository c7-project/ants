import pygame
from random import randint, choice # random function
import hole_class  # Used in ant_from_hole


def display_text(screen, text, size, location):
    """
    Display a string on the screen
    :param screen: The pygame.display screen object
    :param text: Text to be displayed
    :param size: Text size
    :param location: Location on screen
    """
    # Create font
    my_font = pygame.font.SysFont("monospace", size)
    # Label text
    label = my_font.render(text, 1, (250, 250, 250))
    # Display text
    screen.blit(label, location)

# random direct generator for ants
def get_random_ish_direction(max_degrees=10):
    """
    Random direction generator
    :param max_degrees: The maximum magnitude
    :return: Random number between -max_degrees and +max_degrees
    """
    return randint(-max_degrees, max_degrees)


def rotate_center(image, angle):
    """
    Rotate a square image while maintaining its center and size
    """
    # From http://pygame.org/wiki/RotateCenter
    orig_rect = image.get_rect()
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = orig_rect.copy()
    rotate_rect.center = rotate_image.get_rect().center
    rotate_image = rotate_image.subsurface(rotate_rect).copy()
    return rotate_image


def ant_from_hole():
    """
    Get the coordinates of the centre of a random hole
    :return: x and y coordinates
    """
    random_hole = choice(hole_class.hole_locations)
    x = random_hole[0] + 18
    y = random_hole[1] + 18
    return x, y


def move_ants(ant_list):
    new_list = []  # List to return
    for ant in ant_list:  # For each ant
        if ant.stop_count > 0:  # If need to wait for stop
            ant.stop_count -= 1
        else:  # Rotate and/or move or neither
            if randint(0, 2) == 0:  # Rotate
                ant.rotate(get_random_ish_direction(24))
            if randint(0, 7) > 0:  # Move
                ant.move(3)
            if randint(0, 180) == 0:  # Stop
                ant.stop(randint(8, 22))
        new_list.append(ant)  # Add to new list
    return new_list


def check_colliding(s1, s2):
    """
    Checks whether or not ant is on a hole
    :param s1: The ant
    :param s2: The hole centre
    :return: True if the ant is on the hole
    """
    return pygame.sprite.collide_rect(s1, s2)
