from Player import Player
from Enemy import Enemy
from Menu import Menu
from Background import Background
from Assets import Assets
import pygame
import sys

pygame.init()
FPS = 60
FPS_CLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((1920, 1080))
displaySurface.fill((255, 255, 255))
startX = 0
startY= 0

Assets = Assets()
Background1 = Background(Assets.Level1, displaySurface)
Player = Player()

boole = True
while boole:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                startX += 10
            if event.key == pygame.K_a:
                startX -= 10
            if event.key == pygame.K_w:
                startY -= 10
            if event.key == pygame.K_s:
                startY += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass

    displaySurface.fill((255, 255, 255))
    Background1.render()
    Player.render(displaySurface, startX, startY)
    pygame.display.update()
    FPS_CLOCK.tick(FPS)
