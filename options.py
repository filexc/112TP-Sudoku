from cmu_graphics import *

def drawSelections(app):
    left = app.boardLeft + app.boardWidth + 50
    top = app.boardTop + 60
    size = 250
    drawRect(left, top, size, size, fill='lightGray', border='gray', borderWidth=2)
    drawHeadings(app, left, size)
    drawNumSquares(left, top, size)
    drawHelpButton(app, left, size)
    
def drawHeadings(app, left, width):
    drawRect(left + 1, app.boardTop, width / 2, 40, fill='lightGray', 
             border='gray')
    drawRect(left + 124, app.boardTop, width / 2, 40,
             fill='lightGray', border='gray')
    drawLabel('Normal', left + 64, app.boardTop + 20, size=16, 
              font='Canela Text')
    drawLabel('Candidate', left + 187, app.boardTop + 20, size=16, 
              font='Canela Text')
    
def drawNumSquares(left, top, size):
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    for row in range(3):
        for col in range(3):
            drawRect(left + size/3*col, top + size/3*row, size/3, size/3,
                     fill=None, border='gray', borderWidth=1)
            drawLabel(nums[row][col], left + size/3*col + size/6, 
                      top + size/3*row + size/6, size=16, font='Canela Text')
            
def drawHelpButton(app, left, width):
    drawRect(left, 510, width, 40, fill='lightGray', border='gray')
    drawLabel('Help', left + width/2, 530, size=16, font='Canela Text')
