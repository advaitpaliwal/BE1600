from cImage import *


def smoothen(oldImage, col, row):
    try:
        red = (oldImage.getPixel(col,
                                 row).getRed() + oldImage.getPixel(col + 1,
                                                                   row).getRed() + oldImage.getPixel(col - 1,
                                                                                                     row).getRed() + oldImage.getPixel(col,
                                                                                                                                       row + 1).getRed() + oldImage.getPixel(col,
                                                                                                                                                                             row - 1).getRed()) // 5
        green = (oldImage.getPixel(col,
                                   row).getGreen() + oldImage.getPixel(col + 1,
                                                                       row).getGreen() + oldImage.getPixel(col - 1,
                                                                                                           row).getGreen() + oldImage.getPixel(col,
                                                                                                                                               row + 1).getGreen() + oldImage.getPixel(col,
                                                                                                                                                                                       row - 1).getGreen()) // 5
        blue = (oldImage.getPixel(col,
                                  row).getBlue() + oldImage.getPixel(col + 1,
                                                                     row).getBlue() + oldImage.getPixel(col - 1,
                                                                                                        row).getBlue() + oldImage.getPixel(col,
                                                                                                                                           row + 1).getBlue() + oldImage.getPixel(col,
                                                                                                                                                                                  row - 1).getBlue()) // 5
        return Pixel(red, green, blue)
    except BaseException:
        return oldImage.getPixel(col, row)


def makeSmooth(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Stretch", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width * 2, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newIm.setPixel(col, row, oldPixel)
            try:
                newIm.setPixel(width + col, row, smoothen(oldImage, col, row))
            except BaseException:
                newIm.setPixel(width + col, row, oldImage.getPixel(col, row))

    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


makeSmooth("pic.gif")
