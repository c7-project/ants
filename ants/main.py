from random import randint
import pygame

from classes import ant_class  # Ant
from classes import hole_class  # Hole
from classes import misc  # Methods


def main():
    """
    Main game code

    Contains pygame setup and the main game loop
    """
    pygame.init()  # Initialise pygame
    # Set window title
    screen = pygame.display.set_mode((900, 600))  # Set window size

    misc.display_text(screen, "loading...", 28, (20, 20))
    pygame.display.update()  # Update to loading screen

    pygame.display.set_caption(
        "Ants: An Artificial Intelligence Experiment by C7")
    done = False  # The game loop is broken when done becomes True

    # Load background image resource
    bg = pygame.image.load("images/bg01a.jpg")

    hole_list = [hole_class.Hole() for i in range(5)]  # Generate holes
    ant_list = [ant_class.Ant() for i in range(0)]  # Generate initial ants

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

    # List of all sprites
    all_sprites = pygame.sprite.Group()
    # Add sprite groups to main group
    all_sprites.add(ants, holes, rocks, food)
    # pygame clock
    clock = pygame.time.Clock()

    while not done:  # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If close button
                done = True  # Exit
            if event.type == pygame.KEYDOWN:  # If key pressed
                if event.key == pygame.K_ESCAPE:  # If 'esc' pressed
                    done = True  # Exit

        clock.tick(30)  # Frame-rate
        # Add background image, overlaying everything
        screen.blit(bg, (0, 0))

        if hole_list:  # Means 'if there are hole(s)'
            if ant_class.ants_underground > 0 and randint(0, 14) == 0:
                # Spawn new ant
                ant_list.append(ant_class.Ant())  # Add to ant list
                ants.add(ant_list[-1])  # Add it to ants sprite group
                ant_class.ants_underground -= 1  # Decrement underground count
        else:  # No holes exist
            misc.display_text(
                screen,
                "Press 'W' to add a hole at the mouse's location",
                18, (0, 0))

        for ant in ant_list:
            if ant.stop_count > 0:  # If need to wait for stop
                ant.stop_count -= 1
            else:  # Rotate and/or move or neither
                if randint(0, 2) == 0:  # Rotate
                    ant.rotate(misc.get_random_ish_direction(24))
                if randint(0, 7) > 0:  # Move
                    ant.move(3)
                if randint(0, 180) == 0:  # Stop
                    ant.stop(randint(8, 22))

        # Draw all sprites group to the screen
        holes.draw(screen)
        ants.draw(screen)
        # Update all sprites
        all_sprites.update()

        misc.display_text(
            screen, "fps:" + str(int(round(clock.get_fps(), 0))), 14, (850, 0))

        # Update display to show changes made in current iteration
        pygame.display.update()


main()
