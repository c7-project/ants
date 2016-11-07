import pygame
import math
from random import randint, choice



class Ant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.initial_image = pygame.image.load("images/ant01a.png").convert_alpha()
        self.direction = randint(0, 359)
        self.image = self.initial_image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 300
        self.stop_count = 0

    def rotate(self, angle):
        self.direction += angle
        self.image = rotate_center(self.initial_image, self.direction)

    def resolve_direction(self):
        while self.direction < 0:
            self.direction += 360
        self.direction %= 360

    def change_collision_direction(self, boundary_value):
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
        self.resolve_direction()
        if self.rect.x < 1:  # Left edge
            self.change_collision_direction(90)
        if self.rect.x > 875:  # Right edge
            self.change_collision_direction(90)
        if self.rect.y < 1:  # Top edge
            self.change_collision_direction(0)
        if self.rect.y > 575:  # Bottom edge
            self.change_collision_direction(180)

    def move(self, distance):
        self.detect_edge()
        dx = (math.cos(math.radians(self.direction - 90)))
        dy = (math.sin(math.radians(self.direction - 90)))
        if dx < 0:
            dx *= 1.5
        if dy > 0:
            dy *= 1.5
        # print(str(dx) + " and " + str(dy))
        self.rect.x -= dx * distance
        self.rect.y += dy * distance

    def stop(self, iterations):
        self.stop_count += iterations


class Hole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/hole01a.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint(1, 875)
        self.rect.y = randint(1, 575)



class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        food_images = ["pictures/banana.png", "pictures/apple.png", "pictures/donut.png", "pictures/GrapeRedSeedless.png"]
        self.image = pygame.image.load(choice(food_images)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint(1, 875)
        self.rect.y = randint(1, 575)

    









def display_text(screen, text, size, location):
    # Create font
    my_font = pygame.font.SysFont("monospace", size)
    # Label text
    label = my_font.render(text, 1, (250, 250, 250))
    # Display text
    screen.blit(label, location)


def rotate_center(image, angle):
    """rotate an image while keeping its center and size"""
    # From http://pygame.org/wiki/RotateCenter
    orig_rect = image.get_rect()
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = orig_rect.copy()
    rotate_rect.center = rotate_image.get_rect().center
    rotate_image = rotate_image.subsurface(rotate_rect).copy()
    return rotate_image


def get_random_ish_direction(max_degrees=10):
    return randint(-max_degrees, max_degrees)


def main():
    """
    Main game code

    Contains pygame setup and the main game loop
    """
    pygame.init()  # Initialise pygame
    # Set window title
    pygame.display.set_caption("Ants: An Artificial Intelligence Experiment by C7")
    screen = pygame.display.set_mode((900, 600))  # Set window size
    done = False  # The game loop is broken when done becomes True

    # Load background image resource
    bg = pygame.image.load("images/bg01a.jpg")

    ant_list = [Ant() for i in range(40)]
    hole_list = [Hole() for i in range(3)]
    food_list = [Food() for i in range(10)]

   



    # Create groups for objects
    ants = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    food = pygame.sprite.Group()

    # Add ants_list objects to ants list
    for individual_ant in ant_list:
        ants.add(individual_ant)

    for individual_hole in hole_list:
        holes.add(individual_hole)

    for individual_meal in food_list:
        food.add(individual_meal)

    # List of all sprites
    all_sprites = pygame.sprite.Group()
    # Add sprite groups to main group
    all_sprites.add(ants, holes, rocks, food)
    # pygame clock
    clock = pygame.time.Clock()

    while not done:  # Main game loop
        clock.tick(60)  # Frame-rate
        # Add background image, overlaying everything
        screen.blit(bg, (0, 0))

        hits = pygame.sprite.spritecollide(ants, Hole, False, pygame.sprite.collide_circle)
        if hits:
            done = True

        # Rotate the ant - currently an experiment
        # Will be used for when the ant moves around on its own
        for ant in ant_list:
            if ant.stop_count > 0:  # If need to wait for stop
                ant.stop_count -= 1
            else:  # Rotate and/or move or neither
                if randint(0, 2) == 0:  # Rotate
                    ant.rotate(get_random_ish_direction(14))
                if randint(0, 7) > 0:  # Move
                    ant.move(2)
                if randint(0, 150) == 0:
                    ant.stop(randint(10, 40))

        # Draw all sprites group to the screen
        all_sprites.draw(screen)
        # Update all sprites
        all_sprites.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If close button
                done = True  # Exit
            if event.type == pygame.KEYDOWN:  # If key pressed
                if event.key == pygame.K_ESCAPE:  # If 'esc' pressed
                    done = True  # Exit

        display_text(screen, "fps:" + str(int(round(clock.get_fps(), 0))), 14, (850, 0))

        # Update display to show changes made in current iteration
        pygame.display.update()


main()
