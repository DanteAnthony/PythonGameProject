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

# Run Loop
run = True
while run:
    
    CLOCK.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()