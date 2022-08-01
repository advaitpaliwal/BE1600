from cImage import *
import math
myImWin = ImageWin("Line Image", 500, 500)
lineImage = EmptyImage(500, 500)
bluePixel = Pixel(0, 0, 255)
for i in range(1000):
    x = int(200 * math.sin(i)) + 250
    y = int(200 * math.cos(i)) + 250
    lineImage.setPixel(x, y, bluePixel)
lineImage.draw(myImWin)
lineImage.save("lineImage.gif")
myImWin.exitOnClick()
