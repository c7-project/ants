verbose = True


def log(text, important=False):
    if verbose or important:
        print text
