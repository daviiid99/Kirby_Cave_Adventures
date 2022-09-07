import os
import random
import pygame
import time
from datetime import date
from datetime import datetime
import os.path
import threading 

## App icon
#icon = pygame.image.load('Assets/background/title_screen/logo.png')
#pygame.display.set_icon(icon)


## Map Values
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1000, 790 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kirby Cave Adventures")
WHITE = "#ffffff"

# Stages
cave = pygame.transform.scale(pygame.image.load(os.path.join("assets/backgrounds", "cave.png")), (WIDTH, HEIGHT))

# Title screen
logo = pygame.transform.scale(pygame.image.load(os.path.join("assets/logo", "title_screen.png")) , (800, 320))
press = pygame.image.load(os.path.join("assets/logo", "press.png"))


# Kirby

#Walking right
kirby_default_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/right', 'default.png')), (80, 72))
kirby_right_right_foot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/right', 'right_foot.png')), (80, 72))
kirby_right_left_foot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/right', 'left_foot.png')), (80,72))
kirby_right_all_foots = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/right', 'all_foots.png')), (80, 72))

#Walking left
kirby_default_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/left', 'default.png')), (80, 72))
kirby_left_right_foot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/left', 'right_foot.png')), (80,72))
kirby_left_left_foot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/left', 'left_foot.png')), (80,72))
kirby_left_all_foots = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/walking/left', 'all_foots.png')), (80,72))

# Flying Right
kirby_flying_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '1.png')), (80, 72))
kirby_flying_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '2.png')), (80, 72))
kirby_flying_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '3.png')), (80, 72))
kirby_flying_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '4.png')), (80, 72))
kirby_flying_5 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '5.png')), (80, 72))
kirby_flying_6 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '6.png')), (80, 72))
kirby_flying_7 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '7.png')), (80, 72))
kirby_flying_8 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '8.png')), (80, 72))
kirby_flying_9 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '9.png')), (80, 72))
kirby_flying_10 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/kirby/flying/right', '10.png')), (80, 72))
