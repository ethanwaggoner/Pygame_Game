import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, health, attack, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.attack = attack
        self.start_x = start_x
        self.start_y = start_y

    def get_cords(self, x, y):
        return self.start_x + x, self.start_y + y

    @staticmethod
    def resize(image, scaling) -> object:
        image_size = image.get_size()
        return pygame.transform.scale(image, (int(image_size[0] * scaling), int(image_size[1] * scaling)))


