import pygame
import sys
import numpy as np
from PIL import Image

from pygame.locals import *

input = np.asarray(Image.open('input.png'))

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super(Tile, self).__init__()

        self.surf = pygame.Surface((input[0], input[1]))

