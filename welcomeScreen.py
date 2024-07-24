import os, pathlib
from cmu_graphics import *
from PIL import Image

# taken from TP Resources
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def welcome_onAppStart(app):
    app.background = 'white'
    app.welcomeColor = rgb(57, 34, 77)
    app.welcomeBGColor = rgb(174, 151, 219)
    # image taken from https://www.flaticon.com/free-icon/sudoku_5190595
    app.icon = Image.open('images/sudoku-icon.png')
    app.icon = CMUImage(app.icon)

def welcome_onScreenActivate(app):
    app.background = 'white'

def welcome_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.welcomeBGColor)
    drawLabel('Sudoku', app.width/2, 150, size=75, fill=app.welcomeColor, 
              font='Brush Script MT')
    drawImage(app.icon, app.width/2, app.height/2, width=250, height=250, 
              align='center')
    drawPlayButton(app)
    
def drawPlayButton(app):
    drawRect(app.width/2 - 110, 500, 220, 60, fill=rgb(119, 94, 166), 
             border=app.welcomeColor, borderWidth=3)
    drawLabel('play', app.width/2, 525, size=40, align='center', 
              fill=app.welcomeColor, font='Canela Text')

def welcome_onMousePress(app, mouseX, mouseY):
    if ((app.width/2 + 110 > mouseX > app.width/2 - 110) and 
        (500 < mouseY < 560)):
         setActiveScreen('play')