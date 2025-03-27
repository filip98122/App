import os
import pygame
import random
import math
import time
import json
from cryptography.fernet import Fernet
pygame.init()
pygame.joystick.init()
pygame.mixer.init()
keys = pygame.key.get_pressed()
keyE = b'nL5cTPi0324Gk2zgRDR6E4Y2iVHfWnrKu4kGzcB1ZnU='
clock = pygame.time.Clock()
WIDTH,HEIGHT = 1540,900
window = pygame.display.set_mode((WIDTH,HEIGHT))
tilewh=HEIGHT/15