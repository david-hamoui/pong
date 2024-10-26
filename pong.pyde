global mode,reload,pos,speed,ballPos,time,ballDir,points,startTime
mode = 'm'
reload = True
pos = [[100,300],[800,300]]
speed = 4
ballPos = [450,300]
ballDir = [-1,-1]
time = 0
startTime = 0
points = 0


def setup():
    size(900,600)
    background(0)
    rectMode(CENTER)
    textAlign(CENTER)
    textFont(createFont("arial",40))


def draw():
    global mode,reload,pos,time,speed,startTime
    
    if mode == 'm':
        if reload:
            background(0)
            fill(255)
            text("Pong",450,100)
            
            reload = False
        
        if button1(450,350,200,50):
            mode = 'p'
        
        fill(0)
        text("Play",450,365)
        time += 1
   
    elif mode == 'p':
        if reload:
            background(0)
            reload = False
        
        for p in pos:
            player(p[0],p[1])
        
        
        updatePlayer(0,returnKey())
        updatePlayer(1,returnKey())
        
        if startTime > 120:
            moveBall(checkForCol())
        
        fill(255)
        text("Points: " + str(points),450,100)
        text("Speed: " + str(speed), 700,100)
        
        if button1(100,100,25,25):
            speed -= 1
        if button1(150,100,25,25):
            speed += 1
    
        
        ball()
        
        time += 1
        startTime += 1


def checkForCol():
    global points
    if ballPos[0]-10 < pos[0][0] + 10 and pos[0][1]+75 > ballPos[1] > pos[0][1]-75:
        points += 1
        return True
    if ballPos[0]+10 > pos[1][0] - 10 and pos[1][1]-75 < ballPos[1] < pos[1][1]+75:
        points += 1
        return True


def ball():
    global reload
    
    fill(255)
    ellipse(ballPos[0],ballPos[1],20,20)
    reload = True

def moveBall(col):
    global ballPos,ballDir
    
    if col:
        ballDir[0] = -ballDir[0]
    
    if 10 > ballPos[1] or ballPos[1] > 590:
        ballDir[1] = -ballDir[1]


    ballPos[1] += ballDir[1] * (speed-2)
    ballPos[0] += ballDir[0] * (speed-2)
    
    

def updatePlayer(num,k):
    global pos,reload
    
    if num == 0:
        if k == ',':
            moveUp(num)
            reload = True
        elif k == 'o':
            moveDown(num)
            reload = True
    else:
        pos[1][1] = ballPos[1]

def moveUp(num):
    global pos
    if pos[num][1] > 75:
        pos[num][1] -= speed/4 + 4
    
def moveDown(num):
    global pos
    if pos[num][1] < 525:
        pos[num][1] += speed/4 + 4

def returnKey():
    if keyPressed:
        return key

def player(xpos,ypos):
    fill(255)
    rect(xpos,ypos,20,150)

def button1(xpos,ypos,xsize,ysize):
    global reload,time
    
    if xpos - xsize/2 < mouseX < xpos+xsize/2 and ypos-ysize/2 < mouseY< ypos + ysize/2:
        fill(230)
        reload = True
        if mousePressed:
            if time > 15:
                time = 0
                return True
    else:
        fill(255)
    
    rect(xpos,ypos,xsize,ysize,8)
