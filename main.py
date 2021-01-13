
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.kirby import Kirby
from modules.waddle import WaddleDee
from modules.drawable import Drawable
from modules.bullet import Bullet
from modules.waddle2 import Waddle2
from screenManager import *

WORLD_SIZE=Vector2(1000,240)
SCREEN_SIZE = Vector2(320, 240)
SCALE = 2
UPSCALED_SCREEN_SIZE = SCREEN_SIZE * SCALE
offset=Vector2(0,0)

BULLET_LIMIT=1  
SHOT_LIMIT=5



def main():
   
   # initialize the pygame module
   pygame.init()
   music = pygame.mixer.music.load("heatwaves.mp3")
   MUSIC=True
   
   
   pygame.mixer.music.play(-1)
   
   
   pygame.display.set_caption("AL KAHER")
   
   screen = pygame.display.set_mode(list(UPSCALED_SCREEN_SIZE))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
#    bullets=[]
#    enemyBullets=[]
   
   
#    kirby = Kirby(Vector2(0,0))
#    waddles=[]
#    waddle = WaddleDee(Vector2(250,50),10)
#    waddles.append(waddle)

#    waddle2=Waddle2(Vector2(300,100),10)
#    waddles.append(waddle2)
   
   
#    background = Drawable("background.png", Vector2(0,0))
   
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   manager=ScreenManager()
   
   
   # define a variable to control the main loop
   running = True
   
   # main loop
   while running:
      pygame.transform.scale(drawSurface, list(UPSCALED_SCREEN_SIZE), screen)

      manager.draw(drawSurface)
      pygame.display.flip()
      
      # Draw everything

      # background.draw(drawSurface)
      # kirby.draw(drawSurface)
      
      # if kirby.health<=0:
      #       kirby.die()
      # pygame.draw.rect(drawSurface,(255,0,0),(10,220,100,10))
      # pygame.draw.rect(drawSurface,(0,255,0),(10,220,100-(kirby.maxHealth-kirby.health)*(100/kirby.maxHealth),10))
      
      # for bullet in enemyBullets:
      #       bullet.draw(drawSurface)
            
      # for bullet in bullets:

      #       bullet.draw(drawSurface)



      # for wad in waddles:
      #       wad.draw(drawSurface)
            
      # for wad in waddles:
      #       if wad.health==0:
      #             waddles.pop(waddles.index(wad))
            

      
      # # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
                    
         # only do something if the event is of type QUIT or ESCAPE is pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
                  running = False
                  break
            if event.type==pygame.KEYDOWN and event.key==pygame.K_n:
               if MUSIC==True:
                  pygame.mixer.music.pause()
                  MUSIC=False
               else:
                  pygame.mixer.music.unpause()
                  MUSIC=True
               

            result=manager.handleEvent(event)
            if result=='exit':
               running=False
               break
         

      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      ticks = gameClock.get_time() / 1000

      manager.update(ticks)


      


      

if __name__ == "__main__":
   main()