import pygame
import sys
import time

class Pipe:
    def __init__(self,flip):                                                                      #Konstruktor (Aufruf bei Röhrenerstellung) (self = this in java)
        self.img = pygame.image.load("pipe.png")
        if flip: 
            self.img = pygame.transform.flip(self.img, flip_x = False, flip_y = True)             #Obere Röhre wird an y-Achse gespiegelt
            self.imgrect = pygame.Rect(600,-400,50,200)                                           #Array            
        else:
            self.imgrect = pygame.Rect(600,320,50,200)
        self.x = self.imgrect[0]                                                                  #Erste Array Position = 0
    
    def frame(self):
        self.x -= 3
        self.imgrect[0] = self.x
    
    def draw(self, screen):
        screen.blit(self.img, self.imgrect)
    
    #def randomize()
        



pygame.init()
screen = pygame.display.set_mode([640,480])
running = True
pipeunten = Pipe(False)
pipeoben = Pipe(True)
#obere Röhre wird geflippt, untere nicht

clock = pygame.time.Clock()
while running:
    clock.tick(60)
    #time.sleep(2)
    #pygame.draw.rect(screen, (0,255,0), pygame.Rect(320,280,50,200) )
    #while True:
    pipeunten.frame()
    pipeoben.frame()
    pipeunten.draw(screen)
    pipeoben.draw(screen)
        
    # screen ist Argument, deshalb nötig, self wird nicht benötigt
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
