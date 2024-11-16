from cmu_graphics import *

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.boardLeft = 80
    app.boardTop = 80
    app.boardWidth = 1040
    app.boardHeight = 640
    app.blocksWidth = 40
    app.blocksHeight = 40
    app.rows = int((app.height -160)/app.blocksHeight)
    app.cols = int((app.width - 160)/app.blocksWidth)
    app.cellBorderWidth = 2
    app.board = [([None] * app.cols) for row in range(app.rows)]
    app.url = 'resizedClearSnail.png'
    app.snailLocation = [60, 180]

def loadMazeBarriers(app):
    for col in range(4):
        app.board[1][col] = 'darkGreen'
        app.board[13][col] = 'darkGreen'
    for row in range(3, 12):
        app.board[row][1] = 'darkGreen'
    app.board[11][0] = 'darkGreen'
    app.board[12][6] = 'darkGreen'
    for row in range(1, 7):
        app.board[row][3] = 'darkGreen'
    for row in range(9, 14):
        app.board[row][3] = 'darkGreen'
    for col in range(2, 6):
        app.board[8][col] = 'darkGreen'
    for row in range(9, 13):
        app.board[row][5] = 'darkGreen'
    for row in range(5):
        app.board[row][5] = 'darkGreen'
    for col in range(4, 8):
        app.board[6][col] = 'darkGreen'
    for row in range(8, 13):
        app.board[row][7] = 'darkGreen'
    for row in range(1, 6):
        app.board[row][7] = 'darkGreen'
    for col in range(8, 13):
        app.board[1][col] = 'darkGreen'
    for row in range(1, 4):
        app.board[row][9] = 'darkGreen'
        app.board[row][14] = 'darkGreen'
        app.board[row][11] = 'darkGreen'
    for col in range(12, 14):
        app.board[3][col] = 'darkGreen'
    for row in range(3, 11):
        app.board[row][13] = 'darkGreen'
    app.board[8][8] = 'darkGreen'
    for row in range(5, 9):
        app.board[row][9] = 'darkGreen'
    for row in range(5, 11):
        app.board[row][11] = 'darkGreen'
    for col in range(9, 12):
        app.board[10][col] = 'darkGreen'
    for row in range(10, 14):
        app.board[row][9] = 'darkGreen'
    for col in range(10, 13):
        app.board[12][col] = 'darkGreen'
    for row in range(12, 14):
        app.board[row][12] = 'darkGreen'
        app.board[row][14] = 'darkGreen'
    for row in range(7, 13):
        app.board[row][15] = 'darkGreen'
    for row in range(6):
        app.board[row][16] = 'darkGreen'
    for col in range(15, 19):
        app.board[5][col] = 'darkGreen'
    for col in range(15, 18):
        app.board[7][col] = 'darkGreen'
    for row in range(8, 13):
        app.board[row][17] = 'darkGreen'
    app.board[5][10] = 'darkGreen'    
    app.board[0][18] = 'darkGreen'
    for col in range(18, 26):
        app.board[1][col] = 'darkGreen'
    for row in range(3, 5):
        app.board[row][18] = 'darkGreen'
    for col in range(19, 23):
        app.board[3][col] = 'darkGreen'
    for col in range(18, 22):
        app.board[11][col] = 'darkGreen'
    app.board[12][17] = None
    for row in range(7, 10):
        app.board[row][19] = 'darkGreen'
    for row in range(5, 8):
        app.board[row][20] = 'darkGreen'
    for col in range(21, 25):
        app.board[7][col] = 'darkGreen'
    for row in range(3, 6):
        app.board[row][22] = 'darkGreen'
    for row in range(3, 8):
        app.board[row][24] = 'darkGreen'
    app.board[3][25] = 'darkGreen'
    for col in range(21, 24):
        app.board[9][col] = 'darkGreen'
    for row in range(9, 14):
        app.board[row][23] = 'darkGreen'
        app.board[row][25] = 'darkGreen'
    for col in range(17, 26):
        app.board[13][col] = 'darkGreen'
    for col in range(26):
        app.board[15][col] = 'darkGreen'
    # drawRect()

def drawBackground(app):
    loadMazeBarriers(app)
    drawRect(0, 0, app.width, app.height, fill = 'forestGreen')

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col, app.board[row][col])

def drawBoardBorder(app):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight, borderWidth = 2 * app.cellBorderWidth, fill = None, border = 'darkGreen')

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight, borderWidth=app.cellBorderWidth, fill = color, border = 'darkGreen')

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def onKeyPress(app, key):
    if key == 'up':
        if isLegal(app, 0, -40):
            app.snailLocation[1] -= 40
    if key == 'down':
        if isLegal(app, 0, 40):
            app.snailLocation[1] += 40
    if key == 'right':
        if isLegal(app, 40, 0):
            app.snailLocation[0] += 40
    if key == 'left':
        if isLegal(app, 0, -40):
            app.snailLocation[0] -= 40

def isLegal(app, xDirection, yDirection):
    x, y = app.snailLocation
    print(x, y, xDirection, yDirection)
    x += xDirection
    y += yDirection
    # print(x, y)
    if x < 60 or x >= 1120 or y < 80 or y >= 720:
        return False
    else:
        return True
    blockX = (x - 60)//app.blocksWidth
    blockY = (y - 60)//app.blocksHeight
    if blockX < 0 or blockX >= len(app.board[0]) or blockY < 0 or blockY >= len(app.board):
        return False
    if app.board[blockX][blockY] != None:
        return False
    return True

def redrawAll(app):
    #green background
    drawBackground(app)
    #draws the grid for the maze
    drawBoard(app)
    drawBoardBorder(app)
    #SNAIL!!!!
    imageWidth, imageHeight = getImageSize(app.url)
    x, y = app.snailLocation
    drawImage(app.url, x, y, width = imageWidth//3, height = imageHeight//3, align = 'center')

def main():
    runApp()

main()