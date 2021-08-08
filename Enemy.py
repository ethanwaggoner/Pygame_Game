from Entity import Entity
import pygame


class Enemy(Entity):

    def __init__(self, health, attack, start_x, start_y):
        super().__init__(health, attack, start_x, start_y)

