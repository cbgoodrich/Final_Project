#Charlie Goodrich
#12/14/17
#battleship.py - creates the game of battleship (please don't fail me)

from ggame import *
from random import randint

#CONSTANTS/HELPFUL VARIABLES
EMPTY = 0
MISS = 1
HIT = 2
SIZE = 5
SHIP = int(input("Enter the number of ships you want: "))
RADIUS = 40

#BUILDS THE DESIRED MATRIX BOARD AND RETURNS IT TO THE MAIN FUNCTION
def buildBoard():
    return [[EMPTY]*SIZE,[EMPTY]*SIZE,[EMPTY]*SIZE,[EMPTY]*SIZE,[EMPTY]*SIZE]

#AFTER EACH MOVE, THIS FUNCTION REDRAWS THE GAME BOARD    
def reDrawAll():
    for item in App().spritelist[:]: #loop going through all the sprites
        item.destroy() #destroys the sprites
    for row in range(0,SIZE): #the double for loop is to sprite the game board
        for column in range(0,SIZE):
            if data["playerBoard"][row][column] == EMPTY:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == MISS:
                Sprite(circle_miss, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == HIT:
                Sprite(circle_hit, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
            elif data["playerBoard"][row][column] == SHIP:
                Sprite(circle_ship, (RADIUS+2*column*RADIUS, RADIUS+2*row*RADIUS))
    for row in range(0,SIZE):
        for column in range(0,SIZE):
            if data["computerBoard"][row][column] == MISS:
                Sprite(circle_miss, (RADIUS+2*column*RADIUS+SIZE*100, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == HIT:
                Sprite(circle_hit, (RADIUS+2*column*RADIUS+SIZE*100, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == SHIP:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS+SIZE*100, RADIUS+2*row*RADIUS))
            elif data["computerBoard"][row][column] == EMPTY:
                Sprite(circle_empty, (RADIUS+2*column*RADIUS+SIZE*100, RADIUS+2*row*RADIUS))
    
    #sprites the text underneath each game board
    Sprite(TextAsset("USER", fill = black, style = "Bold 24pt Times"),(160,RADIUS*10))
    Sprite(TextAsset("COMPUTER", fill = black, style = "Bold 24pt Times"),(600,RADIUS*10))
    
    if data["playerHits"] == SHIP: #checking to see how many times the player has hit a ship
        data["continue"] = False #variable that makes the mouseClick function run
        Sprite(TextAsset("YOU WIN", fill = black, style = "Bold 60pt Times"),(325,150))
    elif data["computerHits"] == SHIP:
        data["continue"] = False
        Sprite(TextAsset("GAME OVER. YOU LOSE", fill = black, style = "Bold 60pt Times"),(325,150))

#RUNS THE PROGRAM BY SEEING WHERE CLICKS OCCUR, THEN CHANGING THE GAME MATRICES BASED ON CLICKS
def mouseClick(event):
    if data["continue"] == True: #seeing if it should run; if false it doesn't do anything
        if data["shipCount"] < SHIP: #seeing how many ships the user selected
            if event.x <= 2*RADIUS*SIZE: #only doing if user clicks in the game board
                col_click = event.x//80 #creating columns and rows based on a click
                row_click = event.y//80
                if data["playerBoard"][row_click][col_click] != SHIP:
                    data["playerBoard"][row_click][col_click] = SHIP #adding a ship to the player board
                    Sprite(circle_ship, (RADIUS+2*col_click*RADIUS, RADIUS+2*row_click*RADIUS))
                    data["shipCount"] += 1
        else: #only runs if the user has selected enough ships
            col_choose = (event.x-SIZE*100)//80 
            row_choose = event.y//80
            if col_choose >= 0: #making sure the user clicks in the game board
                if data["computerBoard"][row_choose][col_choose] == EMPTY:
                    data["computerBoard"][row_choose][col_choose] = MISS
                    computer = True #variable that tells the computer to guess where to shoot
                elif data["computerBoard"][row_choose][col_choose] == SHIP:
                    data["computerBoard"][row_choose][col_choose] = HIT
                    data["playerHits"] += 1
                    computer = True
                elif data["computerBoard"][row_choose][col_choose] == MISS:
                    computer = False #if computer = False then the computer doesn't shoot, it waits until True
                elif data["computerBoard"][row_choose][col_choose] == HIT:
                    computer = False
                if data["computerHits"] == SHIP: #de-bug where I would sink last ship, computer would guess, fixed
                    data["continue"] = False
                reDrawAll() #updates the board
                if computer == True and data["continue"] == True:
                    computerTurn() #tells the computer to guess

#HAS THE COMPUTER PICK THREE RANDOM SHIP LOCATIONS AND AMEND THE COMPUTER'S BOARD
def pickComputerShips():
    choose = False #variable to see if the computer has chosen all its ships
    if choose == False:
        i = 0
        while i < SHIP: #going through the process of the computer creating ships
            row = randint(0,4)
            column = randint(0,4)
            if data["computerBoard"][row][column] != SHIP:
                data["computerBoard"][row][column] = SHIP
                i += 1
        choose = True

#HAS THE COMPUTER RANDOMLY GUESS TO FIND THE USER'S SHIPS
def computerTurn():
    pick = False #variable that checks to see if the computer has picked
    if pick == False:
        while True: #loop that only breaks if guess is hit or miss
            row_guess = randint(0,4)
            col_guess = randint(0,4)
            if data["playerBoard"][row_guess][col_guess] == SHIP: #checking to see if player board is a ship
                data["playerBoard"][row_guess][col_guess] = HIT
                data["computerHits"] += 1
                break
            elif data["playerBoard"][row_guess][col_guess] == EMPTY:
                data["playerBoard"][row_guess][col_guess] = MISS
                break
        pick = True
    reDrawAll()
    playerTurn = True #tells the program that the computer is done picking, now the user's turn

#MAIN FUNCTION    
if __name__ == "__main__":
    
    #DICTIONARIES
    data = {}
    data["continue"] = True #makes the function run
    data["shipCount"] = 0 #counts number of ships
    data["computerHits"] = 0 #counts number of times the computer hits a ship
    data["playerHits"] = 0 #counts number of times the player hits a ship
    
    #COLORS
    gray = Color(0xD3D3D3, 1)
    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    
    #STUFF TO BE SPRITED
    circle_empty = CircleAsset(RADIUS, LineStyle(1,black), white)
    circle_miss = CircleAsset(RADIUS, LineStyle(1,black), blue)
    circle_hit = CircleAsset(RADIUS, LineStyle(1,black), red)
    circle_ship = CircleAsset(RADIUS, LineStyle(1,black), gray)
    
    #KEEPING TRACK OF THE GAME BOARDS
    data["playerBoard"] = buildBoard()
    data["computerBoard"] = buildBoard()
    
    #STARTS THE PROGRAM
    pickComputerShips()
    reDrawAll()

    App().listenMouseEvent("click", mouseClick)
    App().run()
    
