import pygame


class Assets:
    def __init__(self):
        self.Level1 = "Assets/Backgrounds/Level1.png"
        self.Level2 = "Assets/Backgrounds/Level2.jpg"

        self.playerIdle = [pygame.image.load("Assets/Player/Idle/adventurer-idle-2-00.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Idle/adventurer-idle-2-01.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Idle/adventurer-idle-2-02.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Idle/adventurer-idle-2-03.png").convert_alpha()]

        self.playerWalkRight = [pygame.image.load("Assets/Player/Walk_Right/adventurer-run-00.png").convert_alpha(),
                                pygame.image.load("Assets/Player/Walk_Right/adventurer-run-01.png").convert_alpha(),
                                pygame.image.load("Assets/Player/Walk_Right/adventurer-run-02.png").convert_alpha(),
                                pygame.image.load("Assets/Player/Walk_Right/adventurer-run-03.png").convert_alpha(),
                                pygame.image.load("Assets/Player/Walk_Right/adventurer-run-04.png").convert_alpha(),
                                pygame.image.load("Assets/Player/Walk_Right/adventurer-run-05.png").convert_alpha()]




