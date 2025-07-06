import pygame
import random
from settings import screen, WIDTH, HEIGHT, player_size, enemy_size

player_img = pygame.image.load("assets/rocket.png")
enemy_img = pygame.image.load("assets/alienship.png")

enemy_list = []

def draw_player(pos):
    screen.blit(pygame.transform.scale(player_img, (player_size, player_size)), pos)

def drop_enemies(enemy_list, chance):
    if random.random() < chance:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append({"pos": [x_pos, 0]})

def update_enemy_positions(enemy_list, speed):
    for enemy in enemy_list:
        enemy["pos"][1] += speed

def draw_enemies(enemy_list):
    for enemy in enemy_list:
        x, y = enemy["pos"]
        screen.blit(pygame.transform.scale(enemy_img, (enemy_size, enemy_size)), (x, y))

def collision_check(player_pos, enemies):
    padding = 12  

    px, py = player_pos
    player_rect = pygame.Rect(
        px + padding,
        py + padding,
        player_size - 2 * padding,
        player_size - 2 * padding
    )

    for enemy in enemies:
        ex, ey = enemy["pos"]
        enemy_rect = pygame.Rect(
            ex + padding,
            ey + padding,
            enemy_size - 2 * padding,
            enemy_size - 2 * padding
        )
        if player_rect.colliderect(enemy_rect):
            return True
    return False
