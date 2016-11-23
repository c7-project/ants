import pygame
import ant_class
import hole_class
import sugar_class
import rock_class
import video


def scoreboard(screen, clock, ant_list):
    """
    Displays the scoreboard on the screen
    """
    fps_value = video.get_fps(clock)  # Get fps value
    display_text(screen, "fps: " + fps_value, 14, (904, 0))
    display_text(screen, "Ants above ground: " + str(
        len(ant_list)), 14, (904, 10))
    display_text(screen, "Underground Ants: " + str(
        ant_class.ants_underground), 14, (904, 20))
    display_text(screen, "Number of holes: " + str(
        len(hole_class.hole_locations)), 14, (904, 30))
    display_text(screen, "Active sugar: " + str(
        sugar_class.active_sugar), 14, (904, 40))
    display_text(screen, "Eaten sugar: " + str(
        sugar_class.eaten_sugar), 14, (904, 50))
    display_text(screen, "Rocks: " + str(
        rock_class.number_of_rocks), 14, (904, 60))


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
