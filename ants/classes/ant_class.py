import pygame
from random import randint
import math

import misc

ants_underground = 30  # Number of ants currently underground


class Ant(pygame.sprite.Sprite):
    """
    Ants and their many mysterious methods
    """
    def __init__(self, from_hole=True):
        pygame.sprite.Sprite.__init__(self)
        self.initial_image = pygame.image.load(
            "images/ant01a.png").convert_alpha()
        self.direction = randint(0, 359)
        self.image = self.initial_image
        self.rect = self.image.get_rect()
        if from_hole:
            self.rect.x, self.rect.y = misc.ant_from_hole()
        else:
            self.rect.x = randint(1, 879)
            self.rect.y = randint(1, 579)
        self.stop_count = 0
        self.random_rotate = True

    def rotate(self, angle):
        """
        Calls misc.rotate_center to rotate ant based on initial image

        Negative angle: clockwise rotation
        Positive angle: anticlockwise rotation

        :param angle: The angle (degrees) to rotate the ant
        """
        self.direction += angle
        self.image = misc.rotate_center(self.initial_image, self.direction)

    def resolve_direction(self):
        """
        Over many rotations, self.direction can get too high or low

        This method converts self.direction to its 0-359 degree equivalent
        """
        while self.direction < 0:
            self.direction += 360
        self.direction %= 360

    def turn_from_corner(self):
        """
        If ant moves towards corner, start turning away.

        This needs to be refactored a lot - maybe a method for each 'if'.
        """
        self_x = self.rect.x
        self_y = self.rect.y
        direction = self.direction
        random_rotate = False

        if self_x <= 30 and self_y <= 30:  # Top left corner
            if 45 < direction < 225:  # Towards left
                direction += randint(14, 24)
            else:  # Towards top
                direction -= randint(14, 24)

        elif self_x >= 846 and self_y <= 30:  # Top right corner
            if 135 < direction < 315:  # Towards right
                direction -= randint(14, 24)
            else:  # Towards top
                direction += randint(14, 24)

        elif self_x <= 30 and self_y >= 546:  # Bottom left corner
            if 135 < direction < 315:  # Towards bottom
                direction += randint(14, 24)
            else:  # Towards left
                direction -= randint(14, 24)

        elif self_x >= 846 and self_y >= 546:  # Bottom right corner
            if 45 < direction < 225:  # Towards bottom
                direction -= randint(14, 24)
            else:  # Towards right
                direction += randint(14, 24)

        else:  # Not in any corners
            random_rotate = True
        self.random_rotate = random_rotate
        self.direction = direction

    def change_collision_direction(self, boundary_value):
        """
        This responds to when an ant hits a wall by changing its direction
        """
        if self.direction < boundary_value:
            self.direction -= randint(20, 30)
        elif boundary_value == 0:
            if self.direction > 270:
                self.direction -= randint(20, 30)
            else:
                self.direction += randint(20, 30)
        elif self.direction > boundary_value:
            self.direction += randint(20, 30)
        else:  # Facing edge
            magnitude = randint(30, 40)
            if randint(0, 1) == 0:
                self.direction += magnitude
            else:
                self.direction -= magnitude

    def detect_edge(self):
        """
        Detects when an ant hits a border
        """
        self.resolve_direction()
        self.turn_from_corner()
        if self.rect.x < 1:  # Left edge
            self.change_collision_direction(90)
        if self.rect.x > 875:  # Right edge
            self.change_collision_direction(270)
        if self.rect.y < 1:  # Top edge
            self.change_collision_direction(0)
        if self.rect.y > 575:  # Bottom edge
            self.change_collision_direction(180)

    def move(self, distance):
        """
        Moves forwards in the ant's current direction
        :param distance: How far the ant moves
        """
        self.detect_edge()
        dx = (math.cos(math.radians(self.direction - 90)))
        dy = (math.sin(math.radians(self.direction - 90)))
        if dx < 0:
            dx *= 1.5
        if dy > 0:
            dy *= 1.5
        self.rect.x -= dx * distance
        self.rect.y += dy * distance

    def stop(self, iterations):
        """
        Stops ant for number of iterations
        :param iterations:
        """
        self.stop_count += iterations
