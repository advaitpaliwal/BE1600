from cImage import *


def redPixel(oldpixel):
    newRed = oldpixel.getRed() + 65
    if newRed > 255:
        newRed = 255
    newPixel = Pixel(newRed, oldpixel.getGreen(), oldpixel.getBlue())
    return newPixel


def makeRed(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Black and White", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = redPixel(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


makeRed("butterfly.gif")
