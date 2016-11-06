import pygame


class Ant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.initial_image = pygame.image.load("images/ant01a.png").convert_alpha()
        self.current_rotation = 0
        self.image = self.initial_image
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 5

    def rotate(self, angle):
        self.current_rotation += angle
        self.image = rot_center(self.initial_image, self.current_rotation)


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


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
        clock.tick(60)
        screen.blit(bg, (0, 0))

        ant1.rotate(4)

        all_sprites.draw(screen)
        all_sprites.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True

        pygame.display.update()


main()
