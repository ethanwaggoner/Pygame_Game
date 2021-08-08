from Entity import Entity
import pygame


class Player(Entity):

    def __init__(self, health, attack, start_x, start_y, player_assets: object):
        super().__init__(health, attack, start_x, start_y)

        self.player_assets = player_assets

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

    def run_right(self):
        self.is_running_right = True

    def run_left(self):
        self.is_running_left = True

    def jump(self):
        self.is_jumping = True

    def animate(self, image_list):
        self.current_sprite += 0.15
        if self.current_sprite >= len(image_list):
            self.current_sprite = 0

    def update(self):
        if self.is_running_right:
            self.animate(self.player_walk)
            self.image = self.player_walk[int(self.current_sprite)]
            self.is_running_right = False
        if self.is_running_left:
            self.animate(self.player_walk)
            self.image = pygame.transform.flip(self.player_walk[int(self.current_sprite)], True, False)
            self.is_running_left = False
        if self.is_jumping:
            self.is_jumping = False
        if not self.is_running_right and not self.is_running_left and not self.is_jumping:
            self.animate(self.idles)
            self.idle_image = self.idles[int(self.current_sprite)]

    def render_player(self, display, x, y):
        if self.is_running_right or not (not self.is_running_left or self.is_jumping):
            big_image = self.resize(self.image, self.scaling)
            display.blit(big_image, (self.start_x + x, self.start_y + y))

        elif self.is_jumping:
            big_jump = self.resize(self.jump_image, self.scaling)
            display.blit(big_jump, (self.start_x + x, self.start_y + y))

        elif not self.is_running_right or self.is_running_left and not self.is_jumping:
            big_idle = self.resize(self.idle_image, self.scaling)
            display.blit(big_idle, (self.start_x + x, self.start_y + y))
