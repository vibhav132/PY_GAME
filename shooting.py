import pygame,sys
from pygame.locals import *
import random
pygame.init()
FPS=10
fpsclock = pygame.time.Clock()
Display=pygame.display.set_mode((1450,800),FULLSCREEN,32)
WHITE = (255,255,255)
shipimg = pygame.image.load('space_ship.png')
shipy = 728
shipx = 0
bulletimg = pygame.image.load('bullets1.png')
bullet_speed = 10
bulletx = [100000,100000,100000,10000,100000,100000,100000,100000]
bullety = [100000,100000,100000,10000,100000,100000,100000,100000]
x=0
enemyimg = pygame.image.load('enemy.png')
k = random.randint(0,7)
enemyx = 9+ 200*k
enemyy = 0

while True:
    Display.fill(WHITE)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_RIGHT] and shipx <= 1200:
            shipx += 200
        if keys[pygame.K_LEFT] and shipx >=200:
            shipx -= 200
        if keys[pygame.K_SPACE]:
            bulletx[int(shipx/200)] =shipx+25
            bullety[int(shipx/200)]=shipy
            x+=1
    Display.blit(shipimg,(shipx,shipy))
    Display.blit(enemyimg,(enemyx,enemyy))
    for i in range(0,8):
        if(bullety[i]>0):
         bullety[i] = bullety[i]- 100   
    enemyy = enemyy + 25
    if(enemyy>=shipy):
        pygame.quit()
        sys.exit()
    if(enemyy>=bullety[k] and x>0):
        k = random.randint(0,7)
        enemyx = 9+ 200*k
        enemyy = 0
    if(x>0):
      for i in range(0,8):                 
            Display.blit(bulletimg,(bulletx[i],bullety[i]))
    pygame.display.update()

    fpsclock.tick(FPS)

