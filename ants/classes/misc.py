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
