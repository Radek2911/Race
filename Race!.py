import pygame
pygame.init()
from pygame.locals import*
screen=pygame.display.set_mode()
pygame.display.set_caption(('Race'))
back=pygame.image.load('Circuit.png')
back=pygame.transform.scale(back,(1680,1050))
print(screen.get_size)
class Car:
    def __init__(self,carname):
        self.image=pygame.image.load(carname)
        self.angle=270
        self.image=pygame.transform.rotozoom(self.image,0, 0.05)

        self.x=840
        self.y=100
        self.w=0
    def draw(self):
        rimage=pygame.transform.rotate(self.image, self.angle)
        screen.blit(rimage,(self.x,self.y))
        if self.w==1:

            self.y=self.y-10
        
        if self.w==-1:
        
            self.y=self.y+10
        if self.w==2:
            self.x=self.x+10
        if self.w==-2:
            self.x=self.x-10
    
        

car=Car('mycar.png')
car2=Car('othercar.png')
while True:
    screen.blit(back,(0,0))
    car.draw()
    car2.draw()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==K_w:
                car.angle=0

                car.w=1

            if event.key==K_s:
                car.angle=180
                car.w=-1
            if event.key==K_d:
                car.angle=270
                car.w=2

            if event.key==K_a:
                car.angle=90
                car.w=-2
            
        if event.type == KEYUP:
            if event.key==K_w:
                car.w=0
            if event.key==K_s:
                car.w=0
            if event.key==K_d:
                car.w=0
         
        if event.type == KEYDOWN:
            if event.key==K_UP:
                car2.angle=180

                car2.w=1

            if event.key==K_DOWN:
                car2.angle=0
                car2.w=-1
            if event.key==K_RIGHT:
                car2.angle=90
                car2.w=2

            if event.key==K_LEFT:
                car2.angle=270
                car2.w=-2
            
        if event.type == KEYUP:
            if event.key==K_UP:
                car2.w=0
            if event.key==K_DOWN:
                car2.w=0
            if event.key==K_RIGHT:
                car2.w=0
            if event.key==K_LEFT:
               
                car2.w=0

        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
        
