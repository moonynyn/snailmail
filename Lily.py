from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 500
    app.startWidth = 400
    app.startHeight = 400

#change the really ugly font
def redrawAll(app):
    drawRect(200, 50, app.startWidth, app.startHeight, fill = 'lightGreen')
    drawLabel('Replace with game name', app.width/2, 80, size = 30)
    drawRect(360, 320, 80, 25, fill = 'lightPink')
    drawLabel('Instructions!', app.width/2, 330)
    drawRect(375, 350, 50, 25, fill = 'lightPink')
    drawLabel('Start!', app.width/2, 360)


def main():
    runApp(width = app.width, height = app.height)

main()