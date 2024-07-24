from cmu_graphics import *
from SudokuBoard import *

def play_onAppStart(app):
    pass

def play_onScreenActivate(app):
    # app.selectedBoard = [list(range(9)) for _ in range(9)]
    #hard coded dummy board for testing purposes -- not a legal board
    app.selectedBoard = [[1, 5, 2, 4, 6, None, None, 2, 9], 
                         [None, None, None, 3, 5, 7, 8, 9, 1],
                         [7, None, 1, 4, None, 5, 9, None, 3],
                         [1, 5, 2, 4, 6, None, None, 2, 9],
                         [None, None, None, 3, 5, 7, 8, 9, 1],
                         [7, None, 1, 4, None, 5, 9, None, 3],
                         [1, 5, 2, 4, 6, None, None, 2, 9],
                         [None, None, None, 3, 5, 7, 8, 9, 1],
                         [7, None, 1, 4, None, 5, 9, None, 3]]
    app.selectedBoard = SudokuBoard(app.selectedBoard)
    app.background = 'seashell'
    
def play_redrawAll(app):
    app.selectedBoard.drawBoard(app)

def play_onMousePress(app, mouseX, mouseY):
    pass