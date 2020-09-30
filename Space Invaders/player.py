import pygame
from math import sqrt

player_img_path = "imgs/player.png"
player_img_square = 64
player_img = pygame.image.load(player_img_path)


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dx = 0
        self.dy = 0

    def render(self, surface, surface_width, surface_height):
        self.update_pos(surface_width, surface_height)
        surface.blit(player_img, (self.x, self.y))

    def update_pos(self, surface_width, surface_height):
        self.x += self.dx
        self.y += self.dy

        if self.x >= surface_width - player_img_square:
            self.x = surface_width - player_img_square

        if self.x <= 0:
            self.x = 0

        if self.y >= surface_height - player_img_square:
            self.y = surface_height - player_img_square

        if self.y <= 0:
            self.y = 0

    def enemy_collision(self, enemy):
        distance = sqrt(pow(self.x - enemy.x, 2) + pow(self.y - enemy.y, 2))
        return distance < 32
