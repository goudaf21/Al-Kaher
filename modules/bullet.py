from modules.drawable import Drawable
import pygame
from modules.vector2D import Vector2

SCREEN_SIZE = Vector2(320, 240)
SCALE = 2
UPSCALED_SCREEN_SIZE = SCREEN_SIZE * SCALE

class Bullet(object):
    def __init__(self,position,color,radius=2,velocity=Vector2(-100,0),timeLimit=None):
        self.position=position
        self.color=color
        self.radius=radius
        self.velocity=velocity*SCALE
        self.timeLimit=timeLimit
 

        # if facing=="left":
        #     self.velocity=Vector2(-4,0)*SCALE
        # if facing=="right":
        #     self.velocity=Vector2(4,0)*SCALE

    def draw(self,surface):
        pos=[]
        for i in self.position:
            pos.append(int(i))
        pygame.draw.circle(surface,self.color,list(map(int,self.position-Drawable.WINDOW_OFFSET)),self.radius)
    
    def update(self,ticks):
        self.position+=self.velocity*ticks

        if self.position[0]+self.velocity[0]*ticks >= SCREEN_SIZE[0]+Drawable.WINDOW_OFFSET[0]:
            self.velocity[0]=-self.velocity[0]
        
        if self.timeLimit != None:
            self.timeLimit-=ticks
    
    @classmethod
    def makebullet(cls,object,list,vel,bulletLimit=None, timeLimit=None, color=(255,0,0)):
        if bulletLimit==None or len(list)< bulletLimit:
            bullPos=Vector2(*object.getPosition())
            if object.getFacing() == "right":
                list.append(Bullet(bullPos+[object.getSize()[0]+10,0],color,velocity=vel,timeLimit=timeLimit))

            else:
                vel.x=-vel.x
                list.append(Bullet(bullPos+[-5,0],color,velocity=vel,timeLimit=timeLimit))


                


            
            
        

        
