from cmu_graphics import *

class Cell:
    def __init__(self, value):
        self.value = value
        self.permanent = True if self.value != None else False
        #TODO: need a correct value, candidates displayed, and legals property
    
    def drawCell(self, app, row, col):
        cellLeft, cellTop = self.getCellLeftTop(app, row, col)
        cellWidth, cellHeight = self.getCellSize(app)
        color = 'gray' if self.permanent else None
        drawRect(cellLeft, cellTop, cellWidth, cellHeight, fill=color, 
                 border='black', borderWidth=app.cellBorderWidth)
        if self.value != None:
            drawLabel(self.value, cellLeft + cellWidth/2, (cellTop + 
                      cellHeight/2), size=16, font='Canela Text')

    def getCellLeftTop(self, app, row, col):
        cellWidth, cellHeight = self.getCellSize(app)
        cellLeft = app.boardLeft + col * cellWidth
        cellTop = app.boardTop + row * cellHeight
        return (cellLeft, cellTop)

    @staticmethod
    def getCellSize(app):
        cellWidth = app.boardWidth / app.cols
        cellHeight = app.boardHeight / app.rows
        return (cellWidth, cellHeight)