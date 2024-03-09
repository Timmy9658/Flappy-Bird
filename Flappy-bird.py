import pygame
import time
pygame.init()
window_height, window_width = 700, 700
player_x, player_y = 200,200
game = True
class space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Flappy.png")
        print(self.image)
        self.rect = self.image.get_rect()
    def movement(self):
        self.rect.y += 1
screen = pygame.display.set_mode((window_height, window_width))
screen.fill((0,0,0))
bird = space()
screen.blit(bird.image, (player_x,player_y))
while game == True:
    bird.movement()
    screen.blit(bird.image, (player_x, bird.rect.y))
    pygame.display.update()
    pygame.time.Clock().tick(60)