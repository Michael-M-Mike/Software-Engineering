import pygame

bullet_img_path = "imgs/bullet.png"
bullet_img_square = 64
bullet_img = pygame.image.load(bullet_img_path)

bullet_speed = 14


class Bullet:

    def __init__(self, player):
        self.x = player.x
        self.y = player.y

        self.dy = -bullet_speed

        self.state = "ready"

    def render(self, surface):

        if self.state == "fired":
            self.update_pos()
            surface.blit(bullet_img, (self.x, self.y))

    def update_pos(self):
        self.y += self.dy

        if self.y < 0:
            self.state = "ready"
