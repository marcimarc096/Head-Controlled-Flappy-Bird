import pygame
import sys
import time

class Pipe:
    def __init__(self,flip):                                                                      #Konstruktor (Aufruf bei Röhrenerstellung) (self = this in java)
        self.img = pygame.image.load("pipe.png")
        if flip: 
            self.img = pygame.transform.flip(self.img, flip_x = False, flip_y = True)             #Obere Röhre wird an y-Achse gespiegelt           
            self.x = 600
            self.y = -400
            self.width = 50
            self.height = 200
        else:
            self.x = 600
            self.y = 320
            self.width = 50
            self.height = 200                                                                  
    
    def frame(self):
        pass

    def blit(self,x,y,width,height):
        imgrect = pygame.Rect(x,y,width,height)
        screen.blit(self.img, imgrect)
        
    
    #def randomize()
        
pygame.init()
screen = pygame.display.set_mode([640,480])
running = True
pipeunten = Pipe(False)
pipeoben = Pipe(True)
#obere Röhre wird geflippt, untere nicht

#append hängt Einträge im Array hintendran
objects=[]
objects.append(pipeunten)
objects.append(pipeoben)
cameraPosX = 0
cameraMovementSpeed = 3

clock = pygame.time.Clock()
while running:
    
    cameraPosX += cameraMovementSpeed
    clock.tick(60)
    #time.sleep(2)
    #pygame.draw.rect(screen, (0,255,0), pygame.Rect(320,280,50,200) )
    #while True:
    for object in objects:
        object.frame()
        object.blit(object.x - cameraPosX, object.y, object.width, object.height)
        
    # screen ist Argument, deshalb nötig, self wird nicht benötigt
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
