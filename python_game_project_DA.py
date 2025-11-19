# Pygame Setup
import pygame
from pygame import *

pygame.init()

# Screen Setup
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('BeanForm')

# Constants
CLOCK = pygame.time.Clock()
FPS = 60

# Variables

# Functions

# Classes
class Bean(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Beanman128.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
    
    def update(self):
        self.apply_gravity()

        if self.rect.bottom > 900:
            self.kill()

    def apply_gravity(self):
        self.vel += 0.5
        if self.vel > 20:
            self.vel = 20
        self.rect.y += int(self.vel)

# Groups
player_group = pygame.sprite.Group()

player = Bean(int(SCREEN_WIDTH / 2), 100)
player_group.add(player)

# Run Loop
run = True
while run:
    
    CLOCK.tick(FPS)

    SCREEN.fill((0, 0, 0))
    player_group.draw(SCREEN)
    player_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()