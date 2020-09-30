import pygame
from pygame import mixer
from player import *
from enemy import *
from bullet import *

# ---------------------------------------------------------------- Initialize PyGame
pygame.init()


# ---------------------------------------------------------------- Game Window

# Window Dimensions
window_width, window_height = 1200, 720
window = pygame.display.set_mode((window_width, window_height))

# Window Title
window_title = "Space Invaders"
pygame.display.set_caption(window_title)

# Window Icon
game_icon_path = "imgs/game_icon.png"
game_icon = pygame.image.load(game_icon_path)
pygame.display.set_icon(game_icon)

# Window Background
bg_img_path = "imgs/bg.jpg"
bg = pygame.image.load(bg_img_path)


# ---------------------------------------------------------------- Player Instantiation
player_speed = 6
player = Player(window_width // 2 - 32, window_height // 1.4)


# ---------------------------------------------------------------- Enemies Instantiation
enemies_count = 10
enemies = []
for i in range(enemies_count):
    enemy = Enemy(window_width, window_height)
    enemies.append(enemy)


# ---------------------------------------------------------------- Bullet Instantiation
bullet = Bullet(player)


# ---------------------------------------------------------------- Score
score_font = pygame.font.Font("freesansbold.ttf", 32)


def render_score(score_value):
    score_position = 32, 32
    score = score_font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, score_position)


# ---------------------------------------------------------------- Game Over
game_over_font = pygame.font.Font("freesansbold.ttf", 72)


def game_over():
    position = window_width // 2 - 70 * 3, window_height // 2 - 70 * 3
    text = game_over_font.render("Game Over!", True, (255, 255, 255))
    window.blit(text, position)


# ---------------------------------------------------------------- Sounds
mixer.music.load("sfx/background.wav")
mixer.music.play(-1)

hit_sound = mixer.Sound("sfx/hit.wav")
bullet_sound = mixer.Sound("sfx/bullet.wav")
over_sound = mixer.Sound("sfx/over.wav")


# ---------------------------------------------------------------- Game Loop
score_value = 0
game_state = "running"
while True:

    # Events Handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player.dx -= player_speed

            if e.key == pygame.K_RIGHT:
                player.dx += player_speed

            if e.key == pygame.K_UP:
                player.dy -= player_speed

            if e.key == pygame.K_DOWN:
                player.dy += player_speed

            if e.key == pygame.K_SPACE:
                if bullet.state == "ready":
                    bullet = Bullet(player)
                    bullet.state = "fired"
                    bullet_sound.play()

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                player.dx += player_speed

            if e.key == pygame.K_RIGHT:
                player.dx -= player_speed

            if e.key == pygame.K_UP:
                player.dy += player_speed

            if e.key == pygame.K_DOWN:
                player.dy -= player_speed

    # Update Screen
    bg_color = (0, 0, 0)
    window.fill(bg_color)
    window.blit(bg, (0, 0))

    # Player Collision
    for enemy in enemies:
        if player.enemy_collision(enemy):
            over_sound.play()

            for e in enemies:
                e.despawn()

            game_state = "over"
            break

    # Bullet Collision
    for enemy in enemies:
        if not enemy.bullet_collision(bullet):
            enemy.render(window, window_width, window_height)
        else:
            score_value += 1
            hit_sound.play()
            bullet = Bullet(player)
            enemy.respawn()

    render_score(score_value)

    bullet.render(window)
    player.render(window, window_width, window_height)

    if game_state == "over":
        game_over()

    pygame.display.update()
