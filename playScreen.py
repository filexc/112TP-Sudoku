from cmu_graphics import *
from SudokuBoard import *
from options import *
import random

def play_onAppStart(app):
    pass

def play_onScreenActivate(app):
    selectBoard(app)
    app.selectedBoard = SudokuBoard(app.selectedBoard)
    app.background = 'seashell'
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)
    drawSelections(app) # TODO: make selections clickable

def play_onMousePress(app, mouseX, mouseY):
    if 600 <= mouseX <= 850 and 510 <= mouseY <= 550:
        setActiveScreen('help')

def selectBoard(app):
    if app.level == 'easy' or app.level == 'medium' or app.level == 'hard':
        rand = random.randint(1, 50)
    else:
        rand = random.randint(1, 25)
    if rand < 10:
        rand = '0' + str(rand)
    else:
        rand = str(rand)
    board = readFile(f'boards/{app.level}-{rand}.png.txt')
    res = []
    for line in board.splitlines():
        row = []
        for num in line.split(' '):
            row.append(int(num))
        res.append(row)
    app.selectedBoard = res

# taken from tp resources
def readFile(path):
    with open(path, "rt") as f:
        return f.read()