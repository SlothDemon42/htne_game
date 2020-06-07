import pygame

class Player (object):

    inititalJumpSpeed=30
    jumpSpeed=30
    jumping=False

    gravity=2
    initialFallSpeed=0
    fallSpeed=0
    falling=True

    spriteName="./Run1.png"
    spriteNum=0
    sprite=pygame.image.load("./Run1.png");
    sprite=pygame.transform.scale(sprite,(50,50))
    #print(sprite.get_rect().size)

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

    def __init__ (self, xP, yP):
        self.xPos=xP
        self.yPos=yP
        self.wallCollision=False

    def update(self, dir):

        self.collisionInFront.clear()
        self.collisionInMiddle.clear();
        for i in range(int(self.yPos),int(self.height+self.yPos),1):
            self.collisionInMiddle.append(bool(((imageMask.get_at((int(self.xPos+self.width/2),i))) != (image.get_at((int(self.xPos+self.width/2),i))))))
            if(dir==1):
                self.collisionInFront.append(bool((imageMask.get_at((int(self.xPos+self.width),i))) != (image.get_at((int(self.xPos+self.width),i)))))
            elif(dir==-1):
                self.collisionInFront.append(bool((imageMask.get_at((int(self.xPos),i))) != (image.get_at((int(self.xPos),i)))))

        frontCollisionFrac=(self.collisionInFront.count(True)/self.height)

        if(frontCollisionFrac>=0.5):
            #print("wall hit")
            self.wallCollision=True
        else:
            self.wallCollision=False
        #print(self.collisionInMiddle.count(True))
        #print();
        adjustment=0;
        for i in range(self.height-1,0,-1):
            if self.collisionInMiddle[i]:
                adjustment+=1
        #print(adjustment)
        if (adjustment != 0):
            self.yPos-=adjustment
            self.update(dir);
       

        if(imageMask.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height)) == image.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height)) and not self.jumping):
            self.falling=True
        
        
        if(self.falling):
            self.fall();

        self.spriteName
        self.sprite=pygame.image.load(self.spriteName);
        self.sprite=pygame.transform.scale(self.sprite,(50,50))
        if(dir==-1):
            self.sprite=pygame.transform.flip(self.sprite,True,False)
        self.spriteNum+=self.spriteNum;
        self.hitBox=pygame.Rect(self.xPos,self.yPos,self.width,self.height)

    def fall(self):
        self.yPos+=self.fallSpeed
        self.fallSpeed=self.fallSpeed+self.gravity
        if(imageMask.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height)) != image.get_at((int(self.xPos+self.width/2),int(self.yPos)+self.height))):
            self.falling=False;
            self.fallSpeed=self.initialFallSpeed
            self.airDrift=0
            
        

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




#GAME START

pygame.init()
screenWidth=1000;
screenHeight=700;
gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('HTNE Game')

clock=pygame.time.Clock()
    
crashed = False
gameWin=False

xMoveSpeed=1;
leftHeld=False
rightHeld=False
upHeld=False
dir=1;

goalSet=False;

character=Player(40,40)
goal=Goal(0,0)

image=pygame.image.load("./purple2.jpg")
image=pygame.transform.scale(image,(screenWidth,screenHeight))
imageMask=pygame.image.load("./purple2_Mask.jpg")
imageMask=pygame.transform.scale(imageMask,(screenWidth,screenHeight))

while not goalSet:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            goalSet=True
        if event.type == pygame.MOUSEBUTTONUP:
            goalSet=True
            break;
    goal.xPos=pygame.mouse.get_pos()[0];
    goal.yPos=pygame.mouse.get_pos()[1];

    goal.load()
    gameDisplay.blit(image,(0,0))
    gameDisplay.blit(goal.sprite,(goal.xPos, goal.yPos))
    pygame.display.update()
    clock.tick(60) 
        

while not crashed and not gameWin:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                leftHeld=True
                if not character.jumping and not character.falling:
                    dir=-1
            if event.key == pygame.K_d:
                rightHeld=True
                if not character.jumping and not character.falling:
                    dir=1
            if event.key == pygame.K_w and not character.falling:
                character.falling=False
                character.jumping=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                leftHeld=False
            if event.key == pygame.K_d:
                rightHeld=False
                   


    if leftHeld and not character.jumping and not character.falling:
        dir=-1
    if rightHeld and not character.jumping and not character.falling:
        dir=1

    if(not character.wallCollision):
            #print(character.wallCollision)
            if(leftHeld):
                if character.jumping or character.falling:
                    character.airDrift-=character.xMoveSpeed/12
                    character.xPos+=character.airDrift
                else:
                    character.xPos=character.xPos-character.xMoveSpeed

                if (character.xPos<=0):
                        character.xPos=0;
                elif character.xPos+character.width>=screenWidth:
                        character.xPos=screenWidth-character.width-1;
            elif(rightHeld):
                if character.jumping or character.falling:
                    character.airDrift+=character.xMoveSpeed/12
                    character.xPos+=character.airDrift
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
        winGame=True
        break

    character.update(dir)
    goal.load();
    gameDisplay.blit(image,(0,0))
    gameDisplay.blit(character.sprite,(character.xPos, character.yPos))
    gameDisplay.blit(goal.sprite,(goal.xPos,goal.yPos))
    pygame.display.update()
    clock.tick(60) 