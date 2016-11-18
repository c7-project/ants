from random import randint
import pygame

from classes import ant_class  # Ant
from classes import hole_class  # Hole
from classes import sugar_class  # Sugar
from classes import misc  # Other methods
from classes import video  # Video
from classes import logger  # Print to command line


def main():
    """
    Main game code

    Contains pygame setup and the main game loop
    """
    pygame.init()  # Initialise pygame
    logger.log("Init done", important=True)
    # Set window title
    screen = pygame.display.set_mode((900, 600))  # Set window size
    logger.log("Set title", important=True)

    misc.display_text(screen, "loading...", 28, (20, 20))
    pygame.display.update()  # Update to loading screen
    logger.log("Loading screen", important=True)

    pygame.display.set_caption(
        "Ants: An Artificial Intelligence Experiment by C7")
    logger.log("Set title", important=True)
    done = False  # The game loop is broken when done becomes True

    # Load background image resource
    bg = pygame.image.load("images/bg01a.jpg")
    logger.log("Loaded background image", important=True)

    initial_holes = 7  # Number to be initially generated
    hole_list = [hole_class.Hole() for i in range(initial_holes)]
    logger.log("Generated {} holes".format(str(initial_holes)), important=True)
    initial_ants = 0
    ant_list = [ant_class.Ant() for i in range(initial_ants)]
    logger.log("Generated {} ants".format(str(initial_ants)), important=True)
    initial_sugar = 0
    sugar_list = [sugar_class.Sugar() for i in range(initial_sugar)]
    logger.log("Generated {} sugar".format(str(initial_sugar)),important=True)


    # Create groups for objects
    ants = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    sugar = pygame.sprite.Group()
    logger.log("Set up sprite groups", important=True)

    # Add ants_list objects to ants list
    for individual_ant in ant_list:
        ants.add(individual_ant)
    logger.log("Added ant_list contents to ants pygame.sprite.Group",
               important=True)

    for individual_hole in hole_list:
        holes.add(individual_hole)
    logger.log("Added hole_list contents to holes pygame.sprite.Group",
               important=True)

    # List of all sprites
    all_sprites = pygame.sprite.Group()
    logger.log("Created all_sprites group", important=True)
    # Add sprite groups to main group
    all_sprites.add(ants, holes, rocks, sugar)
    logger.log("Added Groups to all_sprites Group", important=True)
    # pygame clock
    clock = pygame.time.Clock()
    logger.log("Initialised clock", important=True)

    while not done:  # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If close button
                logger.log("Quitting (QUIT event)", important=True)
                done = True  # Exit
            if event.type == pygame.KEYDOWN:  # If key pressed
                if event.key == pygame.K_ESCAPE:  # If 'esc' pressed
                    logger.log("Quitting (ESC key)", important=True)
                    done = True  # Exit\
                elif event.key == pygame.K_h:  # If 'h' is pressed
                    hole_list.append(hole_class.Hole(at_mouse=True))
                    holes.add(hole_list[-1])
                elif event.key == pygame.K_s: # If 's' is pressed
                    sugar_list.append(sugar_class.Sugar())
                    sugar.add(sugar_list[-1])


        clock.tick(30)  # Frame-rate
        # Add background image, overlaying everything
        screen.blit(bg, (0, 0))

        if hole_list:  # Means 'if there are hole(s)'
            if ant_class.ants_underground > 0 and randint(0, 10) == 0:
                # Spawn new ant
                ant_list.append(ant_class.Ant())  # Add to ant list
                ants.add(ant_list[-1])  # Add it to ants sprite group
                ant_class.ants_underground -= 1  # Decrement underground count
        else:  # No holes exist
            misc.display_text(
                screen,
                "Hit 'H' to add a hole at the mouse's location",
                18, (0, 0))

        ant_list = misc.move_ants(ant_list)

        for hole in hole_list:
            hole_centre = pygame.draw.rect(screen, (0, 0, 0), (
                hole.rect.x + 30, hole.rect.y + 30, 1, 1), 1)
            for ant in ant_list:
                if ant.rect.colliderect(hole_centre) and ant.head_start == 0:
                    logger.log("Killing ant {}".format(str(ant)))
                    ant.kill()
                    ant_list.remove(ant)
                    ant_class.ants_underground += 1
                    logger.log("ants_underground incremented")

        for sugar in sugar_list:
            sugar_centre = pygame.draw.rect(screen, (0, 0, 0), (
                sugar.rect.x + 114, sugar.rect.y + 114, 1, 1), 1)
            for ant in ant_list:
                if ant.rect.colliderect(sugar_centre):
                    logger.log("Feeding ant{}".format(str(sugar)))
                    ant_class.found_food = True


                    # Draw all sprites group to the screen
        holes.draw(screen)
        sugar.draw(screen)
        ants.draw(screen)
        # Update all sprites
        all_sprites.update()

        fps_value = video.get_fps(clock)  # Get fps value
        misc.display_text(screen, "fps:" + fps_value, 14, (850, 0))

        # Update display to show changes made in current iteration
        pygame.display.update()

        # Save frame if video.video_mode
        video.save_screen(screen)


main()
