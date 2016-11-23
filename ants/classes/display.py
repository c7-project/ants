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
    x_left = 965
    y_offset = 58
    fps_value = video.get_fps(clock)  # Get fps value
    display_text(screen, fps_value, 14, (x_left, y_offset + 0))
    display_text(screen, str(len(ant_list)), 14, (x_left, y_offset + 40))  # Ants on ground
    display_text(screen, str(ant_class.ants_underground), 14, (x_left, y_offset + 80))  # Ants underground
    display_text(screen, str(len(hole_class.hole_locations)), 14, (x_left, y_offset + 120))  # Number of holes
    display_text(screen, str(rock_class.number_of_rocks), 14, (x_left, y_offset + 160))  # Number of rocks
    display_text(screen, str(sugar_class.active_sugar), 14, (x_left, y_offset + 200))  # Active sugar
    display_text(screen, str(sugar_class.eaten_sugar), 14, (x_left, y_offset + 240))  # Sugar found


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
