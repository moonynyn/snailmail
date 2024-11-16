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
    app.mixColor = 'white'
    app.submitColor = 'lightGreen'
    app.submitted = False
    app.score = 0

def redrawAll(app):
    drawBackground(app)
    drawUserBoard(app)
    drawSelectionLabels(app) #screen before game starts
    drawSubmitButton(app)
    drawColorMixerDis(app)
    if app.submitted:
        drawSuccess(app)

def drawSuccess(app):
    drawRect(0,0,app.width, app.height, fill = rgb(254,213,255))
    drawRect(app.width*0.5-300, app.height*0.5 - 150, 300, 300, fill = app.mixColor)
    drawRect(app.width*0.5, app.height*0.5 - 150, 300, 300, \
             fill = app.secretColor)
    drawLabel(f'You scored {app.score}%!', app.width*0.5, app.height*0.5 + 200, \
              size = 40, font = 'monospace', bold = True)

def drawColorMixerDis(app):
        
    drawRect(365, app.height *0.3, 50, 400, fill = app.mixColor)

def drawSubmitButton(app):
    drawRect(75, app.height*0.65, 250, 120, fill = app.submitColor, border = 'green',\
             borderWidth = 5)
    drawLabel('submit', 75+125, app.height*0.65 + 60, size = 55, font = 'monospace',\
              align = 'center', bold = True)



def getScore(app):
    secret = [72, 201, 82]
    red = getAverageColor(app)[0] 
    blue = getAverageColor(app)[1]
    green = getAverageColor(app)[2]
    print(red,blue,green)
    print(secret[0], secret[1], secret[2])
    # print(type(red), type(secret[0]))
    
    app.score = (1 - (threeDist(red, blue, green, secret[0], secret[1],secret[2]) / 255)) * 100
    return int(app.score)
    
#d = √((x2 - x1)² + (y2 - y1)² + (z2 - z1)²
def threeDist(x1, y1, z1, x2, y2,z2):
    return ((x2-x1)**2 + (y2-y1)**2+(z2-z1)**2)**0.5
def getRGB(str):
    d = {'red': [255, 0, 0], 'blue': [0, 0, 255],\
         'yellow': [255, 255, 0], 'white': [255,255,255]}
    return d[str]


def getAverage(L):
    total = 0
    for val in L:
        total += val
    return total//len(L)

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
    if inSubmitBox(app, mouseX, mouseY):
        app.submitColor = rgb(252, 98, 170)
        app.submitted = True
        app.done = True
        app.score = getScore(app)
        
def inSubmitBox(app,mouseX, mouseY):
    if mouseX < 75 or mouseX > 250+75 or mouseY < app.height*0.65 or \
    mouseY > app.height*0.65 + 120:
        return False
    return True

def getAverageColor(app):
    redList = []
    blueList = []
    greenList = []
    for row in range(app.userRows):
        for col in range(app.userCols):
            red, blue, green = getRGB(app.board[row][col])
            redList.append(red)
            blueList.append(blue)
            greenList.append(green)
    return [getAverage(redList), getAverage(blueList), getAverage(greenList)]
    
def onMouseDrag(app, mouseX, mouseY):
    app.mixColor = rgb(getAverageColor(app)[0], getAverageColor(app)[1], getAverageColor(app)[2])
    # print(app.mixColor, getAverageColor(app)[0], getAverageColor(app)[1], getAverageColor(app)[2])
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
        return 'red'
    if mouseX > 920 and mouseX < 1120 and mouseY > 240 and mouseY < 440:
        return 'blue'
    if mouseX > 920 and mouseX < 1120 and mouseY >= 440 and mouseY < 640:
        return 'white'
    if mouseX > 720 and mouseX < 1120 and mouseY >= 440 and mouseY < 640:
        return 'yellow'

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
    drawRect(200,app.height *0.3+125,250,250, align = 'center', fill = app.secretColor)
    drawCircle(200,app.height *0.3+125,100, fill = gradient(rgb(0,0,100), 'white'))
    drawImage(app.url, 200, app.height *0.3+125, align = 'center')

    #Color Palette
    drawLabel("Nature's finest color palette", app.width*0.77, app.height * 0.27, \
               size = 20, font = 'monospace', bold = True)
    drawRect(app.width*0.6, app.height *0.3,app.squareLength, \
             app.squareLength, fill = rgb(255, 0, 0), border = 'black')  # red
    drawRect(app.width*0.6,app.height * 0.55,app.squareLength, \
             app.squareLength, fill = rgb(255, 255, 0), border = 'black') # yellow
    drawRect(app.width*0.6+app.squareLength,app.height * 0.3,app.squareLength, \
             app.squareLength, fill = rgb(0, 0, 255), border = 'black') #blue
    drawRect(app.width*0.6+app.squareLength,app.height * 0.55,app.squareLength, \
             app.squareLength, fill = rgb(255, 255, 255), border = 'black') # white
    
    
def main():
    runApp()

main()