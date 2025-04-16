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
        self.manuallyRemovedCandidates = set()
        self.correct = None
    
    def drawCell(self, app, row, col):
        self.row, self.col = row, col
        cellLeft, cellTop = self.getCellLeftTop(app, self.row, self.col)
        cellWidth, cellHeight = self.getCellSize(app)
        color = None
        illegal = False # if there's a value on the board that makes it wrong
        incorrect = False # if it's the incorrect value based on the solution
        
        # when the cell is permanently on the board, make it gray
        if self.permanent and app.selection == (self.row, self.col):
            color = rgb(128, 118, 64)
        elif self.permanent:
            color = 'gray'
        # if the cell is highlighted with a hint and it's selected, make it a 
        # mix of yellow and green
        elif (app.highlighted != None and (app.highlighted.row, app.highlighted.
                                          col) == (self.row, self.col) and app.
                                          selection == (self.row, self.col)):
            color = rgb(199, 222, 72)
        # if the cell is highlighted with a hint, make it green
        elif (app.highlighted != None and (app.highlighted.row, app.highlighted.
                                          col) == (self.row, self.col)):
            color = 'darkSeaGreen'
        # if the cell is highlighted with a row hint aid and it's selected, make
        # it a mix of the hint aid color and yellow
        elif (app.hintType == "Row Single" and (app.highlighted.row == self.row)
                                                and app.selection == (self.row, 
                                                                      self.col)):
            color = rgb(236, 249, 108)
        # if the cell is highlighted with a row hint aid make it hint aid green
        elif app.hintType == "Row Single" and app.highlighted.row == self.row:
            color = rgb(216, 242, 216)
        # if the cell is highlighted with a col hint aid and it's selected, make
        # it a mix of the hint aid color and yellow
        elif (app.hintType == "Col Single" and (app.highlighted.col == self.col)
                                                and app.selection == (self.row, 
                                                                      self.col)):
            color = rgb(236, 249, 108)
        # if the cell is highlighted with a col hint aid make it hint aid green
        elif app.hintType == "Col Single" and app.highlighted.col == self.col:
            color = rgb(216, 242, 216)
        # if the cell is highlighted with a block hint aid and it's selected,
        # make it a mix of the hint aid color and yellow
        elif app.hintType == "Block Single" and app.selection == (self.row, self.col):
            hRow = app.highlighted.row
            hCol = app.highlighted.col
            row = self.row
            col = self.col
            if (((hRow % 3 == 0 and (row == hRow or row == hRow + 1 or row == hRow + 2)) 
                or (hRow % 3 == 1) and (row == hRow - 1 or row == hRow or row == hRow + 1)
                or (hRow % 3 == 2) and (row == hRow - 2 or row == hRow - 1 or row == hRow)) 
                and ((hCol % 3 == 0 and (col == hCol or col == hCol + 1 or col == hCol + 2)) 
                or (hCol % 3 == 1) and (col == hCol - 1 or col == hCol or col == hCol + 1)
                or (hCol % 3 == 2) and (col == hCol - 2 or col == hCol - 1 or col == hCol))):
                color = rgb(236, 249, 108)
        # if the cell is hihglighted with a block hint aid, make it hint aid green
        elif app.hintType == "Block Single":
            hRow = app.highlighted.row
            hCol = app.highlighted.col
            row = self.row
            col = self.col
            if (((hRow % 3 == 0 and (row == hRow or row == hRow + 1 or row == hRow + 2)) 
                or (hRow % 3 == 1) and (row == hRow - 1 or row == hRow or row == hRow + 1)
                or (hRow % 3 == 2) and (row == hRow - 2 or row == hRow - 1 or row == hRow)) 
                and ((hCol % 3 == 0 and (col == hCol or col == hCol + 1 or col == hCol + 2)) 
                or (hCol % 3 == 1) and (col == hCol - 1 or col == hCol or col == hCol + 1)
                or (hCol % 3 == 2) and (col == hCol - 2 or col == hCol - 1 or col == hCol))):
                color = rgb(216, 242, 216)
        
        # if the cell is selected, make it yellow
        elif app.selection == (self.row, self.col):
            color = 'yellow'

        if self.value != self.correct.value:
            incorrect = True
        if not isLegal(app.selectedBoard.board, self, self.value):
            illegal = True
        
        drawRect(cellLeft, cellTop, cellWidth, cellHeight, fill=color, 
                 border='black', borderWidth=app.cellBorderWidth)
        if self.value != None:
            drawLabel(self.value, cellLeft + cellWidth/2, (cellTop + 
                      cellHeight/2), size=16, font='Canela Text')
            if illegal:
                drawCircle(cellLeft + cellWidth - 10, cellTop + cellHeight - 10,
                           5, fill='red')
            if incorrect and app.autocorrect:
                drawLine(cellLeft + cellWidth, cellTop, cellLeft, cellTop + 
                         cellHeight, fill='red')
        else:
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

        # Recalculate legal values
        self.legals.clear()
        for i in range(1, 10):
            if isLegal(board, self, i):
                self.legals.append(i)

        # Update userCandidates based on mode
        if app.candidateMode == 'Automatic':
            if self.userCandidates == []:
                self.userCandidates = self.legals.copy()
            else:
                # Keep user-removed candidates while syncing with new legals
                self.userCandidates = [
                    candidate for candidate in self.userCandidates if candidate in self.legals
                ]

                for legal in self.legals:
                    if legal not in self.userCandidates and legal not in self.manuallyRemovedCandidates:
                        self.userCandidates.append(legal)
                self.userCandidates = sorted(self.userCandidates)
        else:
            # In Manual mode, userCandidates remain unchanged
            self.userCandidates = self.userCandidates or []

    def removeCandidate(self, candidate):
        if candidate in self.userCandidates:
            self.userCandidates.remove(candidate)
            self.manuallyRemovedCandidates.add(candidate)
        print("user candidates: ",self.userCandidates)
        print("legals: ", self.legals)
    
    def addCandidate(self, candidate):        
        if candidate not in self.userCandidates:
            self.userCandidates.append(candidate)
            self.manuallyRemovedCandidates.discard(candidate)
    
    def displayLegals(self, app, row, col):
        cellWidth, cellHeight = self.getCellSize(app)
        cellLeft = app.boardLeft + col * cellWidth
        cellTop = app.boardTop + row * cellHeight

        for num in range(9):
            if num + 1 in self.userCandidates:
                drawLabel(num + 1, cellLeft + 8 + 20 * (num % 3), 
                          cellTop + 11 + 18 * (num//3), font='Canela Text', 
                          fill='gray')
                
    def __repr__(self):
        return f'{self.value}'