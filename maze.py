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

def redrawAll(app):
    #green background
    drawBackground(app)
    #draws the grid for the maze
    drawBoard(app)
    drawBoardBorder(app)

def main():
    runApp()

main()