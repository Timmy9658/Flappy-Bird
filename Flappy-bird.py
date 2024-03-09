import pygame
import time

window_height, window_width = 700, 700
class space(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load("Flappy.png")

pygame.display.set_mode((window_height, window_width))
bird = space()
time.sleep(1)
pygame.init()