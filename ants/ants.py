import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    done = False

    # Load background image resource
    bg = pygame.image.load("images/{}.jpg".format("bg01a"))
    screen.blit(bg, (0, 0))  # Might have to be moved to game loop

    while not done:  # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.update()

main()
