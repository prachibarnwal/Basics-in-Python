import pygame
import random as rd
import time
from pygame import mixer

#SCREEN SET-UP
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("HAPPIEST BDAY VAIBHAVI DIDDI..🥳🎂🥳🎂🥳")


#SONG PLAYING
mixer.init()
mixer.music.load("ilahi.mp3")
mixer.music.set_volume(100.5) 
mixer.music.play()

#CAKE1
y = 800
p = pygame.image.load("blue.png")
for i in range(112):
    clr = (0, 0, 0)
    win.fill(clr)
    win.blit(p, (10,y))
    time.sleep(0.1)
    y -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    
#CAKE2
y = 300
p = pygame.image.load("blast.png")
for i in range(80):
    clr = (0, 0, 0)
    win.fill(clr)
    win.blit(p, (10,y))
    time.sleep(0.1)
    y -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

#PIC
y = 300
p = pygame.image.load("vabhavi.png")
for i in range(80):
    clr = (0, 0, 0)
    win.fill(clr)
    win.blit(p, (10,y))
    time.sleep(0.1)
    y -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

#CAKE3
y = 300
p = pygame.image.load("flower.png")
for i in range(80):
    clr = (0, 0, 0)
    win.fill(clr)
    win.blit(p, (10,y))
    time.sleep(0.1)
    y -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

#CAKE4
y = 300
p = pygame.image.load("hbd.png")
for i in range(80):
    clr = (0, 0, 0)
    win.fill(clr)
    win.blit(p, (10,y))
    time.sleep(0.1)
    y -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    
#song stop
mixer.music.stop()
