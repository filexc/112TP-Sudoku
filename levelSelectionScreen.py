from cmu_graphics import *
from SudokuBoard import *

import random

def levels_onAppStart(app):
    app.labels = ['easy', 'medium', 'hard', 'expert', 'evil']

def levels_onScreenActivate(app):
    app.level = None
    app.selection = None

def levels_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.welcomeBGColor)
    drawLabel('Choose Level', app.width/2, 110, size=60, 
              fill=app.welcomeColor, align='center', font='Brush Script MT')
    drawButtons(app)

def levels_onMousePress(app, mouseX, mouseY):
    if app.width/2 + 110 >= mouseX >= app.width/2 - 110:
        for i in range(5):
            if i * 75 + 213 >= mouseY >= i * 75 + 163:
                app.level = app.labels[i]
                selectBoard(app)
                app.selectedBoard = SudokuBoard(app.selectedBoard)
                for row in range(app.selectedBoard.rows):
                    for col in range(app.selectedBoard.cols):
                        app.selectedBoard.board[row][col].resetLegals(app.selectedBoard)
                setActiveScreen('play')

def drawButtons(app):
    for i in range(5):
        drawRect(app.width/2 - 110, i * 75 + 163, 220, 50, fill=rgb(119, 94, 166), 
             border=app.welcomeColor, borderWidth=3)
        drawLabel(app.labels[i], app.width/2, i * 75 + 187, fill=app.welcomeColor, 
                  font='Canela Text', size=16)
        
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