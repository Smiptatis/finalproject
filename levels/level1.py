#from platform import platform
from cmu_graphics import *

def createSpike(x, y, angle, points):
    spike = Polygon(fill=gradient('red', 'darkRed', 'black', start='top'))
    for n in range(points):
        spike.addPoint(x+30*n, y)
        spike.addPoint(x+15+30*n, y-30)
        spike.addPoint(x+30+30*n, y)
    spike.rotateAngle = angle
    return spike

def createGobbler(x, y):
    gobbler = Image('images/gobb.png', x, y, align='bottom')
    return gobbler

def createLevelOne(platforms, spikes, goal, walls, gobblers):
    #PLATFORM 1 250 PLATFORM LAST 4450 highest y platform from ground == 255
    platforms.add(
    Rect(-200, 255, 300, 20, fill='grey'), 
    Rect(-600, 160, 150, 20, fill='grey'),
    Rect(500, 180, 300, 20, fill='grey'),
    Rect(500, 270, 100, 20, fill='grey'),
    Rect(700, 270, 100, 20, fill='grey'),
    Rect(600, 290, 100, 70, fill='grey'),
    Rect(1000, 200, 400, 20, fill='grey'),
    Rect(1600, 150, 40, 20, fill='grey'),
    Rect(1800, 100, 40, 20, fill='grey'),
    Rect(2200, 50, 40, 20, fill='grey'),
    )
    

    platforms.add(
    Rect(250, 350, 100, 20, fill='grey'), Rect(270, 340, 100, 20, fill='grey'), Rect(290, 330, 100, 20, fill='grey'), Rect(310, 320, 100, 20, fill='grey'), Rect(330, 310, 100, 20, fill='grey'),
    Rect(350, 300, 100, 20, fill='grey'), Rect(370, 290, 100, 20, fill='grey'), Rect(390, 280, 100, 20, fill='grey'), Rect(410, 270, 100, 20, fill='grey'), Polygon(15+255, 370, 235+255, 280, 345+255, 290, 345+255, 370, fill='grey'), Polygon(600, 370, 700, 360, 600, 360, fill='grey'),
    Rect(2800, 150, 150, 20, fill='grey'), Rect(3100, 255, 100, 20, fill='grey'), Rect(3600, 255, 100, 20, fill='grey'), Rect(3800, 200, 100, 20, fill='grey'), Rect(4200, 130, 200, 20, fill='grey'), Rect(4600, 100, 400, 20, fill='grey')
    )
    
    spikes.add(createSpike(800, 360, 0, 12))
    spikes.add(createSpike(-95, 255, 0, 3))
    spikes.add(createSpike(605, 290, 0, 3,))
    spikes.add(createSpike(705, 310, 180, 3, ))
    spikes.add(createSpike(505, 180, 0, 3, ))
    spikes.add(createSpike(710, 180, 0, 3, ))
    
    spikes.add(createSpike(800, 360, 0, 12+3*15, ))

    gobblers.add(createGobbler(2710, 360), createGobbler(3200, 360), createGobbler(3400, 360), createGobbler(3800, 360), createGobbler(3650, 255), createGobbler(4000, 360), createGobbler(-525, 160))
    spikes.add(createSpike(2710+200, 360, 0, 4))
    goal.centerX -= 100


#createLevelOne()