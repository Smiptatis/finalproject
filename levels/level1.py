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
    Image('images/platform3.png', -200, 255), 
    Image('images/platform2.png', -600, 160),
    Image('images/platform3.png', 500, 180),
    Image('images/platform.png', 500, 270),
    Image('images/platform.png', 700, 270),
    Image('images/platform.png', 600, 290),
    Image('images/platform4.png', 1000, 200),
    Image('images/platform5.png', 1600, 150),
    Image('images/platform5.png', 1800, 100),
    Image('images/platform5.png', 2200, 50),
    )
    

    platforms.add(
    Image('images/platform.png', 250, 350), Image('images/platform.png', 270, 340), Image('images/platform.png', 290, 330), Image('images/platform.png', 310, 320), Image('images/platform.png', 330, 310),
    Image('images/platform.png', 350, 300), Image('images/platform.png', 370, 290), Image('images/platform.png', 390, 280), Image('images/platform.png', 410, 270),
    Image('images/platform2.png', 2800, 150), Image('images/platform.png', 3100, 255), Image('images/platform.png', 3600, 255), Image('images/platform.png', 3800, 200), Image('images/platform2.png', 4200, 130), Image('images/platform4.png', 4600, 100)
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
    goal.centerX = 4650


#createLevelOne()