from __future__ import division
from math import atan, atan2, degrees
import logger


def get_angle(x, y, center_x, center_y):
    angle = degrees(atan2(y - center_y, x - center_x))
    angle *= -1
    angle += 90 + 360
    angle %= 360
    return angle


def smants_guidants(ant):
    angle = get_angle(ant.rect.x, ant.rect.y, ant.return_loc[0], ant.return_loc[1])
    logger.log("hole:{},{} , ant:{},{} , angle:{}".format(
        str(ant.return_loc[0]),
        str(ant.return_loc[1]),
        str(ant.rect.x),
        str(ant.rect.y),
        angle), important=True)
    ant.direction = angle
