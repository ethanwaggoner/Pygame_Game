from Entity import Entity
from Assets import Assets
import pygame


class Player(Entity):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_assets = Assets()

        self.images = player_assets.playerIdle
        self.convimages = []
        self.start_positionX = 500
        self.start_positionY = 900

        width, height = pygame.display.get_surface().get_size()

        for image in self.images:
            image = pygame.image.load(image).convert_alpha()
            self.convimages.append(image)

    def render(self, display, x, y):
        display.blit(self.convimages[0], (self.start_positionX + x, self.start_positionY + y))


