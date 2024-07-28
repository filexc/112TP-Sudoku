from cmu_graphics import *

def levels_onAppStart(app):
    app.level = None
    app.labels = ['easy', 'medium', 'hard', 'expert', 'evil']

def levels_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.welcomeBGColor)
    drawLabel('Choose Level', app.width/2, 110, size=60, 
              fill=app.welcomeColor, align='center', font='Brush Script MT')
    drawButtons(app)

def levels_onMousePress(app, mouseX, mouseY):
    if app.width/2 + 110 >= mouseX >= app.width/2 - 110:
        for i in range(5):
            if i * 75 + 213 >= mouseY >= i * 75 + 163:
                app.level = app.labels[i]
                setActiveScreen('play')

def drawButtons(app):
    for i in range(5):
        drawRect(app.width/2 - 110, i * 75 + 163, 220, 50, fill=rgb(119, 94, 166), 
             border=app.welcomeColor, borderWidth=3)
        drawLabel(app.labels[i], app.width/2, i * 75 + 187, fill=app.welcomeColor, 
                  font='Canela Text', size=16)