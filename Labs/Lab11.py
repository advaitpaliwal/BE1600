from cImage import *

myImWin = ImageWin("Line Image", 500, 500)
lineImage = EmptyImage(500, 500)
bluePixel = Pixel(0, 0, 255)
redPixel = Pixel(255, 0, 0)
for i in range(500):
    lineImage.setPixel(i, i, bluePixel)
for j, l in zip(range(499, 0, -1), range(0, 500)):
    lineImage.setPixel(j, l, bluePixel)
for k in range(250, 500):
    lineImage.setPixel(250, k, redPixel)
lineImage.draw(myImWin)
lineImage.save("lineImage.gif")
myImWin.exitOnClick()
