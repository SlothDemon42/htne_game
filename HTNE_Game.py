import pygame

class Player (object):

    inititalJumpSpeed=30
    jumpSpeed=30
    jumping=False

    gravity=3
    initialFallSpeed=0
    fallSpeed=0
    falling=True

    spriteName="./img/Run1.png"
    spriteNum=1
    sprite=pygame.image.load("./img/Run1.png");
    sprite=pygame.transform.scale(sprite,(50,50))
    #print(sprite.get_rect().size)

    xSpawn=0;
    ySpawn=0;
    xPos=20;
    yPos=400;
    xMoveSpeed=10
    airDrift=0;
    width=(sprite.get_rect().size)[0];
    height=sprite.get_rect().size[1];

    collisionInFront=[];
    collisionInMiddle=[];
    wallCollision=False;
    frontCollisionFrac=0;

    hitBox=pygame.Rect(xPos,yPos,width,height);

    playable=False

    def __init__ (self, xP, yP):
        self.xPos=xP
        self.yPos=yP
        self.wallCollision=False
        self.playable=False

    def update(self, dir):
        if self.playable and endCondition==0:
            self.collisionInFront.clear()
            self.collisionInMiddle.clear();
            for i in range(int(self.yPos),int(self.height+self.yPos),1):
                pixelColor=(imageMask.get_at((int(self.xPos+self.width/2),i)))
                self.collisionInMiddle.append(bool(pixelColor[0]!=pixelColor[1] or pixelColor[1]!=pixelColor[2] or pixelColor[0]!=pixelColor[2]))
                if(dir==1):
                    pixelColor=(imageMask.get_at((int(self.xPos+self.width),i)))
                    self.collisionInFront.append(bool(pixelColor[0]!=pixelColor[1] or pixelColor[1]!=pixelColor[2] or pixelColor[0]!=pixelColor[2]))
                elif(dir==-1):
                    pixelColor=(imageMask.get_at((int(self.xPos),i)))
                    self.collisionInFront.append(bool(pixelColor[0]!=pixelColor[1] or pixelColor[1]!=pixelColor[2] or pixelColor[0]!=pixelColor[2]))

            frontCollisionFrac=(self.collisionInFront.count(True)/self.height)

            if(frontCollisionFrac>=0.5):
                #print("wall hit")
                self.wallCollision=True
            else:
                self.wallCollision=False
            #print(self.collisionInMiddle.count(True))
            #print();
            adjustment=0;
            for i in range(self.height-1,int((self.height-1)/2),-1):
                if self.collisionInMiddle[i]:
                    adjustment+=1
            #print(adjustment)
            if (adjustment != 0):
                self.yPos-=adjustment
                self.update(dir);
       
            pixelColor=imageMask.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height))
            if(pixelColor[0]==pixelColor[1] and pixelColor[1]==pixelColor[2] and not self.jumping):
                self.falling=True

        
        
            if(self.falling):
                self.fall();

        if not self.jumping and (leftHeld or rightHeld):
            if self.spriteNum>3:
                self.spriteNum=1
            self.spriteName="./img/Run"+str(self.spriteNum)+".png"
            self.spriteNum+=1;
        elif self.jumping:
            self.spriteName="./img/Jump1.png"
        elif self.falling:
            self.spriteName="./img/Fall.png"
        else: 
            self.spriteName="./img/Stand.png"

        #self.spriteName="./img/Run1.png"

        self.sprite=pygame.image.load(self.spriteName);
        self.sprite=pygame.transform.scale(self.sprite,(50,50))
        self.width=(self.sprite.get_rect().size)[0];
        self.height=self.sprite.get_rect().size[1];

        if(dir==-1):
            self.sprite=pygame.transform.flip(self.sprite,True,False)
        #self.spriteNum+=self.spriteNum;
        self.hitBox=pygame.Rect(self.xPos,self.yPos,self.width,self.height)

    def fall(self):
        self.yPos+=self.fallSpeed
        self.fallSpeed=self.fallSpeed+self.gravity
        pixelColor=imageMask.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height))
        if(pixelColor[0]!=pixelColor[1] or pixelColor[1]!=pixelColor[2] or pixelColor[0]!=pixelColor[2]):
            self.falling=False
            self.fallSpeed=self.initialFallSpeed
            self.airDrift=0
        if(self.yPos+self.height>=screenHeight-100):
            endCondition=3;
            self.fallSpeed=0;
            self.xPos=self.xSpawn;
            self.yPos=self.ySpawn;
            
        

    def jump(self):
        self.yPos-=self.jumpSpeed
        self.jumpSpeed=self.jumpSpeed-self.gravity
        if(self.yPos<0):
            self.yPos=0
        if(self.jumpSpeed==0):
            self.jumping=False
            self.falling=True
            self.jumpSpeed=self.inititalJumpSpeed

class Goal (object):
    xPos=0;
    yPos=0;
    sprite=pygame.image.load("./StarSprites/0.png");
    spriteNum=0;
    hitBox=pygame.Rect((xPos,yPos),(sprite.get_rect().size));

    def __init__ (self, xP, yP):
        self.xPos=xP
        self.yPos=yP
        self.wallCollision=False

    def load(self):
        self.spriteNum+=0.2
        if self.spriteNum>=8: self.spriteNum=0
        self.sprite=pygame.image.load("./StarSprites/"+str(int(self.spriteNum))+".png");
        self.hitBox=pygame.Rect((self.xPos,self.yPos),(self.sprite.get_rect().size));

class Obstacle (object):
    xPos=0;
    yPos=0;
    sprite=pygame.image.load("./EnemySprites/0.png");
    spriteNum=0;
    hitBox=pygame.Rect((xPos,yPos),(sprite.get_rect().size));
    wrongSpriteList=[15, 32, 33, 34, 35, 36, 37, 40, 42,49,54,57,71,72,75,76,77,78,79,86,87,88,89,92,97,101,102,103,104,105,106,122, 123, 124,125,126,127,128,129,130,139,140,148,149,150,151,152,161,163,164,171]

    def __init__ (self, xP, yP):
        self.xPos=xP
        self.yPos=yP

    def load(self):
        self.spriteNum+=1
        if self.spriteNum>=173: self.spriteNum=0

        while self.wrongSpriteList.count(self.spriteNum) !=0:
            self.spriteNum+=1
        self.sprite=pygame.image.load("./EnemySprites/"+str(int(self.spriteNum))+".png");
        self.hitBox=pygame.Rect((self.xPos,self.yPos),(self.sprite.get_rect().size));


#GAME START

pygame.init()
screenWidth=1000;
screenHeight=700;
gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('HTNE Game')

clock=pygame.time.Clock()
    
crashed = False
endCondition=0 #0=ongoing 1=restart 2=death 3=win 4=quit

leftHeld=False
rightHeld=False
upHeld=False
dir=1;

goalSet=False;
charPlaced=False;
badCount=0;
maskOn=False;

character=Player(50,0)
character.playable=False
goal=Goal(0,0)
badList=[]

image=pygame.image.load("./HTNE_image.jpg")
image=pygame.transform.scale(image,(screenWidth,screenHeight))
imageMask=pygame.image.load("./HTNE_stage.jpg")
imageMask=pygame.transform.scale(imageMask,(screenWidth,screenHeight))


while not goalSet:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            goalSet=True
            charPlaced=True
        if event.type == pygame.MOUSEBUTTONUP:
            goalSet=True
            break;
    goal.xPos=pygame.mouse.get_pos()[0];
    goal.yPos=pygame.mouse.get_pos()[1];

    goal.load()
    gameDisplay.blit(imageMask,(0,0))
    gameDisplay.blit(goal.sprite,(goal.xPos, goal.yPos))

    pygame.display.update()
    clock.tick(60)

while badCount<3:
    temp=Obstacle(0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            badCount=4
        if event.type == pygame.MOUSEBUTTONUP:
            badList.append(temp)
            badCount+=1
    temp.xPos=pygame.mouse.get_pos()[0];
    temp.yPos=pygame.mouse.get_pos()[1];

    goal.load();
    temp.load();
    gameDisplay.blit(imageMask,(0,0))
    gameDisplay.blit(goal.sprite,(goal.xPos, goal.yPos))
    gameDisplay.blit(temp.sprite,(temp.xPos,temp.yPos))
    for i in range(0,len(badList)):
       badList[i].load();
       gameDisplay.blit(badList[i].sprite,(badList[i].xPos,badList[i].yPos))

    pygame.display.update()
    clock.tick(60)

while not charPlaced:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            charPlaced=True
        if event.type == pygame.MOUSEBUTTONUP:
            charPlaced=True
            character.playable=True
            break;
    character.xPos=pygame.mouse.get_pos()[0];
    character.yPos=pygame.mouse.get_pos()[1];
    character.xSpawn=character.xPos;
    character.ySpawn=character.yPos;

    character.update(1)
    goal.load();
    gameDisplay.blit(imageMask,(0,0))
    gameDisplay.blit(goal.sprite,(goal.xPos, goal.yPos))
    gameDisplay.blit(character.sprite,(character.xPos,character.yPos))
    for i in range(0,len(badList)):
       badList[i].load();
       gameDisplay.blit(badList[i].sprite,(badList[i].xPos,badList[i].yPos))
    pygame.display.update()
    clock.tick(60)
        


while not crashed:
    print("Restart")
    endCondition=0;
    character.xPos=character.xSpawn;
    character.yPos=character.ySpawn;
    while endCondition==0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                endCondition=4;
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    leftHeld=True
                    if not character.jumping and not character.falling:
                        dir=-1
                if event.key == pygame.K_d:
                    rightHeld=True
                    if not character.jumping and not character.falling:
                        dir=1
                if event.key == pygame.K_SPACE and not character.falling:
                    character.falling=False
                    character.jumping=True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    leftHeld=False
                if event.key == pygame.K_d:
                    rightHeld=False
                if event.key ==pygame.K_r:
                    endCondition=1;
                if event.key == pygame.K_t:
                    maskOn=not maskOn;
                   


        if leftHeld and not character.jumping and not character.falling:
            dir=-1
        if rightHeld and not character.jumping and not character.falling:
            dir=1

        if(not character.wallCollision):
                #print(character.wallCollision)
                if(leftHeld):
                    if character.jumping or character.falling:
                        character.airDrift-=character.xMoveSpeed/10
                        character.xPos+=character.airDrift-character.xMoveSpeed
                    else:
                        character.xPos=character.xPos-character.xMoveSpeed

                    if (character.xPos<=0):
                            character.xPos=0;
                    elif character.xPos+character.width>=screenWidth:
                            character.xPos=screenWidth-character.width-1;
                elif(rightHeld):
                    if character.jumping or character.falling:
                        character.airDrift+=character.xMoveSpeed/10
                        character.xPos+=character.airDrift+character.xMoveSpeed
                    else:
                        character.xPos=character.xPos+character.xMoveSpeed

                    if (character.xPos<=0):
                            character.xPos=0;
                    elif character.xPos+character.width>=screenWidth:
                            character.xPos=screenWidth-character.width-1;
                elif(character.jumping or character.falling):
                        character.xPos+=character.airDrift;
                        if (character.xPos<=0):
                            character.xPos=0;
                        elif character.xPos+character.width>=screenWidth:
                            character.xPos=screenWidth-character.width-1;

        if(character.jumping):
            character.jump();

        if(character.hitBox.colliderect(goal.hitBox)):
            print("WIN")
            endCondition=3

        for i in range(0,len(badList)):
            if character.hitBox.colliderect(badList[i].hitBox):
                print("Dead")
                endCondition=2
                break;

        character.update(dir)

        goal.load();
        if not maskOn:
            gameDisplay.blit(image,(0,0))
        else:
            gameDisplay.blit(imageMask,(0,0))
        gameDisplay.blit(character.sprite,(character.xPos, character.yPos))
        gameDisplay.blit(goal.sprite,(goal.xPos,goal.yPos))
        for i in range(0,len(badList)):
            badList[i].load();
            gameDisplay.blit(badList[i].sprite,(badList[i].xPos,badList[i].yPos))
        pygame.display.update()
        clock.tick(60) 