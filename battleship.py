#Charlie Goodrich
#12/14/17
#battleship.py - creates the game of battleship (please don't fail me)

from ggame import *
from random import randint

#CONSTANTS
EMPTY = 0
MISS = 1
HIT = 2
SHIP = 3
RADIUS = 40

def buildBoard():
    return [[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5]
    
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    i = 0
    while i <= 1:
        for row in range(0,5):
            for column in range(0,5):
                Sprite(circle_empty, (RADIUS+2*row*RADIUS+500*i, RADIUS+2*column*RADIUS))
        i += 1


def mouseClick(event):
    print(event.x, event.y)
    
def computerTurn():
    choose = False
    i = 0
    if choose == False:
        while i <= 2:
            row = randint(0,4)
            column = randint(0,4)
            if data["computerBoard"][row][column] != SHIP:
                data["computerBoard"][row][column] = SHIP
            i += 1
        choose = True
        print(data["computerBoard"])

if __name__ == "__main__":
    
    data = {}

    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    
    circle_empty = CircleAsset(RADIUS, LineStyle(1,black), white)
    circle_miss = CircleAsset(RADIUS, LineStyle(1,blue), blue)
    circle_hit = CircleAsset(RADIUS, LineStyle(1, red), red)
    
    data["playerBoard"] = buildBoard()
    data["computerBoard"] = buildBoard()
    reDrawAll()
    computerTurn()
    Sprite(TextAsset("USER", fill = black, style = "Bold 24pt Times"),(160,RADIUS*10))
    Sprite(TextAsset("COMPUTER", fill = black, style = "Bold 24pt Times"),(600,RADIUS*10))

    
    App().run(event)
    
    
    
    
    
    
