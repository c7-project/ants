import pygame
from random import randint, choice
import ant_class
import hole_class
import sugar_class
import logger
import pixel_perfect
import display
from math import atan2, degrees


def get_random_ish_direction(max_degrees=10):
    """
    Random direction generator
    :param max_degrees: The maximum magnitude
    :return: Random number between -max_degrees and +max_degrees
    """
    return randint(-max_degrees, max_degrees)


def move_ants(ant_list, rock_list):
    new_list = []  # List to return
    for ant in ant_list:  # For each ant
        initial_ant = ant.rect.x, ant.rect.y, ant.direction
        if not ant.found_food and randint(0, 600) == 0:
            ant.random_sugar_targeting()
        if ant.return_loc\
                and not ant.found_food\
                and [ant.return_loc[0] - 57, ant.return_loc[1] - 57
                     ] not in sugar_class.sugar_locations:
            ant.return_loc = []
        ant = move_ant(ant)
        for rock in rock_list:
            attempts = 0
            give_up = False
            while pygame.sprite.spritecollide(
                    ant, rock_list, False
            ) and pixel_perfect.check_collision(ant, rock) and not give_up:
                ant.check_escape()
                attempts += 1
                if attempts > 10:
                    ant.direction += randint(0, 359)
                    ant.move(randint(3, 7))
                    if attempts > 11:
                        give_up = True
                else:
                    ant.rect.x, ant.rect.y, ant.direction = initial_ant
                    abs_angle_change = randint(20, 100)
                    if randint(0, 1) == 0:
                        ant.direction += abs_angle_change
                    else:
                        ant.direction -= abs_angle_change
                    ant = move_ant(ant)
        new_list.append(ant)  # Add to new list
    return new_list


def move_ant(ant):
    if ant.stop_count > 0:  # If need to wait for stop
        ant.stop_count -= 1
    else:  # Rotate and/or move or neither
        if randint(0, 20) > 0:  # Move
            ant.move(randint(1, 3))
        if ant.return_loc:
            face_return_loc(ant)
            ant.rotate(0)
        if randint(0, 4) > 0:  # Rotate
            ant.rotate(get_random_ish_direction(8))
        if randint(0, 180) == 0:  # Stop
            ant.stop(randint(8, 22))
    ant.movement_variant()
    return ant


def face_return_loc(ant):
    """"
    Sets the ant's direction to face its return location

    Formerly 'smants_guidants'
    """
    angle = get_angle(
        ant.rect.x + 12,
        ant.rect.y + 12,
        ant.return_loc[0],
        ant.return_loc[1])
    logger.log("hole:{},{} , ant:{},{} , angle:{}".format(
        str(ant.return_loc[0]),
        str(ant.return_loc[1]),
        str(ant.rect.x),
        str(ant.rect.y),
        angle))
    ant.direction = angle


def get_angle(x, y, center_x, center_y):
    angle = degrees(atan2(y - center_y, x - center_x))
    angle *= -1
    angle += 90 + 360
    angle %= 360
    return angle


def generate_new_ant(hole_list, ant_list, rock_list, ants, screen):
    if hole_list:  # Means 'if there are hole(s)'
        if ant_class.ants_underground > 0 and randint(0, 10) == 0:
            # Spawn new ant
            try:
                ant_list.append(ant_class.Ant(rock_list))  # Add to ant list
                ants.add(ant_list[-1])  # Add it to ants sprite group
                ant_class.ants_underground -= 1  # Decrement underground count
            except ValueError as e:
                logger.log("Ant can't appear from hole - " + str(e))
            except IndexError:
                logger.log("No holes exist, can't add ant")
    else:  # No holes exist
        display.display_text(
            screen,
            "Hit 'H' to add a hole at the mouse's location",
            18, (0, 0))
    return ant_list, ants


def user_add_ants(ant_list, ants, rock_list):
    if pygame.key.get_pressed()[pygame.K_a]:
        if ant_class.ants_underground > 0:
            try:
                ant_list.append(ant_class.Ant(rock_list))
                ants.add(ant_list[-1])  # Add it to ants sprite group
                ant_class.ants_underground -= 1  # Decrement underground count
            except ValueError as e:
                logger.log("Ant can't appear from hole - " + str(e))
    if pygame.key.get_pressed()[pygame.K_u]:
        ant_class.ants_underground += 1
    return ant_list, ants, rock_list


def load_ant_image_list():
    image_list = []
    for i in range(4):
        image_list.append(pygame.image.load(
            "images/moving_ant-v1/a{}.png".format(
                str(i+1).zfill(1))))
    return image_list


def ant_from_hole():
    """
    Get the coordinates of the centre of a random hole
    :return: x and y coordinates
    """
    random_hole = choice(hole_class.hole_locations)
    x = random_hole[0] + 18
    y = random_hole[1] + 18
    return x, y
