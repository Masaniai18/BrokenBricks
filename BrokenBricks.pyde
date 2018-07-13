xCoord = 100
yCoord = 50
speed = 3
yspeed = 4
ellipS = 50 - 15
ryCoord = 0
rxCoord = 0
rWidth = 100
rHeight = 30


def setup():
    size(400,400)
    
def draw():
    background(0)
    global xCoord, yCoord, yspeed, speed, ellipS 
    leftBoundary = ellipS / 2
    rightBoundary = 400 - ellipS / 2
    topBoundary = ellipS / 2 
    bottomBoundary = 400 - ellipS / 2 
    brickBoundary = rHeight
    paddleBoundary = fill(255,255,255),(rect(mouseX,375,rWidth-50,rHeight-10))
    insidebrick1 = (xCoord >= 0 and xCoord <= 100 and yCoord >= 0 and yCoord <= 30)
    insidebrick2 = (xCoord >= 100 and xCoord <= 200 and yCoord >= 0 and yCoord <= 30)
    insidebrick3 = (xCoord >= 200 and xCoord <= 300 and yCoord >= 0 and yCoord <= 30)
    insidebrick4 = (xCoord >= 300 and xCoord <= 400 and yCoord >= 0 and yCoord <= 30)
    if yCoord >=  bottomBoundary or yCoord <= topBoundary:
        yspeed = -yspeed
    if xCoord >= rightBoundary or xCoord <= leftBoundary:
        speed = -speed
    xCoord += speed
    yCoord += yspeed
    fill(255,255,0)
    ellipse(xCoord,yCoord,ellipS,ellipS)          # Ball
    
    bb1 =
    bb2 =
    bb3 =
    bb4 =
    
    global bb1,bb2,bb3,bb4
    
    global 
    if insidebrick1:
        fill(0)
    else:
        fill(255)
    rect(rxCoord,ryCoord,rWidth,rHeight)                # 1 brick 
    global
    if insidebrick2:
        fill(0)
    else:
        fill(255)
    rect(rxCoord+100,ryCoord,rWidth,rHeight)            # 2 brick
    global
    if insidebrick3:
        fill(0)
    else: 
        fill(255)
    rect(rxCoord+200,ryCoord,rWidth,rHeight)            # 3 brick 
    global
    if insidebrick4:
        fill(0)
    else:
        fill(255)
    rect(rxCoord+300,ryCoord,rWidth,rHeight)            # 4 brick 
    
    #rect(rxCoord,ryCoord,rWidth,rHeight)                # 1 brick 
   # rect(rxCoord+100,ryCoord,rWidth,rHeight)            # 2 brick
    #rect(rxCoord+200,ryCoord,rWidth,rHeight)            # 3 brick 
    #rect(rxCoord+300,ryCoord,rWidth,rHeight)            # 4 brick 
    rect(rxCoord-150,ryCoord+100,rWidth-50,rHeight-10)  # Paddle 


    if xCoord >= mouseX or xCoord <= mouseX:
        
        fill(255)
    rect(mouseX,375,rWidth-50,rHeight-10)               # Paddle follows mouse
