import os, pathlib
from cmu_graphics import *
from PIL import Image

# taken from TP Resources
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def welcome_onAppStart(app):
    app.background = 'seashell'
    app.accentColor = rgb(57, 34, 77)
    app.bgColor = rgb(174, 151, 219)
    app.buttonColor = rgb(119, 94, 166)
    # image taken from https://www.flaticon.com/free-icon/sudoku_5190595
    # image loading learned on TP resources
    app.icon = Image.open('images/sudoku-icon.png')
    app.icon = CMUImage(app.icon)

def welcome_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.bgColor)
    drawLabel('Sudoku', app.width/2, 110, size=75, fill=app.accentColor, 
              font='Brush Script MT')
    drawImage(app.icon, app.width/2, app.height/2, width=250, height=250, 
              align='center')
    drawPlayButton(app)
    
def drawPlayButton(app):
    drawRect(app.width/2 - 110, 450, 220, 60, fill=rgb(119, 94, 166), 
             border=app.accentColor, borderWidth=3)
    drawLabel('play', app.width/2, 475, size=40, align='center', 
              fill=app.accentColor, font='Canela Text')

def welcome_onMousePress(app, mouseX, mouseY):
    if ((app.width/2 + 110 > mouseX > app.width/2 - 110) and 
        (450 < mouseY < 510)):
         setActiveScreen('levels')

#TODO: get rid of
def welcome_onKeyPress(app, key):
    if key == 's':
        setActiveScreen('endgame')