#Charlie Goodrich
#12/14/17
#battleship.py - creates the game of battleship (please don't fail me)

from ggame import *
from random import randint

#CONSTANTS
EMPTY = 0
MISS = 1
HIT = 2

def buildBoard():
    data["board"] = [[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5]
    for row in range(0,5):
        for column in range(0,5):
            print(data["board"][row][column], end = " ")
        print()
    
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()

def mouseClick(event):
    var = 0

if __name__ == "__main__":
    
    data = {}

    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    
    circle_empty = CircleAsset(25, LineStyle(1,black), white)
    circle_miss = CircleAsset(25, LineStyle(1,blue), blue)
    circle_hit = CircleAsset(25, LineStyle(1, red), red)
    
    buildBoard()
    
    
    
    
