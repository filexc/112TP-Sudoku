from cmu_graphics import *
from welcomeScreen import *
from playScreen import *
from helpScreen import *
from levelSelectionScreen import *

def onAppStart(app):
    app.rows = 9
    app.cols = 9
    app.boardWidth = 500
    app.boardHeight = 500
    app.boardLeft = 50
    app.boardTop = 50
    app.selectedBoard = None
    app.cellBorderWidth = 1

def main():
    # learned how to do from TP Resources
    runAppWithScreens(initialScreen='welcome', width=900, height=600)

main()