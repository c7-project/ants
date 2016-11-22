import pygame
from random import randint, choice
from math import atan2, degrees
import hole_class  # Used in ant_from_hole
import ant_class
import sugar_class
import pixel_perfect
import logger


def display_text(screen, text, size, location, bold=False, italic=False):
    """
    Display a string on the screen
    :param screen: The pygame.display screen object
    :param text: Text to be displayed
    :param size: Text size
    :param location: Location on screen
    :param bold: Uses bold Lekton
    :param italic: Uses italic Lekton
    """
    # Create font
    if bold:
        font_type = "Bold"
    elif italic:
        font_type = "Italic"
    else:
        font_type = "Regular"
    font = pygame.font.Font("fonts/Lekton-{}.ttf".format(font_type), size)
    # Label text
    label = font.render(text, 1, (250, 250, 250))
    # Display text
    screen.blit(label, location)


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


def move_ants(ant_list, rock_list):
    new_list = []  # List to return
    for ant in ant_list:  # For each ant
        initial_ant = ant.rect.x, ant.rect.y, ant.direction
        ant = move_ant(ant)
        for rock in rock_list:
            attempts = 0
            give_up = False
            while pygame.sprite.spritecollide(
                    ant, rock_list, False
            ) and pixel_perfect.check_collision(ant, rock) and not give_up:
                attempts += 1
                if attempts > 40:
                    ant.direction += randint(0, 359)
                    ant.move(randint(3, 7))
                    if attempts > 100:
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
        if ant.found_food:
            face_return_loc(ant)
        if randint(0, 20) > 0:  # Move
            ant.move(randint(1, 3))
        if randint(0, 4) > 0:  # Rotate
            ant.rotate(get_random_ish_direction(8))
        if randint(0, 180) == 0:  # Stop
            ant.stop(randint(8, 22))
    ant.movement_variant()
    return ant


def get_mouse_loc():
    pos = pygame.mouse.get_pos()
    return pos[0], pos[1]


def ant_sugar_collision(sugar_list, ant_list, hole_list, screen):
    for sugar in sugar_list:
        sugar_centre = pygame.draw.rect(screen, (255, 255, 255), (
            sugar.rect.x + 42, sugar.rect.y + 42, 30, 30), 1)
        for ant in ant_list:
            if ant.rect.colliderect(sugar_centre) and ant.head_start == 0:
                ant.found_food = True
                ant.set_return_hole(hole_list)
                ant.stop_count += randint(50, 87)
                ant.head_start += 20
                sugar.remaining_sugar -= 1
                if sugar_class.active_sugar > 0:
                    sugar_class.active_sugar -= 1
                    sugar_class.eaten_sugar += 1
                logger.log(
                    "active sugar: " + str(sugar_class.active_sugar)
                    + ", eaten sugar: " + str(sugar_class.eaten_sugar))
                sugar_exists = sugar.image_switch()
                if not sugar_exists:
                    if sugar in sugar_list:
                        sugar_list.remove(sugar)
    return sugar_list, ant_list


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
                logger.log("No holes exist", important=True)
    else:  # No holes exist
        display_text(
            screen,
            "Hit 'H' to add a hole at the mouse's location",
            18, (0, 0))
    return ant_list, ants


def load_ant_image_list():
    image_list = []
    for i in range(4):
        image_list.append(pygame.image.load(
            "images/moving_ant-v1/a{}.png".format(
                str(i+1).zfill(1))))
    return image_list


def get_angle(x, y, center_x, center_y):
    angle = degrees(atan2(y - center_y, x - center_x))
    angle *= -1
    angle += 90 + 360
    angle %= 360
    return angle


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
