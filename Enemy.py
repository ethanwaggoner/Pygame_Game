from Entity import Entity
import pygame


class Enemy(Entity):

    def __init__(self, health, attack, start_x, start_y, enemy_assets: object):
        super().__init__(health, attack, start_x, start_y)

        self.health = health
        self.attack = attack
        self.start_x = start_x
        self.start_y = start_y

        self.attack_list = enemy_assets.enemy1Att
        self.walk_list = enemy_assets.enemy1Walk

        self.current_sprite = 0
        self.scaling = 3

        self.idle_image = self.attack_list[self.current_sprite]
        self.attack_image = self.walk_list[self.current_sprite]

    def animate(self, image_list):
        self.current_sprite += 0.15
        if self.current_sprite >= len(image_list):
            self.current_sprite = 0

    def update(self):
        if self.is_running_left:
            self.animate(self.walk_list)
            self.attack_image = self.walk_list[int(self.current_sprite)]
            self.is_running_left = False
        if self.is_running_right:
            self.animate(self.walk_list)
            self.attack_image = pygame.transform.flip(self.walk_list[int(self.current_sprite)], True, False)
            self.is_running_right = False
        if not self.is_running_right and not self.is_running_left and not self.is_facing_right:
            self.animate(self.attack_list)
            self.idle_image = self.attack_list[int(self.current_sprite)]
        elif not self.is_running_right and not self.is_running_left and self.is_facing_right:
            self.animate(self.attack_list)
            self.idle_image = pygame.transform.flip(self.attack_list[int(self.current_sprite)], True, False)
            self.idle_image = self.attack_list[int(self.current_sprite)]
            self.is_facing_right = False

    def render_enemy(self, display, x, y):
        if self.is_running_right or self.is_running_left:
            big_image = self.resize(self.attack_image, self.scaling)
            display.blit(big_image, (self.start_x + x, self.start_y + y))
        elif not self.is_running_right or self.is_running_left:
            big_idle = self.resize(self.idle_image, self.scaling)
            display.blit(big_idle, (self.start_x + x, self.start_y + y))
