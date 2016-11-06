import pygame


class Ant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ant01a.png").convert_alpha()
        self.rect = self.image.get_rect()


def main():
    pygame.init()
    pygame.display.set_caption("Ants: An Artificial Intelligence Experiment by C7")
    screen = pygame.display.set_mode((900, 600))
    done = False

    # Load background image resource
    bg = pygame.image.load("images/{}.jpg".format("bg01a"))

    ant1 = Ant()

    ants = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    rocks = pygame.sprite.Group()

    ants.add(ant1)
    holes

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ants, holes, rocks)
    clock = pygame.time.Clock()

    while not done:  # Main game loop
        clock.tick(50)
        screen.blit(bg, (0, 0))

        all_sprites.draw(screen)
        all_sprites.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.update()


main()
