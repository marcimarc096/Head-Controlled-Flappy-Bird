import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode([640,480])
running = True
imgoben = pygame.image.load("pipe.png")
imgoben = pygame.transform.flip(imgoben,flip_x = False, flip_y = True)              #Obere Röhre wird an y-Achse gespiegelt
imgunten = pygame.image.load("pipe.png")
imgrectoben = pygame.Rect(600,-400,50,200)
imgrectunten = pygame.Rect(600,320,50,200)                                          #Array
xunten = imgrectunten[0]                                                            #Array Position --> erste Stelle
xoben = imgrectoben[0]
while running:
    #pygame.draw.rect(screen, (0,255,0), pygame.Rect(320,280,50,200) )
    xunten -= 0.25                                                                  #Röhrengeschwindigkeit
    xoben -= 0.25
    imgrectunten[0] = xunten
    imgrectoben[0] = xoben
    screen.blit(imgunten, imgrectunten)
    screen.blit(imgoben, imgrectoben)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
