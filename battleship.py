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
    

if __name__ == "__main__":
    
    data = {}
    board = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]]

    buildBoard()

    
    white = Color(0xFFFFFF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    
    
