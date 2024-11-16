from cmu_graphics import *

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.squareLength = 200
    app.url = 'resizedClearSnail.png'
    app.userBoardLeft = 450
    app.userBoardTop = app.height *0.3

    app.secretColor = rgb(72, 201, 82)
    app.userRows = 10
    app.userCols = 16
    app.userSquare = 25
    # app.fill = 'white'
    app.coloring = False
    app.board = [(['white'] * app.userCols) for row in range(app.userRows)]
    app.fillColor = 'No Color'

def redrawAll(app):
    drawBackground(app)
    drawUserBoard(app)
    drawSelectionLabels(app)


def getScore(app):

    if app.done:
        secret = [72, 201, 82]
        redList = []
        blueList = []
        greenList = []
        for row in range(app.userRows):
            for col in range(app.userCols):
                red, blue, green = getRGB(app.board[row][col])
                redList.append(red)
                blueList.append(blue)
                greenList.append(green)
    score = 1- ((abs(getAverage(redList)-secret[0]), \
        abs(getAverage(blueList)-secret[1]), \
        abs(getAverage(greenList) - secret[2]))) * 100
    return score

def getRBG(str):
    d = {'lightGreen': [144, 238, 144], 'oliveDrab': [107, 142, 35],\
         'darkGreen': [0, 100, 0], 'seaGreen': [46, 139, 87]}
    return d[str]


def getAverage(L):
    total = 0
    for val in L:
        total += val
    return total/len(L)
def drawSelectionLabels(app):
    if app.fillColor == 'No Color':
            drawLabel(f'No color is currently selected', 920, 650, \
              font = 'monospace', bold = True, size = 20)

    else:
        drawLabel(f'{app.fillColor} is currently selected', 920, 650, \
              font = 'monospace', bold = True, size = 20)


def drawUserBoard(app):
    for row in range(app.userRows):
        for col in range(app.userCols):
            drawCell(app, row, col, app.board[row][col])

def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def onMousePress(app, mouseX, mouseY):
    if inColorPalette(app, mouseX, mouseY):
        app.fillColor = getColorFromPalette(app, mouseX, mouseY)

    
def onMouseDrag(app, mouseX, mouseY):
    # print(mouseX,mouseY)
    if onBoard(app, mouseX, mouseY):
        row = int((mouseX - app.userBoardLeft) // app.userSquare)
        col = int((mouseY - app.userBoardTop) // app.userSquare)
        if 0 <= row < app.userRows and 0 <= col < app.userCols \
            and app.fillColor != 'No Color':
            app.board[row][col] = app.fillColor #from chatgpt
        # getCell(app, mouseX, mouseY)
        
        

def onBoard(app, mouseX, mouseY):
    if 450 > mouseX or 700 < mouseX or app.height*0.3 > mouseY \
    or 640 < mouseY:
        return False
    return True



def inColorPalette(app, mouseX, mouseY):
    if 720 > mouseX or 1120 < mouseX or 240 > mouseY or \
    640 < mouseY: return False
    return True

def getColorFromPalette(app, mouseX, mouseY):
    if mouseX > 720 and mouseX < 920 and mouseY > 240 and mouseY < 440: 
        return 'seaGreen'
    if mouseX > 920 and mouseX < 1120 and mouseY > 240 and mouseY < 440:
        return 'oliveDrab'
    if mouseX > 920 and mouseX < 1120 and mouseY >= 440 and mouseY < 640:
        return 'darkGreen'
    if mouseX > 720 and mouseX < 1120 and mouseY >= 440 and mouseY < 640:
        return 'lightGreen'

def drawCell(app, row, col, fill):
    drawRect(app.userBoardLeft+(app.userSquare*row), app.userBoardTop+(app.userSquare*col), \
             app.userSquare, app.userSquare, fill = fill, border = 'black')

def drawBackground(app):
    #Fr Background + Text Instructions
    drawRect(0,0, app.width, app.height, fill = rgb(254,213,255))
    drawLabel("We can't always use the magical bubble of protection...", \
              app.width * 0.5, app.height * 0.1, size = 35, font = 'monospace',\
                bold = True, align = 'center')
    drawLabel("Try to match the snail's shell to the color of  ", \
              app.width * 0.5, app.height * 0.15, size = 35, font = 'monospace',\
                bold = True, align = 'center')
    drawLabel("their environment by coloring in their shell!", \
              app.width * 0.5, app.height * 0.2, size = 35, font = 'monospace',\
                bold = True, align = 'center')
    
    #Snail Image!
    drawRect(200,400,250,250, align = 'center', fill = app.secretColor)
    drawCircle(200,400,100, fill = gradient(rgb(0,0,100), 'white'))
    drawImage(app.url, 200, app.height/2, align = 'center')

    #Color Palette
    drawLabel("Nature's finest color palette", app.width*0.77, app.height * 0.27, \
               size = 20, font = 'monospace', bold = True)
    drawRect(app.width*0.6, app.height *0.3,app.squareLength, \
             app.squareLength, fill = rgb(46, 139, 87), border = 'black')  # seaGreen
    drawRect(app.width*0.6,app.height * 0.55,app.squareLength, \
             app.squareLength, fill = rgb(144, 238, 144), border = 'black') # lightGreen
    drawRect(app.width*0.6+app.squareLength,app.height * 0.3,app.squareLength, \
             app.squareLength, fill = rgb(107, 142, 35), border = 'black') #oliveDrab
    drawRect(app.width*0.6+app.squareLength,app.height * 0.55,app.squareLength, \
             app.squareLength, fill = rgb(0, 100, 0), border = 'black') # darkGreen
    
    
def main():
    runApp()

main()