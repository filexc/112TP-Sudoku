from cmu_graphics import *
from legality import *
import math

class Cell:
    def __init__(self, value):
        self.value = value if value != 0 else None
        self.permanent = True if self.value != None else False
        self.row = None
        self.col = None
        #TODO: need a correct value, candidates displayed, and legals property
    
    def drawCell(self, app, row, col):
        self.row, self.col = row, col
        cellLeft, cellTop = self.getCellLeftTop(app, self.row, self.col)
        cellWidth, cellHeight = self.getCellSize(app)
        color = None
        if self.permanent:
            color = 'gray'
        elif self.value != None:
            if not isLegal(app.selectedBoard, self, self.value):
                color = 'red'
        if color == None:
            if app.selection == (self.row, self.col):
                color = 'yellow'
            else:
                color = None
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
    def getCell(app, x, y):
        dx = x - app.boardLeft
        dy = y - app.boardTop
        cellWidth, cellHeight = Cell.getCellSize(app)
        row = math.floor(dy / cellHeight)
        col = math.floor(dx / cellWidth)
        if (0 <= row < app.rows) and (0 <= col < app.cols):
            return (row, col)
        else:
            return None

    @staticmethod
    def getCellSize(app):
        cellWidth = app.boardWidth / app.cols
        cellHeight = app.boardHeight / app.rows
        return (cellWidth, cellHeight)