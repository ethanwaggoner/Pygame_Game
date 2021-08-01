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
posX = 0
posY = 0
velocity = 8
jumpHeight = 10

Assets = Assets()
Background1 = Background(Assets.Level1, displaySurface)
Player = Player()


def draw():
    Background1.render()
    Player.render_player(displaySurface, posX, posY)
    Player.update()
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


boole = True
while boole:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boole = False

    keys = pygame.key.get_pressed()
    playerX = Player.get_x(Player.start_positionX, posX)
    playerY = Player.get_y(Player.start_positionY, posY)

    if keys[pygame.K_d] and playerX < 1920 - Player.player_width:
        posX += velocity
        Player.run_right()
    if keys[pygame.K_a] and playerX > 0 + Player.player_width:
        posX -= velocity
        Player.run_left()
    if keys[pygame.K_w] and playerY > 0 + Player.player_height:
        Player.jump()
        if jumpHeight >= -10:
            posY -= (jumpHeight * abs(jumpHeight)) * 0.5
            jumpHeight -= 1
    else:
        # if the player isn't on the ground, return at a speed of 20
        jumpHeight = 10
        if posY <= 0:
            posY += 20

    draw()
