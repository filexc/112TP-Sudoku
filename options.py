from cmu_graphics import *
import math

def drawSelections(app):
    left = app.boardLeft + app.boardWidth + 50
    top = app.boardTop + 60
    size = 250
    drawRect(left, top, size, size, fill='lightGray', border='gray', borderWidth=2)
    drawHeadings(app, left, size)
    drawNumSquares(left, top, size)
    drawHelpButton(app, left, size)
    drawCandidateModeCheckbox(app, left)
    
def drawHeadings(app, left, width):
    if app.mode == 'Candidate':
        cColor, cText = 'black', 'white'
        nColor, nText = 'lightGray', 'black'
    elif app.mode == 'Normal':
        cColor, cText = 'lightGray', 'black'
        nColor, nText = 'black', 'white'
    drawRect(left + 1, app.boardTop, width / 2, 40, fill=nColor, 
             border='gray')
    drawRect(left + 124, app.boardTop, width / 2, 40, fill=cColor,
             border='gray')
    drawLabel('Normal', left + 64, app.boardTop + 20, size=16, 
              font='Canela Text', fill=nText)
    drawLabel('Candidate', left + 187, app.boardTop + 20, size=16, 
              font='Canela Text', fill=cText)
    
def drawNumSquares(left, top, size):
    for row in range(3):
        for col in range(3):
            drawRect(left + size/3*col, top + size/3*row, size/3, size/3,
                     fill=None, border='gray', borderWidth=1)
            drawLabel(app.nums[row][col], left + size/3*col + size/6, 
                      top + size/3*row + size/6, size=16, font='Canela Text')
            
def drawHelpButton(app, left, width):
    drawRect(left, 510, width, 40, fill='lightGray', border='gray')
    drawLabel('Help', left + width/2, 530, size=16, font='Canela Text')

def getNum(app, x, y):
        dx = x - (app.boardLeft + app.boardWidth + 50)
        dy = y - (app.boardTop + 60)
        cellSize = 250/3
        row = math.floor(dy / cellSize)
        col = math.floor(dx / cellSize)
        if (0 <= row < 3) and (0 <= col < 3):
            return app.nums[row][col]
        else:
            return None
        
def drawCandidateModeCheckbox(app, left):
    if app.candidateMode == 'Manual':
        drawLabel(chr(0x2610), left + 10, 400, size=24, 
                  font='Noto Sans Symbols 2')
    elif app.candidateMode == 'Automatic':
        drawLabel(chr(0x2611), left + 10, 400, size=24, 
                  font='Noto Sans Symbols 2')
    drawLabel('Auto Candidate Mode', left + 110, 400, size=16,
              font='Canela Text')