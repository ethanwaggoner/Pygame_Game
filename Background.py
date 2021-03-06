import pygame


class Background:
    def __init__(self, background, surface):
        self.background = background
        self.surface = surface
        self.rectBackgroundImg = self.background.get_rect()
        self.backgroundY = 0
        self.backgroundX = 0

    def render(self):
        self.surface.blit(self.background, (self.backgroundX, self.backgroundY))
