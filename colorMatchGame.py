from cmu_graphics import *

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.url = 'the clear snail.png'
    width, height = getImageSize(app.url)
    print(width, height)


def redrawAll(app):
    drawImage(app.url, 50, 100)
    
def main():
    runApp()

main()