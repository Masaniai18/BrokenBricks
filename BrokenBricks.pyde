xCoord = 100
yCoord = 50
speed = 2
yspeed = 2
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
    rightBoundaryBottomBoundary = 400 - ellipS / 2
    topBoundary = 85
    if xCoord >= rightBoundary bottomBoundary or xCoord <= leftBoundarym topBoundary:
        speed = -speed
    if yCoord >= rightBoundary bottomBoundary or yCoord <= leftBoundary topBoundary:
        yspeed = -yspeed
    xCoord += speed
    yCoord += yspeed
    fill(255,255,0)
    ellipse(xCoord,yCoord,ellipS-15,ellipS-15)
    
    
         
    



    
    
    fill(255)
    rect(rxCoord,ryCoord,rWidth,rHeight)
    rect(rxCoord+100,ryCoord,rWidth,rHeight)
    rect(rxCoord+200,ryCoord,rWidth,rHeight)
    rect(rxCoord+300,ryCoord,rWidth,rHeight)
    rect(rxCoord-150,ryCoord+100,rWidth-50,rHeight-10)
    
    
    fill(255)
    rect(mouseX,375,rWidth-50,rHeight-10)
