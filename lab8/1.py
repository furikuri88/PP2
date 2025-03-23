import pygame
import random
pygame.init()
#4496
with open("record.txt", "r") as txt:
    con = txt.read().strip()
reco=int(con)
with open("coins.txt", "r") as tx:
    co = tx.read().strip()
obc=int(co)
clock=pygame.time.Clock()
scr=pygame.display.set_mode((840,650))
scr.fill((255,255,255))
road=pygame.image.load("images/road.png")
road2=pygame.image.load("images/road.png")
player=pygame.image.load("images/player.png")
enemy=pygame.image.load("images/enemy.png")
coin=pygame.transform.scale(pygame.image.load("images/coin.png"),(44,43))
y=0
xp=420
yp=525
ye=-93
xe=random.randint(140,650)
yc=-43
xc=random.randint(140,650)
while ((xc<xe and xe<xc+44) or (xc>xe and xe+48>xc)):
    xc=random.randint(140,650)

done=True
sur=True
f=pygame.font.Font("fonts/cartoon.ttf",100)
go=f.render("Game Over", False,(255,255,255))
p=pygame.font.Font("fonts/day.ttf",60)
pres=p.render("press R to restart",False,(0,0,0))
rec=pygame.Surface((840,650))
rec.fill(color="Red")
crush=pygame.mixer.Sound("sounds/crash.wav")
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)
#132135

s=pygame.font.Font("fonts/day.ttf",20)
wer=pygame.font.Font("fonts/day.ttf",40)
scores=0
cn=0
while done:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            done=False
        if ev.type==pygame.KEYDOWN and ev.key==pygame.K_r:
            sur=True
            yc=-43
            cn=0
            xp=420
            ye=-93
            pygame.mixer.music.play(-1)
            scores=0
            
    if sur==True:

        pre=pygame.key.get_pressed()
        if pre[pygame.K_RIGHT] and xp+player.get_width()<700:
            xp+=10
        if pre[pygame.K_LEFT] and xp>140:
            xp-=10
        ts=s.render(f"score: {scores}",False,(0,0,0))
        y+=5
        yc+=9
        ye+=18
        
        if ye>=743:
            scores+=1
            ye=-93
            xe=random.randint(140,650)
        if yc>=693:
            yc=-43
            xc=random.randint(140,650)
            while (xc<xe and xe<xc+44) or (xc>xe and xe+48>xc):
                xc=random.randint(140,650)
        if y==650:
            y=0
        if yc+43>yp and yc<yp+96 and ((xp<xc and xc<xp+44) or (xp>xc and xc+44>xp)):
            yc=-43
            xc=random.randint(140,650)
            while ((xc<xe and xe<xc+44) or (xc>xe and xe+48>xc)):
                xc=random.randint(140,650)
            cn+=1
        tc=s.render(str(cn),False,"Yellow")
        scr.blit(road,(0,y))
        scr.blit(road2,(0,y-650))
        scr.blit(player,(xp,yp))
        scr.blit(enemy,(xe,ye))
        scr.blit(ts,(320,50))
        scr.blit(coin,(0,0))
        scr.blit(tc,(53,10))
        scr.blit(coin,(xc,yc))
    else:
        scr.blit(rec,(0,0))
        scr.blit(go,(220,200))
        scr.blit(pres,(210,280))
        scr.blit(wer.render(f"your score: {scores}",False,(0,0,0)),(315,360))
        scr.blit(wer.render(f"best score: {reco}",False,(0,0,0)), (280,70))
        scr.blit(s.render(f"coins in round {cn}",False,("Yellow")),(360,420))
        scr.blit(wer.render(str(obc),False,"Yellow"), (240,5))
        scr.blit(coin,(186,0))

    if ye+93>yp and ye<yp+96 and ((xp<xe and xe<xp+44) or (xp>xe and xe+48>xp)) and sur==True:
        if scores>reco:
            reco=scores
            with open('record.txt', 'w') as file:
                file.write(str(reco))
        obc+=cn
        with open('coins.txt', 'w') as file:
                file.write(str(obc))
        sur=False
        pygame.mixer.music.stop()
        crush.play()


    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)