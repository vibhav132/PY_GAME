import pygame,sys
from pygame.locals import *
import time
pygame.init()
FPS = 30
fpsclock = pygame.time.Clock()
soundobj = pygame.mixer.Sound('cat.mp3')

Display = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Animation")
WHITE = (255,255,255)
catimg = pygame.image.load('cat.png')
catx=10
caty=10
direction='right'
while True:
    Display.fill(WHITE)
    if direction=='right':
        catx+=5
        if catx == 280:
            direction="down"
    elif direction=='down':
        caty+=5
        if caty == 220:
            direction='left'
    elif direction=='left':
        catx-=5
        if catx == 10:
            direction='up'
    elif direction=='up':
        caty-=5
        if caty == 10:
            direction='right'
    Display.blit(catimg,(catx,caty))
    soundobj.set_volume(1.0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    soundobj.play()
    fpsclock.tick(FPS)