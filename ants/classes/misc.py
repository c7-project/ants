import pygame
from random import randint


def display_text(screen, text, size, location):
    # Create font
    my_font = pygame.font.SysFont("monospace", size)
    # Label text
    label = my_font.render(text, 1, (250, 250, 250))
    # Display text
    screen.blit(label, location)


def get_random_ish_direction(max_degrees=10):
    return randint(-max_degrees, max_degrees)


def rotate_center(image, angle):
    """rotate an image while keeping its center and size"""
    # From http://pygame.org/wiki/RotateCenter
    orig_rect = image.get_rect()
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = orig_rect.copy()
    rotate_rect.center = rotate_image.get_rect().center
    rotate_image = rotate_image.subsurface(rotate_rect).copy()
    return rotate_image
