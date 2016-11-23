import pygame


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


def get_mouse_loc():
    pos = pygame.mouse.get_pos()
    return pos[0], pos[1]
