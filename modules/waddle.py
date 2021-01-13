from modules.vector2D import Vector2
from .mobile import Mobile
from .FSM import MobileState 
from modules.kirby import Kirby
import random

import pygame

class WaddleDee(Mobile):
   def __init__(self, position,health):
      super().__init__("waddleDee.png", position)

      self.initialPosition=position
      self._nFrames = 1
      self._vSpeed = 100
      self._aSpeed = 70
      self._framesPerSecond = 2
      self.maxHealth=health
      self.health=self.maxHealth
      self.hitbox=(self._position[0]+2,self._position[1]+2,31,18)
      self._state = MobileState()
      self._shootTimer= random.randrange(2,15,1)/10
      self.shoot=False
      
      self._nFramesList = {
         "moving" : 2,
         "standing" : 1
      }
      
      self._rowList = {
         "moving" : 1,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "standing" : 1
      }
      
      self._state = MobileState()
      
      self._sight = 50
      self._forget = 100
      
   
   def think(self, kirby):
      difference=kirby.getPosition()-self.getPosition()
      if kirby.getPosition()[1]>50 and  kirby.getPosition()[1]<200 :
            self._vSpeed=abs(difference.y) * 1.2
            if difference[1]<0:
               self._state.movement["down"]=False
               self._state.manageState("up",self)
            if difference[1]>0:
               self._state.movement["up"]=False
               self._state.manageState("down",self)
            
            if self._shootTimer<=0:
               self.shoot=True
               self._shootTimer=1
            if difference.x<0:
               self._state._lastFacing="left"
            if difference.x>0:
               self._state._lastFacing="right"
      else:
         self._state.manageState("stopall",self)
   

            


   def hit(self):
      self.health-=1
   
   def getFacing(self):
      return self._state.getFacing()

   def update(self,ticks,boundaries):
      super().update(ticks,boundaries)
      self._shootTimer-=ticks

   



   