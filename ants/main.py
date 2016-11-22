import pygame

from classes import ant_class  # Ant
from classes import hole_class  # Hole
from classes import sugar_class  # Sugar
from classes import rock_class  # Rock
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

    initial_holes = 1  # Number to be initially generated
    if initial_holes > 60:
        raise ValueError("Exceeded maximum number of random holes: 60")
    hole_list = [hole_class.Hole() for i in range(initial_holes)]
    logger.log("Generated {} holes".format(str(initial_holes)), important=True)
    ant_list = []
    sugar_list = []
    rock_list = []

    # Create groups for objects
    ants = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    sugars = pygame.sprite.Group()
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
    all_sprites.add(ants, holes, rocks, sugars)
    logger.log("Added Groups to all_sprites Group", important=True)
    # pygame clock
    clock = pygame.time.Clock()
    logger.log("Initialised clock", important=True)

    while not done:  # Main game loop
        clock.tick(32)  # Frame-rate limit

        ant_list, ants = misc.generate_new_ant(hole_list, ant_list, rock_list, ants, screen)

        ant_list = misc.move_ants(ant_list, rock_list)

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

        sugar_list, ant_list = misc.ant_sugar_collision(sugar_list, ant_list, hole_list, screen)

        # Add background image, overlaying everything
        screen.blit(bg, (0, 0))

        # Draw all sprites group to the screen
        holes.draw(screen)
        sugars.draw(screen)
        rocks.draw(screen)
        ants.draw(screen)
        # Update all sprites
        all_sprites.update()

        fps_value = video.get_fps(clock)  # Get fps value
        misc.display_text(screen, "fps: " + fps_value, 14, (843, 0))
        misc.display_text(screen, "Ants above ground: " + str(len(ant_list)), 14, (745, 10))
        misc.display_text(screen, "Underground Ants: " + str(ant_class.ants_underground), 14, (752, 20))
        misc.display_text(screen, "Number of holes: " + str(len(hole_class.hole_locations)), 14, (760, 30))
        misc.display_text(screen, "Active sugar: " + str(sugar_class.active_sugar), 14, (781, 40))
        misc.display_text(screen, "Eaten sugar: " + str(sugar_class.eaten_sugar), 14, (788, 50))
        misc.display_text(screen, "Rocks: " + str(rock_class.number_of_rocks), 14, (830, 60))
        # misc.display_text(screen, "Number of rocks:" + )

        # Update display to show changes made in current iteration
        pygame.display.update()

        # Save frame if video.video_mode
        video.save_screen(screen)

        misc.user_add_ants(ant_list, ants, rock_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If close button
                logger.log("Quitting (QUIT event)", important=True)
                done = True  # Exit

            if event.type == pygame.KEYDOWN:  # If key pressed
                if event.key == pygame.K_ESCAPE:  # If 'esc' pressed
                    logger.log("Quitting (ESC key)", important=True)
                    done = True  # Exit

                elif event.key == pygame.K_h:  # If 'h' is pressed
                    logger.log("Adding a hole")
                    hole_list.append(hole_class.Hole(at_mouse=True))
                    holes.add(hole_list[-1])

                elif event.key == pygame.K_s:  # If 's' is pressed
                    logger.log("Adding sugar")
                    sugar_list.append(sugar_class.Sugar())
                    sugars.add(sugar_list[-1])

                elif event.key == pygame.K_r:  # If 'r' is pressed
                    logger.log("Adding a rock")
                    try:
                        rock_list.append(rock_class.Rock(ant_list))
                        rocks.add(rock_list[-1])
                    except ValueError:
                        logger.log(
                            "Rock not placed - ant collision detected.",
                            important=True)

    logger.log("~~~~~ THE END ~~~~~", important=True)


main()
