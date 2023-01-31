import pygame,sys
from pygame.locals import *
pygame.init()
Display = pygame.display.set_mode((800,800),0,32)
pygame.display.set_caption("Hello world")
Display.fill((255,255,255))
x=0
list = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
while True:
    x=x+1
    for event in pygame.event.get():
        pygame.draw.line(Display,list[(x+2)%4],(100,100),(500,100),2)
        pygame.draw.line(Display,list[(x)%4],(500,100),(500,300),2)
        pygame.draw.line(Display,list[(x+3)%4],(500,300),(100,300),2)
        pygame.draw.line(Display,list[(x+1)%4],(100,100),(100,300),2)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()