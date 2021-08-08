from Entity import Entity
import pygame


class Enemy(Entity):

    def __init__(self, health, attack, start_x, start_y, enemy_assets: object):
        super().__init__(health, attack, start_x, start_y)
        self.health = health
        self.attack = attack
        self.start_x = start_x
        self.start_y = start_y

        self.idle_list = enemy_assets.enemy1Idle
        self.walk_list = enemy_assets.enemy1Walk

    def update(self):
        pass

    def render_enemy(self, display, x, y):
        pass
