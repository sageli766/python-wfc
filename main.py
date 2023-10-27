import pygame
import sys
import numpy as np
from PIL import Image
import os

from pygame.locals import *

os.chdir('python-wfc')
input = pygame.image.load('input.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super(Tile, self).__init__()

        self.surf = input
        self.rect = self.surf.get_rect()

        self.wavefunction = {}


pygame.init()

screen = pygame.display.set_mode((800,600))

gameOn = True

tile1 = Tile()
tile2 = Tile()
tile3 = Tile()
tile4 = Tile()

while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

    screen.blit(tile1.surf, (40, 40))
    screen.blit(tile2.surf, (40, 530))
    screen.blit(tile3.surf, (730, 40))
    screen.blit(tile4.surf, (730, 530))

    pygame.display.flip()