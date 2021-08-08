import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, health, attack, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.attack = attack
        self.start_x = start_x
        self.start_y = start_y

        self.is_running_right = False
        self.is_running_left = False
        self.is_jumping = False
        self.is_facing_right = False

    def get_cords(self, x, y):
        return self.start_x + x, self.start_y + y

    def run_right(self):
        self.is_running_right = True

    def run_left(self):
        self.is_running_left = True

    def jump(self):
        self.is_jumping = True

    def face_right(self):
        self.is_facing_right = True

    @staticmethod
    def resize(image, scaling):
        image_size = image.get_size()
        return pygame.transform.scale(image, (int(image_size[0] * scaling), int(image_size[1] * scaling)))


