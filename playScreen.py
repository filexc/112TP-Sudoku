from cmu_graphics import *
from SudokuBoard import *
from options import *

import random

def play_onAppStart(app):
    app.selection = None
    app.nums = [[1,2,3],[4,5,6],[7,8,9]]
    app.gameOver = False

def play_onScreenActivate(app):
    app.background = 'seashell'
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)
    drawSelections(app)

def play_onStep(app):
    app.gameOver = app.selectedBoard.gameIsOver(app)
    if app.gameOver: # also if the board is the correct solution but do that later
        setActiveScreen('endgame')

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
        for i in range(1, 10):
            if key == str(i):
                val = key
                row, col = app.selection
                app.selectedBoard.board[row][col].value = int(val)
    skipToEnd(app, key)
    
#TODO: get rid of but for now TEMP FOR TESTING GAME OVER/REPLAY MODES
def skipToEnd(app, key):
    if key == 's':
        setActiveScreen('endgame')