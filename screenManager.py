
from basicManager import BasicManager
from gameManager import GameManager
from screenFSM import ScreenState
from items import Text
from displays import *
from modules.vector2D import Vector2
from screenInfo import SCREEN_SIZE
import pygame
from worldInfo import WORLD_SIZE
from info import *


class ScreenManager(BasicManager):
      
   def __init__(self):
      super().__init__()
      self._game = GameManager(SCREEN_SIZE,"jsonLevel0.txt")
      self._game.load()
      self._state = ScreenState()
      self._pausedText = Text(Vector2(0,0),"Paused")
      
      size = self._pausedText.getSize()
      midPointX = SCREEN_SIZE.x // 2 - size[0] // 2
      midPointY = SCREEN_SIZE.y // 2 - size[1] // 2
      
      self._pausedText.setPosition(Vector2(midPointX, midPointY))

      
      self._mainMenu = CursorMenu("cave.png", fontName="default8")
      self._mainMenu.addOption("start", "Start Level 1",
                               SCREEN_SIZE // 2 - Vector2(0,20),
                               center="both")
      self._mainMenu.addOption("exit", "exit",
                               SCREEN_SIZE // 2 + Vector2(0,20),
                               center="both")
      self._mainMenu.setCursor("start")
      self.mainText= Text(SCREEN_SIZE//2-Vector2(110,80),"AL-KAHER",font="default30", color=(255,0,0))
      #self._mainMenu.addText("AL-KAHER",SCREEN_SIZE//2-Vector2(0,80),center="both")

      self._pauseMenu=AbstractMenu("sky.png",fontName="default8",color=(255,0,0))

      self._pauseMenu.addOption("Paused","Paused",SCREEN_SIZE // 2 - Vector2(0,30),center="both")
      self._pauseMenu.addOption("Press P to Continue", "Press P to Continue",
                               SCREEN_SIZE // 2 + Vector2(0,20),
                               center="both")
      
      self._gameOver= CursorMenu("code1.png",fontName="default8",color=(0,0,0))
      self._gameOver.addText("Game Over :(",
                               SCREEN_SIZE // 2 - Vector2(0,50),
                               center="both")
      self._gameOver.addOption("restart", "Restart Level",
                               SCREEN_SIZE // 2,
                               center="both")
      self._gameOver.addOption("exit", "Exit Game",
                               SCREEN_SIZE // 2 + Vector2(0,50),
                               center="both")
      
      self._nextLevel=CursorMenu("skyy.png",fontName="default8",color=(0,0,0))
      self._nextLevel.addText("YOU WIN! " +"Ready for more?",SCREEN_SIZE //2 -Vector2(0,50), center="both")
      self._nextLevel.addOption("nextLevel", "Next Level", SCREEN_SIZE //2 - Vector2(0,20),center="both")
      self._nextLevel.addOption("restart", "Restart Level", SCREEN_SIZE //2 - Vector2(0,0),center="both")
      self._nextLevel.addOption("exit", "Exit", SCREEN_SIZE //2 + Vector2(0,20),center="both")

      self.currentLevel=0
      self.maxLevel=3
      self._games=[GameManager(SCREEN_SIZE,"jsonLevel0.txt"),GameManager(SCREEN_SIZE,"jsonLevel1.txt"),GameManager(SCREEN_SIZE,"jsonLevel2.txt"),GameManager(SCREEN_SIZE,"jsonLevel3.txt")]
      for game in self._games:
         game.load()
      
      self._endGame=CursorMenu("background.png",fontName="default8")

      self._endGame.addOption("exit", "Exit", SCREEN_SIZE //2 +Vector2(0,20) ,center="both")
      self._endGame.addText ("You WIN!",SCREEN_SIZE//2-Vector2(0,50),center="both")
      self._endGame.addOption("restart","Restart Level",SCREEN_SIZE//2-Vector2(0,20),center="both")
      self._endGame.addText("Best BackGround ", SCREEN_SIZE//2+Vector2(0,50),center="both")


 

   
   
   def draw(self, drawSurf):
      if self._state == "game":
         self._games[self.currentLevel].draw(drawSurf)
      
         if self._state.isPaused():
            self._pauseMenu.draw(drawSurf)
      if self._state=="advanceScreen":
         self._nextLevel.draw(drawSurf)
      
      elif self._state == "mainMenu":

         self._mainMenu.draw(drawSurf)
         self.mainText.draw(drawSurf)

      elif self._state == "gameOver":
         self._gameOver.draw(drawSurf)
      elif self._state=="gameWon":
         self._endGame.draw(drawSurf)
      
   
   def handleEvent(self, event):
      # Handle screen-changing events first
      if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
         self._state.manageState("pause", self)
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
         self._state.manageState("mainMenu", self)
      else:
         if self._state == "game" and not self._state.isPaused():
            self._games[self.currentLevel].handleEvent(event,BULLET_LIMIT,SHOT_LIMIT)
         elif self._state == "mainMenu":
            choice = self._mainMenu.handleEvent(event)
            
            if choice == "start":
               self._state.manageState("startGame", self)
            elif choice == "exit":
               return "exit"
         

         elif self._state =="gameWon":
            choice= self._endGame.handleEvent(event)
            if choice=="exit":
               return "exit"
            elif choice=="restart":
               self._state.manageState("restart",self)
            
         
         elif self._state == "gameOver":
            choice = self._gameOver.handleEvent(event)
            
            if choice == "exit":
               return "exit"
            elif choice == "restart":
               self._state.manageState("restart", self)
         
         elif self._state=="advanceScreen":
            choice=self._nextLevel.handleEvent(event)
            if choice=="exit":
               return "exit"
            elif choice=="restart":
               self._state.manageState("restart",self)
            elif choice=="nextLevel":
               self._state.manageState("nextLevel",self)

   
   
   def update(self, ticks):      
      if self._state == "game" and not self._state.isPaused():
         status=self._games[self.currentLevel].update(ticks, SCREEN_SIZE,WORLD_SIZE,BULLET_LIMIT)
         if status=="dead":
            self._state.manageState("gameOver",self)
         if self._games[self.currentLevel].levelWin==True and self.currentLevel!=self.maxLevel:
            self._state.manageState("levelWin",self)
         if self._games[self.currentLevel].levelWin==True and self.currentLevel==self.maxLevel:
            self._state.manageState("endGame",self)


      elif self._state == "mainMenu":
         self._mainMenu.update(ticks)
      elif self._state=="advanceScreen":
         self._nextLevel.update(ticks)
   
   
   # Prevents kirby from constantly walking if the direction arrow
   #  is released when the game isn't playing
   def transitionState(self, state):

      if state == "game":
         self._game.updateMovement()
   

   def restartLevel(self):
      self._games[self.currentLevel]=GameManager(SCREEN_SIZE,'jsonLevel'+str(self.currentLevel)+ '.txt')
      self._games[self.currentLevel].load()