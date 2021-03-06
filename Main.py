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
resolutionObject = pygame.display.Info()
displaySurface = pygame.display.set_mode((resolutionObject.current_w, resolutionObject.current_h))
displaySurface.fill((255, 255, 255))
playerPosX, playerPosY = 0, 0
enemy1PosX, enemy1PosY = 0, 0
velocity = 10
jumpHeight = 10
level = 1

Assets = Assets()
Player = Player(100, 25, 500, 850, Assets)
Enemy1 = Enemy(50, 20, 1050, 600, Assets)
Background1 = Background(Assets.Level1, displaySurface)
Background2 = Background(Assets.Level2, displaySurface)


def draw(background, get_level):
    background.render()
    Player.render_player(displaySurface, playerPosX, playerPosY)
    Player.update()
    if get_level == 2:
        Enemy1.render_enemy(displaySurface, enemy1PosX, enemy1PosY)
        Enemy1.update()
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


boole = True
while boole:

    keys = pygame.key.get_pressed()
    playerCords = Player.get_cords(playerPosX, playerPosY)
    enemyCords = Enemy1.get_cords(enemy1PosX, enemy1PosY)

    if level == 1:
        draw(Background1, level)
    elif level == 2:
        draw(Background2, level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boole = False

    if keys[pygame.K_d] and playerCords[0] < 1850:
        playerPosX += velocity
        Player.run_right()
    if keys[pygame.K_a] and playerCords[0] > -100:
        playerPosX -= velocity
        Player.run_left()
    if keys[pygame.K_w] and playerCords[1] > 0 + Player.player_height:
        Player.jump()
        if jumpHeight >= -10:
            playerPosY -= (jumpHeight * abs(jumpHeight)) * 0.5
            jumpHeight -= 1
    else:
        #  gravity
        jumpHeight = 10
        if playerPosY <= 0:
            playerPosY += 50

    if playerCords[0] >= 1850 and level == 1:
        Player.start_x = -1350
        Player.start_y = 750
        level = 2
    elif playerCords[0] < 0 and level == 2:
        Player.start_x = 500
        Player.start_y = 850
        level = 1

    if enemyCords[0] - 100 >= playerCords[0]:
        enemy1PosX -= 3
        Enemy1.run_left()
    elif enemyCords[0] + 100 <= playerCords[0]:
        enemy1PosX += 3
        Enemy1.face_right()
        Enemy1.run_right()

    #  print("Player X: " + str(playerCords[0]))
    #  print("Enemy1 X: " + str(enemyCords[0]))




