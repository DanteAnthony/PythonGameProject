# Pygame Setup
import pygame
from pygame import *

pygame.init()

# Screen Setup
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bean')

# Constants
CLOCK = pygame.time.Clock()
FPS = 60

# Variables

# Functions

# Classes
class Bean(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Bean2.png').convert_alpha()
        self.rect = self.image.get_rect(center = [x, y])
        self.vel_y = 0
        self.speed = 9
        self.on_ground = True
        self.facing_right = True
    
    def update(self):
        # Self Functions
        self.apply_gravity()
        self.handle_movement()
        self.handle_jumping()

        # Ground Collision (for now)
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.on_ground = True
        elif self.rect.bottom < 600:
            self.on_ground = False

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.flip_sprite(False)
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.flip_sprite(True)
            self.rect.x += self.speed

    def handle_jumping(self):
        keys = pygame.key.get_pressed()
        if self.on_ground == True:
            if keys[pygame.K_SPACE]:
                self.on_ground = False
                self.vel_y = -15
            else:
                self.on_ground = True

    def flip_sprite(self, new_direction_right):
        if new_direction_right and not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = True
        elif not new_direction_right and self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False

    def apply_gravity(self):
        self.vel_y += 0.98
        if self.vel_y > 20:
            self.vel_y = 20
        self.rect.y += int(self.vel_y)

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Rect.png').convert_alpha()
        self.rect = self.image.get_rect(center = [x, y])
        self.vel = 0
        self.speed = 9
        self.on_ground = True
        self.facing_right = True
    
    def update(self):
        # Self Functions
        self.apply_gravity()

        # Ground Collision (for now)
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.on_ground = True
        elif self.rect.bottom < 600:
            self.on_ground = False

        # Flip Sprite
        if self.facing_right == False:
            self.flipped_img = pygame.transform.flip(self.image, True, False)
        elif self.facing_right == True:
            pass

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.flip_sprite(False)
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.flip_sprite(True)
            self.rect.x += self.speed

    def handle_jumping(self):
        keys = pygame.key.get_pressed()
        if self.on_ground == True:
            if keys[pygame.K_SPACE]:
                self.on_ground = False
                self.vel = -15
            else:
                self.on_ground = True

    def flip_sprite(self, new_direction_right):
        if new_direction_right and not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = True
        elif not new_direction_right and self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False

    def apply_gravity(self):
        self.vel += 0.98
        if self.vel > 20:
            self.vel = 20
        self.rect.y += int(self.vel)

# Groups
player_group = pygame.sprite.Group()

player = Bean(int(SCREEN_WIDTH / 2), 100)
player_group.add(player)

enemy_group = pygame.sprite.Group()

enemy = Rect(int(SCREEN_WIDTH / 3), 100)
enemy_group.add(enemy)

# Run Loop
run = True
while run:
    
    CLOCK.tick(FPS)

    SCREEN.fill((72, 72, 72))
    player_group.draw(SCREEN)
    player_group.update()
    enemy_group.draw(SCREEN)
    enemy_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()