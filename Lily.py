from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 500
    app.startWidth = 400
    app.startHeight = 400
    app.instructionsTop = 360
    app.instructionsLeft = 320
    app.instructionsWidth = 80
    app.instructionsHeight = 25

#change the really ugly font
def redrawAll(app):
    drawRect(200, 50, app.startWidth, app.startHeight, fill = 'lightGreen')
    drawLabel('Replace with game name', app.width/2, 80, size = 30)
    drawRect(app.instructionsTop, app.instructionsLeft, app.instructionsWidth, app.instructionsHeight, fill = 'lightPink')
    drawLabel('Instructions!', app.width/2, 330)
    drawRect(375, 350, 50, 25, fill = 'lightPink')
    drawLabel('Start!', app.width/2, 360)

#if instructions button is pressed
def onMousePress(app, mouseX, mouseY):
    if intersection(app, mouseX, mouseY):
        drawRect()
        
def intersection(app, mouseX, mouseY):
    if (mouseX >= app.instructionsLeft and mouseX <= app.instructionsLeft + app.instructionsWidth) and (mouseY <= app.instructionsTop and mouseY >= app.instructionsHeight + app.instructionsTop):
        print('hi')

def main():
    runApp(width = app.width, height = app.height)

main()