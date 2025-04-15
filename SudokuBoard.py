from cmu_graphics import *
from Cell import *
import copy

class SudokuBoard:
    def __init__(self, board):
        self.rows = 9
        self.cols = 9
        self.board = board
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.board[row][col] = Cell(board[row][col], row, col)
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col].resetLegals(self)
        self.sol = self.solveBoard(self.board)
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col].correct = self.sol[row][col]
        for line in self.sol: # TODO: prints the generated solution for testing purposes
            print(line)

    def drawBoard(self, app):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col].row = row
                self.board[row][col].col = col
                self.board[row][col].drawCell(app, row, col)
        SudokuBoard.drawBoardBorders(app)

    @staticmethod
    def drawBoardBorders(app):
        drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
                 fill=None, border='black', borderWidth=4 * app.cellBorderWidth)
        cellWidth, cellHeight = Cell.getCellSize(app)
        for v in range(3, 7, 3):
            drawLine(app.boardLeft + cellWidth * v, app.boardTop, (app.boardLeft
                     + cellWidth * v), app.boardTop + app.boardHeight,
                     lineWidth=4 * app.cellBorderWidth)
            drawLine(app.boardLeft, app.boardTop + cellHeight * v, 
                     app.boardLeft + app.boardWidth, (app.boardTop + cellHeight
                     * v), lineWidth=4 * app.cellBorderWidth)
            
    def gameIsOver(self, app):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                cell = self.board[row][col]
                if (cell.value == None or cell.value != cell.correct.value):
                    return False
        return True
    
    def solveBoard(self, board):
        board = copy.deepcopy(board)
        return self.backtracker(board)
        
    def backtracker(self, board):
        cellWithSmallestLegals = self.findSmallestLegals(board)
        row, col, legals = cellWithSmallestLegals
        if cellWithSmallestLegals == (None, None, None):
            return board
        for val in legals:
            board[row][col].value = val
            oldLegals = board[row][col].legals
            self.resetAffectedBoardLegals(board, row, col)
            posSol = self.backtracker(board)
            if posSol != None:
                return posSol
            board[row][col].value = None
            board[row][col].legals = oldLegals
            self.resetAffectedBoardLegals(board, row, col)
        return None
        
    def findSmallestLegals(self, board):
        smallestRow, smallestCol = None, None
        smallestLegals = None
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col].value == None:
                    if smallestLegals == None or (len(smallestLegals) == 1 or 
                        len(board[row][col].legals) < len(smallestLegals)):
                        smallestRow, smallestCol = row, col
                        smallestLegals = board[row][col].legals
                        if len(smallestLegals) == 1:
                            return smallestRow, smallestCol, smallestLegals
        return smallestRow, smallestCol, smallestLegals
    
    def resetAffectedBoardLegals(self, board, row, col):
        blockStartRow = row//3 * 3
        blockStartCol = col//3 * 3

        for c in range(len(board[row])):
            board[row][c].resetLegals(board)
        for r in range(len(board)):
            board[r][col].resetLegals(board)
        for r in range(blockStartRow, blockStartRow + 3):
            for c in range(blockStartCol, blockStartCol + 3):
                board[r][c].resetLegals(board)

    def findOnlyOneLegalHint(self, board):
        row, col, smallestLegals = self.findSmallestLegals(board)
        if len(smallestLegals) == 1:
            return row, col
        return None
    #TODO: make it so the hint also appears if there's only one of a value in a row, col, or box