from Entity import Entity
from Assets import Assets
import pygame


class Player(Entity):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_assets = Assets()

        self.is_running_right = False
        self.is_running_left = False
        self.is_jumping = False

        self.player_walk = player_assets.playerWalkRight
        self.idles = player_assets.playerIdle
        self.jump_list = player_assets.playerJump

        self.current_sprite = 0

        self.image = self.player_walk[self.current_sprite]
        self.idle_image = self.idles[self.current_sprite]
        self.jump_image = self.jump_list[self.current_sprite]

        self.scaling = 3
        self.player_width = self.idle_image.get_width() * 2
        self.player_height = self.idle_image.get_height() * 2
        self.start_positionX = 500
        self.start_positionY = 850

    @staticmethod
    def get_x(start_x, x):
        return start_x + x

    @staticmethod
    def get_y(start_y, y):
        return start_y + y

    @staticmethod
    def resize(image, scaling):
        image_size = image.get_size()
        return pygame.transform.scale(image, (int(image_size[0] * scaling), int(image_size[1] * scaling)))

    def run_right(self):
        self.is_running_right = True

    def run_left(self):
        self.is_running_left = True

    def jump(self):
        self.is_jumping = True

    def update(self):
        if self.is_running_right:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.player_walk):
                self.current_sprite = 0
                self.is_running_right = False
            self.image = self.player_walk[int(self.current_sprite)]

        if self.is_running_left:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.player_walk):
                self.current_sprite = 0
                self.is_running_left = False
            self.image = pygame.transform.flip(self.player_walk[int(self.current_sprite)], True, False)

        if self.is_jumping:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.jump_list):
                self.current_sprite = 0
                self.is_jumping = False
                self.jump_image = self.jump_list[int(self.current_sprite)]

        if not self.is_running_right and not self.is_running_left and not self.is_jumping:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.idles):
                self.current_sprite = 0
            self.idle_image = self.idles[int(self.current_sprite)]

    def render_player(self, display, x, y):
        if self.is_running_right or self.is_running_left and not self.is_jumping:
            big_image = self.resize(self.image, self.scaling)
            display.blit(big_image, (self.start_positionX + x, self.start_positionY + y))

        elif self.is_jumping:
            big_jump = self.resize(self.jump_image, self.scaling)
            display.blit(big_jump, (self.start_positionX + x, self.start_positionY + y))

        elif not self.is_running_right or self.is_running_left and not self.is_jumping:
            big_idle = self.resize(self.idle_image, self.scaling)
            display.blit(big_idle, (self.start_positionX + x, self.start_positionY + y))
