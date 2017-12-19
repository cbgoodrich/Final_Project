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
    for row in range(0,5):
        for column in range(0,5):
            if data["playerBoard"][row][column] == EMPTY:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == MISS:
                Sprite(circle_miss, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == HIT:
                Sprite(circle_hit, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == SHIP:
                Sprite(circle_ship, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
    for row in range(0,5):
        for column in range(0,5):
            if data["computerBoard"][row][column] == MISS:
                Sprite(circle_miss, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == HIT:
                Sprite(circle_hit, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == SHIP:
                Sprite(circle_ship, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == EMPTY:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
    

def mouseClick(event):
    while data["shipCount"] < 3:
        col_click = event.x//80
        row_click = event.y//80
        data["playerBoard"][row_click][col_click] = SHIP
        Sprite(circle_ship, (RADIUS+2*col_click*RADIUS, RADIUS+2*row_click*RADIUS))
        data["shipCount"] += 1
        

def pickComputerShips():
    choose = False
    i = 0
    if choose == False:
        while i < 3:
            row = randint(0,4)
            column = randint(0,4)
            if data["computerBoard"][row][column] != SHIP:
                data["computerBoard"][row][column] = SHIP
                i += 1
        choose = True
        print(data["computerBoard"])
        
    
if __name__ == "__main__":
    
    data = {}
    data["shipCount"] = 0
    
    
    gray = Color(0xD3D3D3, 1)
    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    
    circle_empty = CircleAsset(RADIUS, LineStyle(1,black), white)
    circle_miss = CircleAsset(RADIUS, LineStyle(1,black), blue)
    circle_hit = CircleAsset(RADIUS, LineStyle(1,black), red)
    circle_ship = CircleAsset(RADIUS, LineStyle(1,black), gray)
    
    data["playerBoard"] = buildBoard()
    data["computerBoard"] = buildBoard()
    
    pickComputerShips()
    reDrawAll()
    
    Sprite(TextAsset("USER", fill = black, style = "Bold 24pt Times"),(160,RADIUS*10))
    Sprite(TextAsset("COMPUTER", fill = black, style = "Bold 24pt Times"),(600,RADIUS*10))

    App().listenMouseEvent("click", mouseClick)
    App().run()
    
    
    
    
    
    
