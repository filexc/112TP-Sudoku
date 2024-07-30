from cmu_graphics import *
import SudokuBoard
from legality import *
import math

class Cell:
    def __init__(self, value, row, col):
        self.value = value if value != 0 else None
        self.permanent = True if self.value != None else False
        self.row = row
        self.col = col
        self.legals = []
        self.userCandidates = []
        #TODO: need a correct value
    
    def drawCell(self, app, row, col):
        self.row, self.col = row, col
        cellLeft, cellTop = self.getCellLeftTop(app, self.row, self.col)
        cellWidth, cellHeight = self.getCellSize(app)
        color = None
        if self.permanent:
            color = 'gray'
        elif self.value != None:
            if not isLegal(app.selectedBoard.board, self, self.value):
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
        if self.value == None:
            self.displayLegals(app, row, col)

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
    
    def resetLegals(self, board):
        if isinstance(board, SudokuBoard.SudokuBoard):
            board = board.board
        self.userCandidates = (self.userCandidates if app.candidateMode == 
                               'Manual' else self.legals)
        #TODO: figure out how to only create the duplicate once for candidates
        #      so that the user can adjust the candidates, but it will still
        #      auto update
        self.legals.clear()
        for i in range (1, 10):
            if isLegal(board, self, i):
                self.legals.append(i)
    
    def displayLegals(self, app, row, col):
        cellWidth, cellHeight = self.getCellSize(app)
        cellLeft = app.boardLeft + col * cellWidth
        cellTop = app.boardTop + row * cellHeight

        for num in range(9):
            if num + 1 in self.userCandidates:
                drawLabel(num + 1, cellLeft + 8 + 20 * (num % 3), 
                          cellTop + 11 + 18 * (num//3), font='Canela Text')
                
    def __repr__(self):
        return f'{self.value}'