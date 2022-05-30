from cmu_graphics import *

toreList = ['images/tore1.png', 'images/tore2.png']
felixList = []
textBox = Group(Rect(0, 300, 300, 100, ), Polygon(300, 300, 400, 300, 300, 400), Polygon(0, 300, 400, 300, 375, 325, 0, 325, fill='darkBlue'), Image(choice(toreList), 0, 400-78))


cmu_graphics.run()