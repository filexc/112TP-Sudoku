from math import sqrt
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
    
    def findHints(self, board):
        hint = self.findOnlyOneLegalHint(board)
        if hint != None:
            return hint
        hint = self.findHiddenSingleHint(board)
        return hint
    
    def findHiddenSingleHint(self, board):
        # Check each row
        for row in range(len(board)):
            counts = self.countLegalValues([board[row][col] for col in range(len(board[row]))])
            for val, cells in counts.items():
                if len(cells) == 1:
                    cell = cells[0] #this is because there is only one cell for this value in the dictionary, therefore we get the 0th position
                    # print("row single", val)
                    return cell.row, cell.col

        # Check each column
        for col in range(len(board[0])):
            counts = self.countLegalValues([board[row][col] for row in range(len(board))])
            for val, cells in counts.items():
                if len(cells) == 1:
                    cell = cells[0] #this is because there is only one cell for this value in the dictionary, therefore we get the 0th position
                    # print("col single", val)
                    return cell.row, cell.col

        # Check each 3x3 box
        for boxRow in range(0, len(board), int(sqrt(len(board)))):
            for boxCol in range(0, len(board[boxRow]), int(sqrt(len(board[boxRow])))):
                block = [board[row][col]
                        for row in range(boxRow, boxRow + int(sqrt(len(board))))
                        for col in range(boxCol, boxCol + int(sqrt(len(board[row]))))]
                counts = self.countLegalValues(block)
                for val, cells in counts.items():
                    if len(cells) == 1:
                        cell = cells[0] #this is because there is only one cell for this value in the dictionary, therefore we get the 0th position
                        # print("block single", val)
                        return cell.row, cell.col
        return None


    def countLegalValues(self, cells):
        counts = {}
        for cell in cells:
            if cell.value == None:
                for val in cell.legals:
                    if val not in counts:
                        counts[val] = []
                    counts[val].append(cell)
        return counts