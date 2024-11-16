from cmu_graphics import *

def onAppStart(app):
    app.width = 600
    app.height = 600
    app.blocksWide = 30
    app.blocksTall = 30

def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill = 'forestGreen')

def redrawAll(app):
    drawBackground(app)
    #draws the grid for the maze
    numBlocksTall = app.height/app.blocksTall
    numBlocksWide = app.width/app.blocksWide
    for x in range(int(numBlocksWide)):
        x *= app.blocksWide
        drawLine(x, 0, x, app.height, fill = 'darkGreen')
    for y in range(int(numBlocksTall)):
        y *= app.blocksTall
        drawLine(0, y, app.width, y, fill = 'darkGreen')


def main():
    runApp()

main()