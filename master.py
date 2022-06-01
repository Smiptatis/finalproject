from cmu_graphics import *
from levels.level1 import createLevelOne
#img = 'images/tore1.png'
#image = Image(img, 0, 0)
app.gravity = 0.6
app.friction = 1
app.mouseX = 0
app.mouseY = 0
app.started = False


void = Rect(-10*10**4, 360, 10*10**9, 440, fill='black')
player = Group(Rect(150, 320, 30, 40, fill='red'))
player.horizontalSpeed = 2
player.maxHorizontal = 16
player.dx = 0
player.jumpHeight = 10
player.jumpHeight2 = 5
player.jumps = 2
player.dy = 0
player.dashLength = 30
player.dash = 1

app.stepsPerSecond = 20

map = Group()
floor = Rect(-100, 360, 4800, 40, fill=gradient('saddleBrown',  'lime', start='bottom'))
#sign = Polygon(-100,360,)
platforms = Group()
walls = Group()
map.add(floor, platforms, walls)
secret = Rect(-700, 100, 40, 40, fill='pink')
goal = Group(Rect(4750, 350, 50, 10, fill='lightGrey'), Polygon(4750, 350, 4770, 320, 4780, 320, 4800, 350, fill=gradient('blue', 'lightBlue', 'lightblue', start='bottom')),)
goal.star = Star(4775, 320, 20, 5, fill='yellow')
goal.add(goal.star)
gobblers = Group()
gobblers.speed = 5
map.add(secret, goal, gobblers)
gameOverLabel = Label('GAME OVER', 200, 200, fill='red', size=60, visible=False)

spikes = Group()

hurtfulObjects = Group(spikes)

map.add(spikes)

app.rickastleyurl = 'https://media.discordapp.net/attachments/750800636928458843/948274243785875529/Lukasgif.gif'

    
#execfile('levels/level1.py')
createLevelOne(platforms, spikes, goal, walls, gobblers)
app.resetLeft = map.left

background = Image('images/gamebackground.png', map.left-2000, 0)
map.add(background)

background.toBack()
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
            player.jumps = 2
            player.dash = 1
        elif player.hitsShape(platform) and player.top > platform.top:
            player.top = platform.bottom
            player.dy = 0
        elif player.hitsShape(platform) and player.right < platform.centerX:
            player.right = platform.left
            player.dx = 0
        elif player.hitsShape(platform) and player.left > platform.centerX:
            player.left = platform.right
            player.dx = 0

def gobblerCheck():
    for gobbler in gobblers:
        if player.hitsShape(gobbler) and player.bottom < gobbler.top +20:
            player.dy = -10
            
                

def onWallCheck():
    for wall in walls:
        if player.hitsShape(wall):
            if player.right > wall.left:
                player.right = wall.left
                player.dx = 0
                player.jumps = 1
            elif player.left < wall.right:
                player.left = wall.right
                player.dx = 0
                player.jumps = 1
                

def gameOverCheck():
    for spike in spikes:
        if player.hitsShape(spike):
            return True
    for gobbler in gobblers:
        if player.hitsShape(gobbler) and player.bottom > gobbler.top +20:
            return True
    if player.bottom > 400:
        return True
    return False

def win():
    Label('Wow you did it!!!', 200, 200, fill='Pink', size=40)
    app.stop()

def leftPlatformCheck():
    for platform in platforms:
        if player.hitsShape(platform) and player.right < platform.centerX and player.bottom > platform.centerY and player.top < platform.centerY:
            return True
    return False
def rightPlatformCheck():
    for platform in platforms:
        if player.hitsShape(platform) and player.left > platform.centerX and player.bottom > platform.centerY and player.top < platform.centerY:
            return True
    return False

def leftWallCheck():
    for wall in walls:
        if player.hitsShape(wall) and player.right > wall.left:
            return True
    return False
def rightWallCheck():
    for wall in walls:
        if player.hitsShape(wall) and player.left < wall.right:
            return True
    return False


def onKeyHold(keys):
    if app.started == True:
        if (('d' in keys) or ('D' in keys) or ('right' in keys)) and (('a' in keys) or ('A' in keys) or ('left' in keys)):
            player.dx += 0
        elif ('d' in keys) or ('D' in keys) or ('right' in keys):
            if leftPlatformCheck() == False and leftWallCheck() == False:
                if player.dx > -player.maxHorizontal:
                    player.dx -= player.horizontalSpeed
                elif player.dx < -player.maxHorizontal:
                    player.dx = -player.maxHorizontal
            else:
                player.dx = 0
                
        elif ('a' in keys) or ('A' in keys) or ('left' in keys):
            if rightPlatformCheck() == False and rightWallCheck() == False:
                if player.dx < player.maxHorizontal:
                    player.dx += player.horizontalSpeed
                elif player.dx > player.maxHorizontal:
                    player.dx = player.maxHorizontal
            else:
                player.dx = 0


toreList = ['images/tore1.png', 'images/tore2.png', 'images/fruitytore.png']
felixList = ['images/Felle1.png', 'images/Felle2.png', 'images/Felle3.png']

#textBox = Group(Rect(0, 300, 322, 100, ), Polygon(322, 300, 322, 400, 400, 400), Polygon(0, 300, 400, 300, 375, 325, 0, 325, fill='darkBlue'), Image(choice(toreList), 0, 400-222), Polygon(0, 300, 78, 300, 0, 400, fill='white'))
menu = Group(Image('images/background.png', 0, 0), Label('Socky Adventure', 200, 50, size=40, font='cinzel', fill=gradient('white', 'white', 'red', 'blue', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'red', 'red', 'red',  start='left')), Label('Against Bonke', 200, 90, size=40, font='cinzel', fill=gradient('white', 'white', 'red', 'blue', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'red', 'red', 'red',  start='left')))
textBox = Group(Polygon(0, 400, 78, 300, 322, 300, 400, 400), Polygon(78, 300, 322, 300, 337.5, 320, 62.5, 320, fill='darkBlue'), Label('Tore and Felix', 200, 310, size=20, fill='white'), Image(choice(toreList), 0, 400-120), Image(choice(felixList), 322, 400-120))
textBox.text1 = Group(Label('Welcome to (LOOK UP!!!)', 200, 330, fill='white'), Label('wasd or arrow keys to move', 200, 340, fill='white'), Label('space to jump and double jump', 200, 350, fill='white'), Label('q to dash towards the mouse.', 200, 360, fill='white'), Label('try not to die will you?', 200, 370, fill='white'), Label('Press the red scary button to start!!!!', 200, 380, fill='white'))

startButton = Group(Circle(200, 200, 50, fill='black', border=gradient('darkGrey', 'grey', 'lightGrey', 'black'), borderWidth=10), Circle(200, 200, 38, fill=gradient('red', 'darkRed')))

menu.add(textBox, textBox.text1, startButton)

def onMousePress(mouseX, mouseY):
    if startButton.hits(mouseX, mouseY):
        app.started = True
        menu.clear()

def onMouseMove(mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onKeyPress(key):
    if app.started == True:
        if 'space' == key and player.jumps > 0:
            if player.jumps > 1:
                player.dy -= player.jumpHeight
            else:
                if player.dy > -player.jumpHeight2:
                    player.dy = player.jumpHeight2*-1.5
                else:
                    player.dy -= player.jumpHeight2
            player.jumps -= 1
        if 'q' == key and player.dash > 0:
            angle = angleTo(player.centerX, player.centerY, app.mouseX, app.mouseY)
            x, y = getPointInDir(player.centerX, player.centerY, angle, player.dashLength)
            xchange = int(distance(player.centerX, 0, x, 0))
            ychange = int(distance(0, player.centerY, 0, y))
            if player.centerX > x:
                player.dx += xchange
            if player.centerX < x:
                player.dx -= xchange
            if player.centerY > y:
                player.dy -= ychange/2
            if player.centerY < y:
                player.dy += ychange/2
            player.dash -= 1
        
        

    

def onStep():
    if app.started == True:
        background.toBack()
        player.toFront()
        player.centerX = 150
        player.centerY += player.dy
        map.centerX += player.dx
        gobblerCheck()

        if player.dx > 0:
            player.dx -= app.friction
        if player.dx < 0:
            player.dx += app.friction
        
        if player.hitsShape(floor):
            player.dy = 0
            player.bottom = floor.top
            player.jumps = 2
            player.dash = 1
        
        onPlatformCheck()
        onWallCheck()
        
        if playerOnPlatform() == False:
            player.dy += app.gravity
            if player.jumps > 1:
                player.jumps -= 1   
        
        goal.star.rotateAngle += 10
        
        if player.hitsShape(goal):
            win()
        if player.hitsShape(secret):
            Image(app.rickastleyurl, 0, 0, width=400, height=400)
            Label('You found the secret ending!!!', 200, 200, fill='red', size=30)
            app.stop()
        
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
            gameOverLabel.visible = True
            app.stop()



cmu_graphics.run()