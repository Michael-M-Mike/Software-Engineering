import pygame
from random import randint, choice
from math import sqrt

enemy_img_path = "imgs/enemy.png"
enemy_img_square = 96
enemy_img = pygame.image.load(enemy_img_path)

enemy_max_speed = 4


class Enemy:

    def __init__(self, surface_width, surface_height):
        self.surface_width = surface_width
        self.surface_height = surface_height

        self.x = randint(0, surface_width)
        self.y = randint(0, surface_height // 2)

        self.dx = choice([-enemy_max_speed, enemy_max_speed])
        self.dy = 0

        self.despawned = False

    def render(self, surface, surface_width, surface_height):
        self.update_pos(surface_width, surface_height)
        surface.blit(enemy_img, (self.x, self.y))

    def update_pos(self, surface_width, surface_height):

        if not self.despawned:
            self.x += self.dx
            self.y += self.dy

            # Right Boundary
            if self.x >= surface_width - enemy_img_square:
                self.x = surface_width - enemy_img_square

                self.dx = -self.dx
                self.dy = choice([-enemy_max_speed / 5, 0, enemy_max_speed / 5])

            # Left Boundary
            if self.x <= 0:
                self.x = 0

                self.dx = -self.dx
                self.dy = choice([-enemy_max_speed / 5, 0, enemy_max_speed / 5])

            # Lower Boundary
            if self.y >= surface_height - enemy_img_square:
                self.y = surface_height - enemy_img_square

                self.dx = -self.dx
                self.dy = choice([-enemy_max_speed / 5, 0, enemy_max_speed / 5])

            # Upper Boundary
            if self.y <= 0:
                self.y = 0

                self.dx = -self.dx
                self.dy = choice([-enemy_max_speed / 5, 0, enemy_max_speed / 5])

    def bullet_collision(self, bullet):

        distance = sqrt(pow(self.x - bullet.x, 2) + pow(self.y - bullet.y, 2))
        return distance < 32

    def respawn(self):
        self.__init__(self.surface_width, self.surface_height)

    def despawn(self):
        self.x = self.surface_width
        self.y = self.surface_height

        self.dx = 0
        self.dy = 0

        self.despawned = True