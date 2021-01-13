from modules.waddle import WaddleDee




class Waddle2(WaddleDee):
    def __init__(self,position,health):
        super().__init__( position,health)
        self.triggered=False
        
        

    
    def think(self,kirby):
        difference=kirby.getPosition()-self.getPosition()
        if kirby.getPosition()[1]>50 and  kirby.getPosition()[1]<200 :
            self.triggered=True

        if self.triggered==True:
            #self._vSpeed=abs(difference.y) * 1.2
            
            if difference[1]<0:
               self._state.movement["down"]=False
               self._state.manageState("up",self)
            if difference[1]>0:
               self._state.movement["up"]=False
               self._state.manageState("down",self)
            if difference.x >0 :
                self._state._lastFacing="right"
                self._state.movement["left"]=False
                self._state.manageState("right",self)
            if difference.x < 0:
                self._state._lastFacing="left"
                self._state.movement["right"]=False
                self._state.manageState("left",self)

                
            


