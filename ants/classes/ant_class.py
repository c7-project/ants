import pygame
from random import randint, choice
import math
import hole_class
import pixel_perfect
import ant_other
import misc

ants_underground = 50  # Number of ants currently underground


class Ant(pygame.sprite.Sprite):
    """
    Ants and their many mysterious methods
    """

    def __init__(self, rock_list, from_hole=True):
        """
        Set up ant class variables
        """
        pygame.sprite.Sprite.__init__(self)
        self.image_list = ant_other.load_ant_image_list()
        self.image = self.image_list[0]
        self.image_iteration = 0
        self.image_index = 0
        self.direction = randint(0, 359)
        self.rect = self.image.get_rect()
        self.found_food = False
        self.return_loc = []
        if from_hole:
            x_and_y = ant_other.ant_from_hole()
            self.rect.x, self.rect.y = x_and_y
        else:
            self.rect.x = randint(1, 879)
            self.rect.y = randint(1, 579)
        self.hitmask = pixel_perfect.get_alpha_hitmask(self.image, self.rect)
        self.previous_location = [self.rect.x, self.rect.y]
        self.stop_count = 0
        self.random_rotate = True
        self.head_start = 20
        self.free_will_timer = 0
        self.scout_ant = True
        if pygame.sprite.spritecollide(self, rock_list, False):
            raise ValueError("There's a rock in the way :(")

    def rotate(self, angle):
        """
        Calls misc.rotate_center to rotate ant based on initial image

        Negative angle: clockwise rotation
        Positive angle: anticlockwise rotation

        :param angle: The angle (degrees) to rotate the ant
        """
        self.direction += angle
        self.image = misc.rotate_center(
            self.image_list[self.image_index], self.direction)

    def resolve_direction(self):
        """
        Over many rotations, self.direction can get too high or low

        This method converts self.direction to its 0-359 degree equivalent
        """
        while self.direction < 0:
            self.direction += 360  # Makes direction positive
        self.direction %= 360  # Calculates direction's lowest equivalent

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
        self.check_escape(collision=False)
        self.previous_location = [self.rect.x, self.rect.y]
        if self.head_start > 0:
            self.head_start -= 1
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
        self.image_iteration = 0
        self.rotate(0)

    def set_return_hole(self, hole_list):
        """
        Its sets it up so that it can choose a random hole from hole_list
        """
        hole = choice(hole_list)
        self.return_loc = [hole.rect.x + 30, hole.rect.y + 30]

    def movement_variant(self):
        """
        Update ant image for walking sprites
        """
        self.image_iteration += 1
        self.image_iteration %= 16
        self.image_index = self.image_iteration // 4

    def check_escape(self, collision=True):
        """
        Escape from a rock collision when returning to holes
        """
        if self.scout_ant:
            return None
        if collision and self.found_food:  # If returning ant collides
            self.found_food = False  # Make the ant forget about food
            self.free_will_timer = randint(10, 70)  # Random timeout time
        elif not self.found_food and not collision:  # If ant moving randomly
            if self.free_will_timer > 0:  # If the ant has free will
                self.free_will_timer -= 1  # Take free will away
            else:
                if randint(0, 3) == 0:  # Sometimes pick different hole
                    new_return = choice(hole_class.hole_locations)
                    self.return_loc = [new_return[0] + 30, new_return[1] + 30]
                self.found_food = True  # Start navigating to hole again
