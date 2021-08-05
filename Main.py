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
velocity = 10
jumpHeight = 10
level = 1

Assets = Assets()
Player = Player(Assets)
Background1 = Background(Assets.Level1, displaySurface)
Background2 = Background(Assets.Level2, displaySurface)


def draw(background):
    background.render()
    Player.render_player(displaySurface, posX, posY)
    Player.update()
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


boole = True
while boole:

    keys = pygame.key.get_pressed()
    playerX = Player.get_x(Player.start_positionX, posX)
    playerY = Player.get_y(Player.start_positionY, posY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boole = False

    if keys[pygame.K_d] and playerX < 1850:
        posX += velocity
        Player.run_right()
    if keys[pygame.K_a] and playerX > -100:
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

    if level == 1:
        draw(Background1)
    elif level == 2:
        draw(Background2)

    if playerX >= 1850 and level == 1:
        Player.start_positionX = -1350
        Player.start_positionY = 750
        level = 2
    elif playerX < 0 and level == 2:
        Player.start_positionX = 500
        Player.start_positionY = 850
        level = 1

