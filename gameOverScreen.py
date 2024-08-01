from cmu_graphics import *

def endgame_onScreenActivate(app):
    app.gameOver = False
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def endgame_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.bgColor)
    drawLabel('You Win', app.width/2, app.height/2 - 50, size=75, 
              fill=app.accentColor, font='Brush Script MT')
    drawReplayButton(app)

def endgame_onMousePress(app, mouseX, mouseY):
    if 340 <= mouseX <= 560 and 350 <= mouseY <= 410:
        setActiveScreen('levels')

def drawReplayButton(app):
    drawRect(app.width/2 - 110, app.height/2 + 50, 220, 60, 
             fill=app.buttonColor, border=app.accentColor, borderWidth=3)
    drawLabel('play again', app.width/2, app.height/2 + 75, size=40, 
              align='center', fill=app.accentColor, font='Canela Text')