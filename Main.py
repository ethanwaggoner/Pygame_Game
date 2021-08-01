from Player import Player
from Enemy import Enemy
from Menu import Menu
from Background import Background
from Assets import Assets
import pygame

pygame.init()
pygame.display.set_caption("Yo")
FPS = 60
FPS_CLOCK = pygame.time.Clock()
displaySurface = pygame.display.set_mode((1920, 1080))
displaySurface.fill((255, 255, 255))
startX = 0
startY = 0
velocity = 10
walkCount = 0


Assets = Assets()
Background1 = Background(Assets.Level1, displaySurface)
Player = Player()


def draw():
    displaySurface.fill((255, 255, 255))
    Background1.render()
    Player.render_player(displaySurface, startX, startY)
    Player.update()
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


boole = True
while boole:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            boole = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        startX += velocity
        Player.run()
    elif keys[pygame.K_a]:
        startX -= velocity
        Player.run()

    draw()
