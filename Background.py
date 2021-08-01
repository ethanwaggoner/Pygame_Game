import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, background, surface):
        super().__init__()
        self.background = background
        self.surface = surface
        self.backgroundImg = pygame.image.load(background).convert()
        self.rectBackgroundImg = self.backgroundImg.get_rect()
        self.backgroundY = 0
        self.backgroundX = 0

    def render(self):
        self.surface.blit(self.backgroundImg, (self.backgroundX, self.backgroundY))
