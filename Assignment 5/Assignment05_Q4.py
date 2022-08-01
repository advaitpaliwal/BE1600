from cImage import *


def blackPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitySum // 3
    if aveRGB > 130:
        newPixel = Pixel(255, 255, 255)
    else:
        newPixel = Pixel(0, 0, 0)
    return newPixel


def makeBlack(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Black and White", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = blackPixel(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


makeBlack("butterfly.gif")
