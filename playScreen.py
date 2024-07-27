from cmu_graphics import *
from SudokuBoard import *
from options import *
import random

def play_onAppStart(app):
    app.selection = None
    app.nums = [[1,2,3],[4,5,6],[7,8,9]]

def play_onScreenActivate(app):
    selectBoard(app)
    app.selectedBoard = SudokuBoard(app.selectedBoard)
    app.background = 'seashell'
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)
    drawSelections(app)

def play_onMousePress(app, mouseX, mouseY):
    if 600 <= mouseX <= 850 and 510 <= mouseY <= 550:
        setActiveScreen('help')
    if Cell.getCell(app, mouseX, mouseY) != None:
        selectedCell = Cell.getCell(app, mouseX, mouseY)
        row, col = selectedCell
        if app.selectedBoard.board[row][col].permanent == False:
            app.selection = selectedCell
    if getNum(app, mouseX, mouseY) != None and app.selection != None:
        row, col = app.selection
        app.selectedBoard.board[row][col].value = getNum(app, mouseX, mouseY)

def play_onKeyPress(app, key):
    if app.selection != None:
        val = None
        for _ in range(1, 10):
            val = key
        row, col = app.selection
        app.selectedBoard.board[row][col].value = val

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