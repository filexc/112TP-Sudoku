from cmu_graphics import *

def help_redrawAll(app):
    drawRect(50, 50, app.width - 100, app.height - 100, fill=app.bgColor)
    drawLabels(app)
    drawBackToHomeButton(app)

def drawLabels(app):
    drawLabel('How to Play Sudoku', app.width/2, 110, size=60, 
              fill=app.accentColor, align='center', font='Brush Script MT')
    drawLabel('Fill in a 9x9 board with numbers from 1-9', 100, 175, size=24, 
              fill=app.accentColor, font='Canela Text', align='left')
    drawLabel('  - No repeated numbers in each line vertically or horizontally',
              100, 200, size=18, fill=app.accentColor, font='Canela Text',
              align='left')
    drawLabel('  - No repeated numbers in each 3x3 square', 100, 225, size=18, 
              fill=app.accentColor, font='Canela Text', align='left')
    drawLabel('  - Each number must appear only 9 times on the board', 100, 250,
              size=18, fill=app.accentColor, font='Canela Text', align='left')
    
    drawLabel('Game Controls and Features', app.width/2, 285, size=60, 
              fill=app.accentColor, align='center', font='Brush Script MT')
    drawLabel('- Click any empty cell to select it, then select a number with' +
              ' either the number pad or the keyboard', 100, 350, size=16, 
              fill=app.accentColor, font='Canela Text', align='left')
    drawLabel('- Fill in cells until the board is completely solved', 100, 375, 
              size=16, fill=app.accentColor, font='Canela Text', align='left')
    # heavily inspired by nyt sudoku instructions
    drawLabel('- Normal Mode: add one number to a cell', 100, 415, size=16, 
              fill=app.accentColor, font='Canela Text', align='left')
    drawLabel('- Candidate Mode: add multiple options to a cell', 100, 440, 
              size=16, fill=app.accentColor, font='Canela Text', align='left')
    drawLabel('- Choose to automatically display all candidates with ' + 
              'auto-candidate mode', 100, 465, size=16, fill=app.accentColor, 
              font='Canela Text', align='left')
    drawLabel('- Choose to show if the cell value is incorrect with autocorrect'
              , 100, 490, size=16, fill=app.accentColor, font='Canela Text', 
              align='left')
    drawLabel('- Need a hint? Click to ask for a cell to be highlighted and ' +
              'press again to apply the hint', 100, 515, size=16, 
              fill=app.accentColor, font='Canela Text', align='left')

def drawBackToHomeButton(app):
    drawRect(75, 75, 100, 35, fill=app.buttonColor, border=app.accentColor)
    drawLabel('Back to Game', 125, 93, align='center', font='Canela Text',
              fill=app.accentColor)

def help_onMousePress(app, mouseX, mouseY):
    if 175 >= mouseX >= 75 and 110 >= mouseY >= 75:
        setActiveScreen('play')