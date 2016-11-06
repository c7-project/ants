import pygame


class Ant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.initial_image = pygame.image.load("images/ant01a.png").convert_alpha()
        self.current_rotation = 0
        self.image = self.initial_image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 300

    def rotate(self, angle):
        self.current_rotation += angle
        self.image = rotate_center(self.initial_image, self.current_rotation)


def rotate_center(image, angle):
    """rotate an image while keeping its center and size"""
    # From http://pygame.org/wiki/RotateCenter
    orig_rect = image.get_rect()
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = orig_rect.copy()
    rotate_rect.center = rotate_image.get_rect().center
    rotate_image = rotate_image.subsurface(rotate_rect).copy()
    return rotate_image


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

    ant1 = Ant()  # Create an ant

    # Create groups for objects
    ants = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    rocks = pygame.sprite.Group()

    # Add ant1 to ants list
    ants.add(ant1)

    # List of all sprites
    all_sprites = pygame.sprite.Group()
    # Add sprite groups to main group
    all_sprites.add(ants, holes, rocks)
    # pygame clock
    clock = pygame.time.Clock()

    while not done:  # Main game loop
        clock.tick(60)  # 60 is the maximum frame-rate
        # Add background image, overlaying everything
        screen.blit(bg, (0, 0))

        # Rotate the ant - currently an experiment
        # Will be used for when the ant moves around on its own
        ant1.rotate(4)

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

        # Update display to show changes made in current iteration
        pygame.display.update()


main()
