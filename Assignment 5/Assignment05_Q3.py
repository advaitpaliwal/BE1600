from cImage import *


def editImg(pic, scale):
    oldImage = FileImage(pic)
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()
    window = ImageWin("Scale Image", oldW * scale, oldH)
    stretchIm = EmptyImage(oldW * scale, oldH)
    for y in range(oldH):
        for x in range(oldW * scale):
            pixel = oldImage.getPixel((x // 2), y)
            stretchIm.setPixel(x, y, pixel)
    stretchIm.draw(window)
    window.exitOnClick()


editImg("butterfly.gif", 2)
