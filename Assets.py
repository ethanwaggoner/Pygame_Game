import pygame


class Assets:
    def __init__(self):
        self.Level1 = pygame.image.load("Assets/Backgrounds/Level1.png").convert()
        self.Level2 = pygame.image.load("Assets/Backgrounds/Level2.png").convert()

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

        self.playerJump = [pygame.image.load("Assets/Player/Jump/adventurer-jump-00.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Jump/adventurer-jump-01.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Jump/adventurer-jump-02.png").convert_alpha(),
                           pygame.image.load("Assets/Player/Jump/adventurer-jump-03.png").convert_alpha()]

        self.enemy1Idle = [pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_1.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_2.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_3.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_4.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_5.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_6.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_7.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Idle/Bringer-of-Death_Idle_8.png").convert_alpha()]

        self.enemy1Walk = [pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_1.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_2.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_3.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_4.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_5.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_6.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_7.png").convert_alpha(),
                           pygame.image.load("Assets/Enemies/Enemy1Walk/Bringer-of-Death_Walk_8.png").convert_alpha()]


