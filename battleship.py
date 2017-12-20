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
                Sprite(circle_empty, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == EMPTY:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS+500, RADIUS+2*row*RADIUS))
    Sprite(TextAsset("USER", fill = black, style = "Bold 24pt Times"),(160,RADIUS*10))
    Sprite(TextAsset("COMPUTER", fill = black, style = "Bold 24pt Times"),(600,RADIUS*10))
    if data["playerHits"] == 3 or data["computerHits"] == 3:
        data["continue"] = False
        Sprite(TextAsset("GAME OVER", fill = black, style = "Bold 60pt Times"),(325,150))

def mouseClick(event):
    if data["continue"] == True:
        if data["shipCount"] < 3:
            col_click = event.x//80
            row_click = event.y//80
            data["playerBoard"][row_click][col_click] = SHIP
            Sprite(circle_ship, (RADIUS+2*col_click*RADIUS, RADIUS+2*row_click*RADIUS))
            data["shipCount"] += 1
        else:
            col_choose = (event.x-500)//80
            row_choose = event.y//80
            if data["computerBoard"][row_choose][col_choose] == EMPTY:
                data["computerBoard"][row_choose][col_choose] = MISS
                computer = True
            elif data["computerBoard"][row_choose][col_choose] == SHIP:
                data["computerBoard"][row_choose][col_choose] = HIT
                data["playerHits"] += 1
                computer = True
            elif data["computerBoard"][row_choose][col_choose] == MISS:
                computer = False
            elif data["computerBoard"][row_choose][col_choose] == HIT:
                computer = False
            reDrawAll()
            if computer == True:
                computerTurn()
    

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
        
def computerTurn():
    pick = False
    if pick == False:
        i = 0
        while i == 0:
            row_guess = randint(0,4)
            col_guess = randint(0,4)
            if data["playerBoard"][row_guess][col_guess] == SHIP:
                data["playerBoard"][row_guess][col_guess] = HIT
                i = 1
                data["computerHits"] += 1
            elif data["playerBoard"][row_guess][col_guess] == EMPTY:
                data["playerBoard"][row_guess][col_guess] = MISS
                i = 1
        pick = True
    reDrawAll()
    playerTurn = True
    
if __name__ == "__main__":
    
    data = {}
    data["continue"] = True
    data["shipCount"] = 0
    data["computerHits"] = 0
    data["playerHits"] = 0
    
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

    App().listenMouseEvent("click", mouseClick)
    App().run()
    
    
    
    
    
    
