from cmu_graphics import *
#img = 'images/tore1.png'
#image = Image(img, 0, 0)
app.gravity = 0.6

void = Rect(-10*10**9, 360, 10*10**18, 440, fill='black')
player = Group(Rect(150, 320, 30, 40, fill='red'))
player.horizontalSpeed = 10
player.jumpHeight = 10
player.jumps = 1
player.dy = 0

app.stepsPerSecond = 120

map = Group()
floor = Rect(-100, 360, 4800, 40, fill=gradient('saddleBrown',  'lime', start='bottom'))
#sign = Polygon(-100,360,)
platforms = Group()
map.add(floor, platforms)

spikes = Group()

hurtfulObjects = Group(spikes)

map.add(spikes)

def createLevelOne():
    for n in range(0,30):
        if n%2 == 0:
            y = randrange(250, 300)
        else:
            y = randrange(150, 200)
        platforms.add(Rect(250+n*150, y, 100, 20, fill='grey'))
    
    for n in range(0, 10+1):
        spike = Group()
        x = 300 +400*n
        spike.add(Polygon(x, 360, x+15, 330, x+30, 360, x+45, 330, x+60, 360, x+75, 330, x+90, 360, fill=gradient('red', 'darkRed', 'black', start='top')))
        spikes.add(spike)

def playerOnPlatform():
    if player.hitsShape(floor):
        return True
    else:
        for platform in platforms:
            if player.hitsShape(platform) and player.bottom < platform.bottom:
                return True
    return False

def onPlatformCheck():
    for platform in platforms:
        if player.hitsShape(platform) and player.bottom < platform.bottom:
            player.bottom = platform.top
            player.dy = 0
            player.jumps = 1
        elif player.hitsShape(platform) and player.top > platform.top:
            player.top = platform.bottom
            player.dy = 0
        elif player.hitsShape(platform) and player.right < platform.centerX:
            player.right = platform.left
        elif player.hitsShape(platform) and player.left > platform.centerX:
            player.left = platform.right

def gameOverCheck():
    for spike in spikes:
        if player.hitsShape(spike):
            return True
    if player.bottom > 400:
        return True
    return False
        

createLevelOne()
        

def onKeyHold(keys):
    if ('d' in keys) or ('D' in keys) or ('right' in keys):
        map.centerX -= player.horizontalSpeed
    if ('a' in keys) or ('A' in keys) or ('left' in keys):
        map.centerX += player.horizontalSpeed

def onKeyPress(key):
    if 'space' == key and player.jumps > 0:
        player.dy -= player.jumpHeight
        player.jumps -= 1

def onStep():
    player.centerY += player.dy
    
    if player.hitsShape(floor):
        player.dy = 0
        player.bottom = floor.top
        player.jumps = 1
    
    onPlatformCheck()
    
    if playerOnPlatform() == False:
        player.dy += app.gravity
        player.jumps = 0    
    
    if gameOverCheck() == True:
        x = player.centerX
        y = player.centerY
        player.clear()
        for n in range(6):
            for i in range(8):
                player.add(Rect(x-15+n, y-20+i, 5, 5, fill='red'))
        for i in range(25):
            for n in player:
                n.centerX += randrange(-10, 10)
                n.centerY += randrange(-10, 10)
        Label('GAME OVER', 200, 200, fill='red', size=60)
        app.stop()



cmu_graphics.run()