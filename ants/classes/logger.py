verbose = False  # By default, limit output to only important information
# verbose can be made True for debugging


def log(text, important=False):
    """
    Log stuff to the command line
    """
    if verbose or important:
        print(text)
