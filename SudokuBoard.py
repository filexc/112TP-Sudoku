from cmu_graphics import *
from Cell import *

class SudokuBoard:
    def __init__(self, board):
        self.rows = 9
        self.cols = 9
        self.board = board
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.board[row][col] = Cell(board[row][col])

    def drawBoard(self, app):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
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
                if self.board[row][col].value == None:
                    return False
        return True