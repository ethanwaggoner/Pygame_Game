from Entity import Entity
from Assets import Assets
import pygame


class Player(Entity):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_assets = Assets()

        self.is_running = False
        self.player_walk = player_assets.playerWalkRight
        self.idles = player_assets.playerIdle
        self.current_sprite = 0
        self.image = self.player_walk[self.current_sprite]
        self.idle_image = self.idles[self.current_sprite]

        self.start_positionX = 500
        self.start_positionY = 850

        width, height = pygame.display.get_surface().get_size()

    @staticmethod
    def resize(image, scaling):
        image_size = image.get_size()
        return pygame.transform.scale(image, (int(image_size[0] * scaling), int(image_size[1] * scaling)))

    def run(self):
        self.is_running = True

    def update(self):
        if self.is_running:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.player_walk):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.player_walk[int(self.current_sprite)]
        elif not self.is_running:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.idles):
                self.current_sprite = 0
            self.idle_image = self.idles[int(self.current_sprite)]

    def render_player(self, display, x, y):
        if self.is_running:
            big_image = self.resize(self.image, 3)
            display.blit(big_image, (self.start_positionX + x, self.start_positionY + y))
        else:
            big_idle = self.resize(self.idle_image, 3)
            display.blit(big_idle, (self.start_positionX + x, self.start_positionY + y))




