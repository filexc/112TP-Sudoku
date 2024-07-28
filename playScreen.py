from cmu_graphics import *
from SudokuBoard import *
from options import *

import random

def play_onAppStart(app):
    app.selection = None
    app.nums = [[1,2,3],[4,5,6],[7,8,9]]
    app.gameOver = False
    app.mode = 'Normal'
    app.candidateMode = 'Manual'

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
    board = app.selectedBoard
    if 600 <= mouseX <= 850 and 510 <= mouseY <= 550:
        setActiveScreen('help')
    if Cell.getCell(app, mouseX, mouseY) != None:
        selectedCell = Cell.getCell(app, mouseX, mouseY)
        row, col = selectedCell
        if board.board[row][col].permanent == False:
            app.selection = selectedCell
    num = getNum(app, mouseX, mouseY)
    if num != None and app.selection != None:
        row, col = app.selection
        if app.mode == 'Normal':
          board.board[row][col].value = num
        elif app.mode == 'Candidate':
            if (num not in board.board[row][col].userCandidates):
                board.board[row][col].userCandidates.append(num)
            else:
                board.board[row][col].userCandidates.remove(num)
        adjustLegals(app.selectedBoard)
    if 50 <= mouseY <= 90:
        if 600 <= mouseX <= 725: # don't currently know the conditions
            app.mode = 'Normal'
        elif 725 <= mouseX <= 850:
            app.mode = 'Candidate'
    if 600 <= mouseX <= 620 and 390 <= mouseY <= 420:
        app.candidateMode = 'Automatic' if app.candidateMode == 'Manual' else 'Manual'
        updateCandidates(app)

def play_onKeyPress(app, key):
    board = app.selectedBoard
    if app.selection != None:
        val = None
        for i in range(1, 10):
            if key == str(i):
                val = key
                row, col = app.selection
                if app.mode == 'Normal':
                    board.board[row][col].value = int(val)
                elif app.mode == 'Candidate':
                    if (int(val) not in board.board[row][col].userCandidates):
                        board.board[row][col].userCandidates.append(int(val))
                    else:
                        board.board[row][col].userCandidates.remove(int(val))
                adjustLegals(app.selectedBoard)
    skipToEnd(app, key)
    
#TODO: get rid of but for now TEMP FOR TESTING GAME OVER/REPLAY MODES
def skipToEnd(app, key):
    if key == 's':
        setActiveScreen('endgame')

def adjustLegals(board):
    for row in range(board.rows):
        for col in range(board.cols):
            board.board[row][col].resetLegals(board)

def updateCandidates(app):
    board = app.selectedBoard
    for row in range(board.rows):
        for col in range(board.cols):
            if app.candidateMode == 'Manual':
                board.board[row][col].userCandidates = []
            else:
                board.board[row][col].userCandidates = (board.board[row][col]
                                                        .legals)