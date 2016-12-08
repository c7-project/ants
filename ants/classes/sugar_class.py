import pygame
import misc

sugar_locations = []  # Appended to when sugar is added. Stores all x,y
active_sugar = 0
eaten_sugar = 0


class Sugar(pygame.sprite.Sprite):
    """
    Sugar for the ants to eat
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/sugar/6.png")
        self.image_value = 1
        self.remaining_sugar = 30
        global active_sugar
        active_sugar += self.remaining_sugar
        self.rect = self.image.get_rect()
        pos = misc.get_mouse_loc()
        self.rect.x, self.rect.y = pos[0] - 57, pos[1] - 57
        global sugar_locations
        sugar_locations.append([self.rect.x, self.rect.y])

    def image_switch(self):
        """
        Change to new images with less sugar
        """
        value = (self.remaining_sugar + 4) // 5
        if value == 0:  # Sugar is completely gone
            self.kill()  # Sugar is removed (sprite killed)
            global sugar_locations
            location = [self.rect.x, self.rect.y]
            if location in sugar_locations:
                # Remove sugar from global list
                sugar_locations.remove(location)
            return False
        elif self.image_value != value:
            # Switch to relevant image according to image value
            # Image only loaded when value has changed to improve efficiency
            self.image_value = value
            self.image = pygame.image.load(
                "images/sugar/{}.png".format(str(value)))
        return True
