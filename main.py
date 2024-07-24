from cmu_graphics import *
from welcomeScreen import *
from playScreen import *

def onAppStart(app):
    app.rows = 9
    app.cols = 9
    app.boardWidth = 600
    app.boardHeight = 600
    app.boardLeft = 50
    app.boardTop = 50
    app.selectedBoard = None
    app.cellBorderWidth = 1

# learned how to do from TP Resources
def main():
    runAppWithScreens(initialScreen='welcome', width=700, height=700)

main()