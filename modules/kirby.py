from .mobile import Mobile
from .FSM import MobileState
from modules.vector2D import Vector2

import pygame

class Kirby(Mobile):
   def __init__(self, position):
      super().__init__("Old hero.png", position)

      self.maxHealth=10
      self.health=self.maxHealth
      self._nFrames = 2
      self._vSpeed = 50
      self._aSpeed = 100
      self._framesPerSecond = 2
      self.level=1
      
      self._nFramesList = {
         "moving" : 4,
         "swimming" : 4,
         "standing" : 4
      }
      
      self._rowList = {
         "moving" : 1,
         "swimming" : 3,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "swimming" : 8,
         "standing" : 2
      }
      
      self._state = MobileState()
      self.hitbox=(self._position[0]+2,self._position[1]+2,18,18)
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._state.manageState("down", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("up", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("left", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("right", self)
         
         if event.key== pygame.K_z:
            if self.level==1:
               self.level= 0
            elif self.level == 0:
               self.level=1
               
      
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            self._state.manageState("stopdown", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("stopup", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("stopleft", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("stopright", self)
   
      
   def getFacing(self):
         return self._state.getFacing()

   def hit(self,power):
         self.health-= power

   
   def die(self):
      self.health=self.maxHealth
      self._position=Vector2(0,0)

   def updateMovement(self):
      pressed=pygame.key.get_pressed()
      if not pressed[pygame.K_LEFT]:
         self._state.manageState("stopleft",self)
      elif not pressed[pygame.K_DOWN]:
         self._state.manageState("stopdown",self)
      elif not pressed[pygame.K_RIGHT]:
         self._state.manageState("stopright",self)
      elif not pressed[pygame.K_UP]:
         self._state.manageState("stopup",self)