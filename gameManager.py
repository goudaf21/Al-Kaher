
from basicManager import BasicManager
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.kirby import Kirby
from modules.waddle import WaddleDee
from modules.drawable import Drawable
from modules.bullet import Bullet
from modules.waddle2 import Waddle2
import json

class GameManager(BasicManager):
    def __init__(self, screenSize, loadFile):
      
      self._loadFile = loadFile
      self._screenSize = screenSize
      self.waddleNumber=0
      self.bullets=[]
      self.enemyBullets=[]
      self.waddles=[]



      self.bulletSound= pygame.mixer.Sound('bullet.wav')
        
      self.shotSound= pygame.mixer.Sound('shotgun.wav')
      self.shotgunDelay=0
      self.levelWin=False

    def load(self):
        filePtr=open(os.path.join("resources","levels",self._loadFile))
        info=json.load(filePtr)
        filePtr.close()
        self.worldSize=Vector2(*info["worldSize"])

        
   
        self.backgroundName=info["background"]
        self.background = Drawable(self.backgroundName, Vector2(0,0))
        self.kirby = Kirby(Vector2(*info["startkirby"]))

        positions= info["waddle"]
        if len(positions)!=0:
            self.waddleNumber=len(positions)//2

            for i in range (self.waddleNumber):
                self.waddles.append(WaddleDee(Vector2(positions[i*2],positions[i*2+1]),health=10))
        positions2=info["waddle2"]
        if len(positions2)!=0:
            self.waddle2Number= len(positions2)//2
            for i in range(self.waddle2Number):
              self.waddles.append(Waddle2(Vector2(positions2[i*2],positions2[i*2+1]),health=6))
   
   


    def draw(self,drawSurface):
        self.background.draw(drawSurface)
        self.kirby.draw(drawSurface)
        pygame.draw.rect(drawSurface,(255,0,0),(10,220,100,10))
        pygame.draw.rect(drawSurface,(0,255,0),(10,220,100-(self.kirby.maxHealth-self.kirby.health)*(100/self.kirby.maxHealth),10))

        for bullet in self.enemyBullets:
            bullet.draw(drawSurface)
        
        for bullet in self.bullets:
            bullet.draw(drawSurface)
        
        for wad in self.waddles:
            wad.draw(drawSurface)

        

    def update(self,ticks,screenSize,worldSize,bulletLimit):



        for wad in self.waddles:
            if wad.health==0:
                  self.waddles.pop(self.waddles.index(wad))
                  if self.kirby.health==10:
                    self.kirby.health+=1
                  elif self.kirby.health==9:
                      self.kirby.health+=1
                  else:
                      self.kirby.health+=2

        for bullet in self.bullets:
            if bullet.position[1]-bullet.radius < self.kirby.getCollisionRect()[1] + self.kirby.hitbox[3] and bullet.position[1]+bullet.radius > self.kirby.getCollisionRect()[1]:
                  if bullet.position[0]+bullet.radius > self.kirby.getCollisionRect()[0] and bullet.position[0]-bullet.radius < self.kirby.getCollisionRect()[0] + self.kirby.hitbox[2]:
                        self.kirby.hit(2)
                        self.bullets.pop(self.bullets.index(bullet))
            for waddle in self.waddles:
                  if bullet.position[1]-bullet.radius < waddle.getCollisionRect()[1] + waddle.hitbox[3] and bullet.position[1]+bullet.radius > waddle.getCollisionRect()[1]:
                        if bullet.position[0]+bullet.radius > waddle.getCollisionRect()[0] and bullet.position[0]-bullet.radius < waddle.getCollisionRect()[0] + waddle.hitbox[2]:

                              waddle.hit()
                              self.bullets.pop(self.bullets.index(bullet))
                              break

        for bullet in self.enemyBullets:
            if bullet.position[1]-bullet.radius < self.kirby.getCollisionRect()[1] + self.kirby.hitbox[3]  and bullet.position[1]+bullet.radius > self.kirby.getCollisionRect()[1]:
                  if bullet.position[0]+bullet.radius > self.kirby.getCollisionRect()[0] and bullet.position[0]-bullet.radius < self.kirby.getCollisionRect()[0] + self.kirby.hitbox[2]:
                        self.kirby.hit(1)
                        self.enemyBullets.pop(self.enemyBullets.index(bullet))
      

        for wad in self.waddles:
            if wad.getCollisionRect()[1]<self.kirby.getCollisionRect()[1]+self.kirby.hitbox[3] and wad.getCollisionRect()[1]+wad.hitbox[3]>self.kirby.getCollisionRect()[1]:
                  if wad.getCollisionRect()[0]+wad.hitbox[2]>self.kirby.getCollisionRect()[0] and wad.getCollisionRect()[0]<self.kirby.getCollisionRect()[0]+self.kirby.hitbox[2]:
                        self.kirby.hit(10) 

        for bullet in self.enemyBullets:
            if bullet.position[0]<=Drawable.WINDOW_OFFSET[0]:
                self.enemyBullets.pop(self.enemyBullets.index(bullet))           
            bullet.update(ticks)
            
        for bullet in self.bullets:
            if bullet.position[0]<=Drawable.WINDOW_OFFSET[0]:
                  self.bullets.pop(self.bullets.index(bullet))           
            bullet.update(ticks)
            if bullet.timeLimit:
                  if bullet.timeLimit <=0:
                        self.bullets.pop(self.bullets.index(bullet))
      

      
        self.kirby.update(ticks, worldSize)
        for wad in self.waddles:
            wad.update(ticks,worldSize)
            if wad.shoot==True:
                Bullet.makebullet(wad,self.enemyBullets,vel=Vector2(300,0),color= (255,0,0))
                wad.shoot=False
        
        for wad in self.waddles:
            wad.think(self.kirby)

        self.shotgunDelay-=ticks

        if self.kirby.health<=0:
            return "dead"
        
        if len(self.waddles)==0:
            self.levelWin=True



        pygame.display.flip() 
        Drawable.updateWindowOffset(self.kirby,screenSize,worldSize)



    def handleEvent(self,event,BULLET_LIMIT,SHOT_LIMIT):
        if event.type == pygame.KEYDOWN:
               
            if event.key==pygame.K_SPACE:
                if self.kirby.level==0:
                    if len(self.bullets)<BULLET_LIMIT:
                              Bullet.makebullet(self.kirby,self.bullets,Vector2(200,0),bulletLimit=BULLET_LIMIT,color=(0,255,0))
                              self.bulletSound.play()
                        
                  
                elif self.kirby.level==1:
                        if len(self.bullets)<SHOT_LIMIT and self.shotgunDelay<=0:
                              Bullet.makebullet(self.kirby,self.bullets,Vector2(200,0),bulletLimit=SHOT_LIMIT,color=(0,255,0),timeLimit=0.1)
                              Bullet.makebullet(self.kirby,self.bullets,Vector2(100,23),bulletLimit=SHOT_LIMIT,color=(0,255,0),timeLimit=0.1)
                              Bullet.makebullet(self.kirby,self.bullets,Vector2(150,-23),bulletLimit=SHOT_LIMIT,color=(0,255,0),timeLimit=0.1)
                              self.shotgunDelay=1

       
                              self.shotSound.play()
        self.kirby.handleEvent(event)

    def updateMovement(self):
        self.kirby.updateMovement()


        
