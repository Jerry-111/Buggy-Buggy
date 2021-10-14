import include.Character
import include.rooms
import numpy as np
import math

Gravity = 0.981
MovementAcceleration = 0.25

TerminalVelocityX = 2.5
TerminalVelocityY = 1

Drag = 0.035

class physics:

    def __init__(self, c):
        self.c = c

    def recalculateVelocity(self, latestVelocityX, latestVelocityY, inputX, inputY): 
        #Requires the velocity of the last frame and the desired input

        calculatedVelocityX = latestVelocityX + (inputX * MovementAcceleration)         #Calculates the desired velocity
        
        if(calculatedVelocityX > TerminalVelocityX):                                    #Clamps the velocity to the terminal velocity
            calculatedVelocityX = TerminalVelocityX                                     #
        if(calculatedVelocityX < -TerminalVelocityX):                                   #
            calculatedVelocityX = -TerminalVelocityX                                    #

        calculatedVelocityX = calculatedVelocityX + Drag * (0 - calculatedVelocityX)    #Interpolates the drag to zero
        

        calculatedVelocityY = latestVelocityY + Gravity
        if(calculatedVelocityY > TerminalVelocityY):
            calculatedVelocityY = TerminalVelocityY
        if(calculatedVelocityY < -TerminalVelocityY):
            calculatedVelocityY = -TerminalVelocityY
        
        return calculatedVelocityX, calculatedVelocityY


def collideDetect(a, b):
    if math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2) <= 10:
        return True
    return False

