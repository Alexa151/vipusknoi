from pygame import*
okno = display.set_mode((1000,600),FULLSCREEN)
game = True
clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,pikt,x,y):
        self.image= transform.scale(image.load(pikt),(120,140))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x 
        self.lasty = self.rect.y
    def ris(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))


fon1 = transform.scale(image.load('fon.jpg'),(1000,600))
fon2 = transform.scale(image.load('fon.jpg'),(1000,600))
fon3 = transform.scale(image.load('fon.jpg'),(1000,600))
x1= 0
shag = 0 
geroi=GameSprite('bob1.png',300,350)

brevno1=GameSprite('brevno1.png',350,350)
brevno2=GameSprite('brevno1.png',350,350)
brevno3=GameSprite('brevno1.png',350,350)
brevno4=GameSprite('brevno1.png',350,350)
brevno5=GameSprite('brevno1.png',350,350)
brevno6=GameSprite('brevno1.png',350,350)
brevno7=GameSprite('brevno1.png',350,350)
brevno8=GameSprite('brevno1.png',350,350)
brevno9=GameSprite('brevno1.png',350,350)
brevno10=GameSprite('brevno1.png',350,350)

brevns=[
    brevno1,
brevno2,
brevno3,
brevno4,
brevno5,
brevno6,
brevno7,
brevno8,
brevno9,
brevno10
]


gravity = 1
xigroka = 0

while game:
    for i in event.get():
        if i.type==QUIT:
            game=False
        if i.type ==KEYDOWN:
            if i.key ==K_ESCAPE:
                game=False

    okno.blit(fon1,(-1000+x1,0))
    okno.blit(fon2,(0+x1,0))
    okno.blit(fon3,(1000+x1,0))
    geroi.ris()
    brevno1.ris()
    brevno1.rect.x = 600+ xigroka
    brevno2.ris()
    brevno2.rect.x = 950+ xigroka
    brevno3.ris()
    brevno3.rect.x = 1300+ xigroka
    brevno4.ris()
    brevno4.rect.x = 1650+ xigroka
    brevno5.ris()
    brevno5.rect.x = 2200+ xigroka
    brevno6.ris()
    brevno6.rect.x = 2600+ xigroka
    brevno7.ris()
    brevno7.rect.x = 2950+ xigroka
    brevno8.ris()
    brevno8.rect.x = 3300+ xigroka
    brevno9.ris()
    brevno9.rect.x = 3600+ xigroka
    brevno10.ris()
    brevno10.rect.x = 4000+ xigroka
    for b in brevns:
        if sprite.collide_rect(b,geroi):
            game=False


    kn = key.get_pressed()
    if kn[K_RIGHT]:
        xigroka -= 5
        x1 -= 5
        shag -=3
    if kn[K_LEFT]:
        x1 += 5
        shag =+3
        xigroka += 5
    if kn[K_SPACE]:
        geroi.rect.y -= 11.5
        gravity+= 0.1
    geroi.rect.y += (5+ gravity)
    if  geroi.rect.y > 350:
        geroi.rect.y = 350
        gravity = 0
    if x1 < -1000:
        x1= 0
    if x1 > 1000:
        x1= 0
    display.update()
    clock.tick(60)
