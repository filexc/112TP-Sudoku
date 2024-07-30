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
    app.autocorrect = False

def play_onScreenActivate(app):
    app.background = 'seashell'
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)
    drawSelections(app)
    drawHintButton(app)

def play_onStep(app):
    app.gameOver = app.selectedBoard.gameIsOver(app)
    if app.gameOver: # also if the board is the correct solution but do that later
        setActiveScreen('endgame')

def play_onMousePress(app, mouseX, mouseY):
    board = app.selectedBoard.board
    if 600 <= mouseX <= 850 and 510 <= mouseY <= 550:
        setActiveScreen('help')
    selectCell(app, board, mouseX, mouseY)
    useNumPad(app, board, mouseX, mouseY)
    changeGameMode(app, mouseX, mouseY)
    toggleCandidateMode(app, mouseX, mouseY)
    toggleAutocorrect(app, mouseX, mouseY)
    clickHintButton(app, mouseX, mouseY, board)


def play_onKeyPress(app, key):
    board = app.selectedBoard.board
    if app.selection != None:
        val = None
        for i in range(1, 10):
            if key == str(i):
                val = key
                row, col = app.selection
                if app.mode == 'Normal':
                    board[row][col].value = int(val)
                elif app.mode == 'Candidate':
                    if (int(val) not in board[row][col].userCandidates):
                        board[row][col].userCandidates.append(int(val))
                    else:
                        board[row][col].userCandidates.remove(int(val))
                if app.highlighted == board[row][col]:
                    app.hintStep = None
                    app.highlighted = None
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
                
def selectCell(app, board, mouseX, mouseY):
    if Cell.getCell(app, mouseX, mouseY) != None:
        selectedCell = Cell.getCell(app, mouseX, mouseY)
        row, col = selectedCell
        if board[row][col].permanent == False:
            app.selection = selectedCell

def useNumPad(app, board, mouseX, mouseY):
    num = getNum(app, mouseX, mouseY)
    if num != None and app.selection != None:
        row, col = app.selection
        if app.mode == 'Normal':
          board[row][col].value = num
        elif app.mode == 'Candidate':
            if (num not in board[row][col].userCandidates):
                board[row][col].userCandidates.append(num)
            else:
                board[row][col].userCandidates.remove(num)
        if app.highlighted == board[row][col]:
            app.hintStep = None
            app.highlighted = None
        adjustLegals(app.selectedBoard)

def changeGameMode(app, mouseX, mouseY):
    if 50 <= mouseY <= 90:
        if 600 <= mouseX <= 725:
            app.mode = 'Normal'
        elif 725 <= mouseX <= 850:
            app.mode = 'Candidate'
        
def toggleCandidateMode(app, mouseX, mouseY):
    if 600 <= mouseX <= 620 and 390 <= mouseY <= 420:
        app.candidateMode = 'Automatic' if app.candidateMode == 'Manual' else 'Manual'
        updateCandidates(app)

def toggleAutocorrect(app, mouseX, mouseY):
    if 600 <= mouseX <= 620 and 440 <= mouseY <= 470:
        app.autocorrect = not app.autocorrect

def clickHintButton(app, mouseX, mouseY, board):
    if 600 <= mouseX <= 850 and 473 <= mouseY <= 513:
        if app.hintStep == None:
            if app.selectedBoard.findOnlyOneLegalHint(board) != None:
                row, col = app.selectedBoard.findOnlyOneLegalHint(board)
                app.highlighted = board[row][col]
                app.hintStep = 'Highlighted'
        elif app.hintStep == 'Highlighted':
            row, col = app.highlighted.row, app.highlighted.col
            board[row][col].value = board[row][col].correct.value
            app.selectedBoard.resetBoardLegals(board, row, col)
            app.hintStep = None
            app.highlighted = None

def drawHintButton(app):
    left = app.boardLeft + app.boardWidth + 50
    width = 250
    drawRect(left, 473, width, 40, fill='lightGray', border='gray')
    if app.hintStep == None:
        drawLabel('Get Hint', left + width/2, 493, size=16, font='Canela Text')
    elif app.hintStep == 'Highlighted':
        drawLabel('Apply Hint', left + width/2, 493, size=16, font='Canela Text')