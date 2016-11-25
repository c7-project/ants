import os  # loads built in python module
import pygame  # loads downloaded module  

video_mode = False  # If true, frames are saved

current_frame = 1  # Show what the current is 
path_checked = False  # checks if file exist in python 


def save_screen(screen):
    """
    If test_mode is True, an image of `screen` is saved
    """
    if not video_mode:
        return False
    global current_frame  # current_frame is available outside the scope of the function
    global path_checked  # path_checked is available outside the scope of the function
    frames_directory = os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__))) + "\\frames\\"
    if not path_checked:
        check_folder(frames_directory)
    pygame.image.save(
        screen,
        frames_directory + "ants-frame{}.jpeg".format(
            str(current_frame).zfill(4)))
    current_frame += 1  # add the frame rate by 1 


def check_folder(directory):
    """
    Check 'frames' folder exists. If not, create it
    """
    global path_checked
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        path_checked = True 


def get_fps(clock): 
    """
    Return the FPS, or if video_mode is true, return the video FPS

    :param clock: The pygame clock object
    :return: The FPS
    """
    if video_mode:
        return "30"
    else:
        return str(int(round(clock.get_fps(), 0)))
