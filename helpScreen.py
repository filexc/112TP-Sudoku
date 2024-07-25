from cmu_graphics import *

def help_onAppStart(app):
    app.helpColor = rgb(204, 204, 255)
    app.helpBGColor = 'lavender'
    app.helpTextColor = rgb(65, 65, 122)

def help_onScreenActivate(app):
    app.background = app.helpBGColor
    
def help_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.helpColor)
    drawLabels(app)
    drawBackToHomeButton(app)

def drawLabels(app):
    drawLabel('How to Play Sudoku', app.width/2, 110, size=60, 
              fill=app.helpTextColor, align='center', font='Brush Script MT')
    drawLabel('Fill in a 9x9 board with numbers from 1-9', 100, 175, size=24, 
              fill=app.helpTextColor, font='Canela Text', align='left')
    drawLabel('  - No repeated numbers in each line vertically or horizontally',
              100, 200, size=18, fill=app.helpTextColor, font='Canela Text',
              align='left')
    drawLabel('  - No repeated numbers in each 3x3 square', 100, 225, size=18, 
              fill=app.helpTextColor, font='Canela Text', align='left')
    drawLabel('  - Each number must appear only 9 times on the board', 100, 250,
              size=18, fill=app.helpTextColor, font='Canela Text', align='left')
    
    # TODO: add the instructions on how to play

def drawBackToHomeButton(app):
    drawRect(75, 75, 100, 35, fill=rgb(160, 160, 235), border=app.helpTextColor)
    drawLabel('Back to Game', 125, 93, align='center', font='Canela Text',
              fill=app.helpTextColor)

def help_onMousePress(app, mouseX, mouseY):
    if 175 >= mouseX >= 75 and 110 >= mouseY >= 75:
        setActiveScreen('play')