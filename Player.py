from Entity import Entity
from Assets import Assets
import pygame


class Player(Entity):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_assets = Assets()

        self.is_running = False
        self.images = player_assets.playerWalkRight
        self.idles = player_assets.playerIdle
        self.current_sprite = 0
        self.image = self.images[self.current_sprite]
        self.idle_image = self.idles[self.current_sprite]

        self.rect = self.image.get_rect()

        self.start_positionX = 500
        self.start_positionY = 900

        width, height = pygame.display.get_surface().get_size()

    def run(self):
        self.is_running = True

    def update(self):
        if self.is_running:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.images):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.images[int(self.current_sprite)]
        elif not self.is_running:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.idles):
                self.current_sprite = 0
            self.idle_image = self.idles[int(self.current_sprite)]

    def render(self, display, x, y):
        if self.is_running:
            image_size = self.image.get_size()
            big_image = pygame.transform.scale(self.image, (int(image_size[0]*2), int(image_size[1]*2)))
            display.blit(big_image, (self.start_positionX + x, self.start_positionY + y))
        else:
            idle_size = self.idle_image.get_size()
            big_idle = pygame.transform.scale(self.idle_image, (int(idle_size[0] * 2), int(idle_size[1] * 2)))
            display.blit(big_idle, (self.start_positionX + x, self.start_positionY + y))




