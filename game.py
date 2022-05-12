#!/bin/python3
# Created by Jacobus Burger (2022), Art, Fonts, and most code structure
#   taken from the workshop.
# Info:
#   This is a cool but simple python game made with pygame.
#   I want to thank Nika for her excellent teaching skills that made
#   learning this a breeze.
#   i also want to thank Women in Computer Science and RUHacks for
#   hosting this event and inviting students of all kinds to learn.
import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RUHacks 6 PyGame Demo (with Nika)")

clock = pygame.time.Clock()
game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
bigg_font = pygame.font.Font("font/Pixeltype.ttf", 100)

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

gameover_surface = bigg_font.render("GAME OVER", False, "Black")
commmand_surface = game_font.render("Press SPACE", False, "Black")

snail_surface = pygame.image.load("graphics/snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("graphics/player_walk.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

game_active = True
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        snail_rect.x -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill("grey")
        screen.blit(gameover_surface, (250, 150))
        screen.blit(commmand_surface, (300, 200))

    pygame.display.update()
    pygame.time.Clock().tick(60)
