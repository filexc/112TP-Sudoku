import time
from cmu_graphics import *
from SudokuBoard import *
from options import *

def play_onAppStart(app):
    app.selection = None
    app.nums = [[1,2,3],[4,5,6],[7,8,9]]
    app.mode = 'Normal'
    app.candidateMode = 'Manual'
    app.autocorrect = False
    app.popupError = False
    app.firstTimeInState = True
    app.initTime = None
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)
    drawSelections(app)
    drawHintButton(app)

def play_onStep(app):
    app.gameOver = app.selectedBoard.gameIsOver(app)
    if app.gameOver:
        setActiveScreen('endgame')
    # found time class/method online on 
    # https://www.geeksforgeeks.org/python-time-time-method/, 
    # but didn't look at code
    if app.popupError:
        if app.firstTimeInState:
            app.initTime = time.time()
            app.firstTimeInState = False
        if time.time() - 2.5 >= app.initTime:
            app.popupError = False
            app.firstTimeInState = True
            app.initTime = None

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
        if key == 'up' and app.selection[0] - 1 >= 0:
            app.selection = app.selection[0] - 1, app.selection[1]
        elif key == 'down' and app.selection[0] + 1 < app.rows:
            app.selection = app.selection[0] + 1, app.selection[1]
        elif key == 'left' and app.selection[1] - 1 >= 0:
            app.selection = app.selection[0], app.selection[1] - 1
        elif key == 'right' and app.selection[1] + 1 < app.cols:
            app.selection = app.selection[0], app.selection[1] + 1
        val = None
        if not board[app.selection[0]][app.selection[1]].permanent:
            for i in range(1, 10):
                if key == str(i):
                    val = key
                    row, col = app.selection
                    if app.mode == 'Normal':
                        board[row][col].value = int(val)
                    elif app.mode == 'Candidate':
                        if app.candidateMode == 'Manual':
                            if (int(val) not in board[row][col].userCandidates):
                                board[row][col].userCandidates.append(int(val))
                            else:
                                board[row][col].userCandidates.remove(int(val))
                        elif app.candidateMode == "Automatic":
                            if (int(val) not in board[row][col].userCandidates):
                                board[row][col].addCandidate(int(val))
                            else:
                                board[row][col].removeCandidate(int(val))
                    if app.highlighted == board[row][col]:
                        app.hintStep = None
                        app.highlighted = None
                    adjustLegals(app.selectedBoard)
    welcome_onKeyPress(app, key)

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
    if num != None and app.selection != None and not board[app.selection[0]][app.selection[1]].permanent:
        row, col = app.selection
        if app.mode == 'Normal':
          board[row][col].value = num
        elif app.mode == 'Candidate':
            if app.candidateMode == 'Manual':
                if (num not in board[row][col].userCandidates):
                    board[row][col].userCandidates.append(num)
                else:
                    board[row][col].userCandidates.remove(num)
            elif app.candidateMode == "Automatic":
                if (num not in board[row][col].userCandidates):
                    board[row][col].addCandidate(num)
                else:
                    board[row][col].removeCandidate(num)
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
            if app.selectedBoard.findHints(board) != None:
                row, col, app.hintType = app.selectedBoard.findHints(board)
                app.highlighted = board[row][col]
                app.hintStep = 'Highlighted'
            else:
                app.popupError = True
        elif app.hintStep == 'Highlighted':
            row, col = app.highlighted.row, app.highlighted.col
            board[row][col].value = board[row][col].correct.value
            app.selectedBoard.resetAffectedBoardLegals(board, row, col)
            app.hintStep = None
            app.highlighted = None
            app.hintType = None

def drawHintButton(app):
    left = app.boardLeft + app.boardWidth + 50
    width = 250
    drawRect(left, 473, width, 40, fill='lightGray', border='gray')
    if app.popupError:
        drawLabel('No hint currently available', left + width/2, 493, size=16, 
                  font='Canela Text', fill='red')
    elif app.hintStep == None:
        drawLabel('Get Hint', left + width/2, 493, size=16, font='Canela Text')
    elif app.hintStep == 'Highlighted':
        drawLabel('Apply Hint', left + width/2, 493, size=16, font='Canela Text')

#TODO: get rid of
def welcome_onKeyPress(app, key):
    if key == 's':
        setActiveScreen('endgame')