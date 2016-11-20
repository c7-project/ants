from __future__ import division
from math import atan, degrees
import logger
from time import sleep


def smants_guidants(ant):
    dy = ant.rect.y - ant.return_loc[1]
    dx = ant.rect.x - ant.return_loc[0]
    if dx == 0:
        dy_by_dx = 9999999
    else:
        dy_by_dx = dy/dx
    radian_change = atan(dy_by_dx)
    degree_change = degrees(radian_change)
    logger.log(str(degree_change), important=True)
    if degree_change > 120:
        sleep(1)
