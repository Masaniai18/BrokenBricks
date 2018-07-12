xCoord = 50
yCoord = 50
speed = 1
yspeed = 1
ellipS = 50
ryCoord = 0
rxCoord = 0
rWidth = 100
rHeight = 30


def setup():
    size(400,400)
    
def draw():
    background(0)
    global xCoord, yCoord, yspeed, speed, ellipS
    leftTopBoundary = ellipS / 2
    rightBottomBoundary = 400 - ellipS / 2
    if xCoord >= 400 - rightBottomBoundary or xCoord <= leftTopBoundary:
        speed = -speed
    if yCoord >= rightBottomBoundary or yCoord <= leftTopBoundary:
        yspeed = -yspeed
    xCoord += speed
    yCoord += yspeed
    fill(255,0,0)
    ellipse(xCoord,yCoord,ellipS,ellipS)
    fill(255,255,255)
    rect(0,ryCoord,100,30)
    rect(rxCoord+100,ryCoord,rWidth,rHeight)
    rect(rxCoord+200,ryCoord,rWidth,rHeight)
    rect(rxCoord+300,ryCoord,rWidth,rHeight)
    
