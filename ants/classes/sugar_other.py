import pygame
from random import randint
import logger
import sugar_class


def ant_sugar_collision(sugar_list, ant_list, hole_list, screen):
    for sugar in sugar_list:
        sugar_centre = pygame.draw.rect(screen, (255, 255, 255), (
            sugar.rect.x + 42, sugar.rect.y + 42, 30, 30), 1)
        for ant in ant_list:
            if ant.rect.colliderect(sugar_centre) and ant.head_start == 0:
                ant.found_food = True
                ant.scout_ant = False
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
