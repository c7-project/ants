import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 600))

bg = pygame.image.load("images/{}.jpg".format("bg01a"))

pygame.display.set_caption("Test Thing - James")
clock = pygame.time.Clock()


class Ant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ant01a.png").convert_alpha()
        self.rect = self.image.get_rect()

x, y = 450, 300
move_x, move_y = 0, 0

ants = pygame.sprite.Group()
ant1 = Ant()
ants.add(ant1)


while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_x = -2
            elif event.key == pygame.K_d:
                move_x = 2
            elif event.key == pygame.K_w:
                move_y = -2
            elif event.key == pygame.K_s:
                move_y = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                move_x = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                move_y = 0

    x += move_x
    y += move_y
    ant1.rect.x = x
    ant1.rect.y = y

    ants.draw(screen)
    ants.update()

    pygame.display.update()
