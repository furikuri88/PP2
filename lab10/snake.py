import pygame
import random
import time
import psycopg2
from tabulate import tabulate
pygame.init()
W=1200
H=850
xs=[90,1050]
ys=[90,710]
def bo(x,y,k,d):
    return y<d[0] or y>d[1] or x<k[0] or x>k[1]
try:
    connection=psycopg2.connect(
        dbname="snake",
        host="localhost",
        user="postgres",
        password="1488"
    )
    connection.autocommit=True
    with connection.cursor() as cur:
        cur.execute("select * from snakeuser;")
        mas=cur.fetchall()
    r=input("l-log in,r-registration: ")
    while r!='l' and r!='r':
        print("not clear")
        r=input("l-log in,r-registration: ")
    if r=='l':
        b=True
        k=False
        while b:
            if k==True:
                print("try again")
            k=True
            user=input("username: ")
            for x in mas:
                if user==x[1]:
                    scc=x[2]
                    lll=x[3]
                    le=x[4]
                    sctt=x[5]
                    b=False
    elif r=='r':
        b=True
        k=False
        while b:
            jj=True
            if k==True:
                print("user already exist")
            k=True
            user=input("create user: ")
            for x in mas:
                if user==x[1]:
                    jj=False
            if jj==True:
                b=False
        scc=0
        lll=1
        le=1
        sctt=9
        with connection.cursor() as cur:
            cur.execute(f"insert into snakeuser(username,score,lvl,lenth,sct) VALUES('{user}',{scc},{lll},{le},{sctt});")
            
            
    with connection.cursor() as cur:
        cur.execute(f"select id,username,score,lvl from snakeuser where username='{user}';")
        row=cur.fetchall()
        columns = []
        for desc in cur.description:
            columns.append(desc[0])
        print(tabulate(row, headers=columns, tablefmt="psql"))
    play=input("n-new game,c-continue: ")
    while play!='n' and play!='c':
        print("not clear")
        play=input("n-new game,c-continue: ")
    if play=='n':
        scc=0
        lll=1
    timing=time.time()
    timb=False #to start secoundmeter
    clock=pygame.time.Clock()
    scr=pygame.display.set_mode((W,H))
    lv=lll
    sh=pygame.image.load("images/snakeh.png") #head
    sb=pygame.image.load("images/snakeb.png") #body
    st=pygame.transform.rotate(pygame.image.load("images/snaket.png"),180) #tail

    srw=pygame.image.load("images/snake1.png")   #body when it rotates
    srd=pygame.image.load("images/snake14.png")
    slw=pygame.image.load("images/snake12.png")
    sld=pygame.image.load("images/snake13.png")

    meat=pygame.image.load("images/meat.png") #food
    gap=pygame.transform.scale(pygame.image.load("images/gapple.png"),(40,40))
    crab=pygame.transform.scale(pygame.image.load("images/crabsb.png"),(40,40)) #great food
    food=random.choice((meat,gap)) #random
    liof=[sb] #lenth of body

    ship=pygame.image.load("images/shipi.png") #border
    ship2=pygame.image.load("images/shipi2.png")
    lv1=pygame.Surface((1200,850))
    lv2=pygame.transform.scale(pygame.image.load("images/lvl2.jpeg"),(1200,850))
    lv3=pygame.transform.scale(pygame.image.load("images/lvl3.png"),(1200,850))  #lvl backgrounds
    lv4=pygame.transform.scale(pygame.image.load("images/lvl4.jpeg"),(1200,850))

    lv1.fill((0,0,0))
    fps=5 #fps
    lens=le #lenth of body
    sur=True #survival of snake
    done=True 
    x=W/2
    y=H/2
    k=x
    p=y-40
    py=True #action to down
    px=False #to right
    pxl=False #to left
    pyw=False #to up
    i=0 #amount of rotates
    yiu=0
    yid=0
    xil=0
    fi=0
    foode=True #exiting of great food

    an=0 #angle
    rot=False 
    rot2=False
    rot3=False
    rot4=False
    pos=[(x,p-40),(k,p)] #positions of parts of body(tail,body)
    for j in range(0,lens-1):
        p=p-40
        pos.append((k,p))
        liof.append(sb)

    rx=random.randint(90,1050) 
    ry=random.randint(90,710) #meat position
    iea=pos[0]
    scor=scc
    f=pygame.font.Font("fonts/cartoon.ttf",100)
    go=f.render("Game Over", False,(255,255,255))
    pon=pygame.font.Font("fonts/day.ttf",60)
    pres=pon.render("press R to restart",False,(0,0,0))
    wer=pygame.font.Font("fonts/day.ttf",40)
    nex=False #to next lvl
    cong=False #WIN
    sct=2000 #score to go next or win
    det=True
    pause=False
    while done:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                with connection.cursor() as cur:
                    cur.execute(f"""UPDATE snakeuser
                                SET score={scor},
                                lvl={lv},
                                lenth={lens}
                                WHERE username='{user}';""")
                done=False
            if ev.type==pygame.KEYDOWN:
                if ev.key==pygame.K_p:
                    if pause==False:
                        pause=True
                    else:
                        pause=False
                if ev.key==pygame.K_r or (nex==True and ev.key==pygame.K_n):
                    sur=True
                    fi=0
                    foode=True
                    timb=False
                    food=random.choice((meat,gap))
                    x=W/2
                    y=H/2
                    liof=[sb]
                    k=x
                    p=y-40
                    py=True
                    px=False
                    pxl=False
                    pyw=False
                    rot=False
                    i=0
                    rx=random.randint(90,1110)
                    ry=random.randint(90,760)
                    lens=1
                    pos=[(x,p-40),(k,p)]
                    sh=pygame.image.load("images/snakeh.png")
                    sb=pygame.image.load("images/snakeb.png")
                    st=pygame.transform.rotate(pygame.image.load("images/snaket.png"),180)

                    srw=pygame.image.load("images/snake1.png")
                    srd=pygame.image.load("images/snake14.png")
                    slw=pygame.image.load("images/snake12.png")
                    sld=pygame.image.load("images/snake13.png")
                    iea=pos[0]
                    scor=0
                    nex=False
                    rot2=False
                    rot3=False
                    rot4=False
        if scor>=sct and lv==1:
            sct=15
            nex=True
            lv+=1
        if scor>=sct and lv==2:
            sct=18
            nex=True
            lv+=1
        if scor>=sct and lv==3:
            sct=25
            nex=True
            lv+=1
        if scor>=sct and lv==4:
            cong=True
        
        

        pre=pygame.key.get_pressed()
        if sur==True and nex==False and cong==False:
            if lv==1:
                scr.blit(lv1,(0,0)) 
                sct=9
            elif lv==2:
                sct=15
                scr.blit(lv2,(0,0))
                fps=8 #velocity to 8
            elif lv==3:
                sct=18
                scr.blit(lv3,(0,0))
                fps=10 #velocity to 10
            elif lv==4:
                sct=25
                scr.blit(lv4,(0,0))
                fps=12
                ys=[0,H]
                ship=ship2
                det=False
            if pause==False:
                if py==True:
                    
                    y+=40 #action for 1 body
                if pyw==True:
                    y-=40
                if px==True:
                    x+=40
                if pxl==True:
                    x-=40
                if i<lens+1:
                    liof[i-1]=pygame.transform.rotate(liof[i-1],an)
                    yui=liof[i-1]  #rotate body
                
                if pre[pygame.K_DOWN] and (px==True or pxl==True):
                    if px==True:
                        an=-90
                        a1=srd #gebuig body
                    else:
                        a1=slw
                        an=90
                    rot=True
                    sh=pygame.transform.rotate(sh,an) #rotate head
                    yid=0
                    py=True
                    px=False
                    pxl=False
                    pyw=False
                if pre[pygame.K_UP] and (px==True or pxl==True):
                    if px==True:
                        an=90
                        a2=srw
                    else:
                        a2=sld
                        an=-90
                    rot2=True
                    sh=pygame.transform.rotate(sh,an)
                    yiu=0
                    py=False
                    px=False
                    pxl=False
                    pyw=True
                if pre[pygame.K_RIGHT] and (py==True or pyw==True):
                    i=0
                    if py==True:
                        a=sld
                        an=90
                    else:
                        a=slw
                        an=-90
                    rot3=True
                    sh=pygame.transform.rotate(sh,an)
                    py=False
                    px=True
                    pxl=False
                    pyw=False
                if pre[pygame.K_LEFT] and (py==True or pyw==True): 
                    if py==True:
                        a3=srw
                        an=-90
                    else:
                        a3=srd
                        an=90
                    rot4=True
                    sh=pygame.transform.rotate(sh,an)
                    xil=0
                    py=False
                    px=False
                    pxl=True
                    pyw=False
                
                if (yid==lens+1 and rot) or (yiu==lens+1 and rot2) or (i==lens+1 and rot3) or (xil==lens+1 and rot4):
                    st=pygame.transform.rotate(st,90)

                if rot3==True and i<lens+1 and i>=1:
                    if i>1:
                        liof[i-2]= pygame.transform.rotate(sb,90)
                    ish1=liof[i-1]
                    liof[i-1]=a #body-->gebuig body
                elif rot3==True and i>=1:
                    liof[i-2]=pygame.transform.rotate(sb,90)
                    rot3=False

                if rot==True and yid<lens+1 and yid>=1:
                    if yid>1:
                        liof[yid-2]=sb
                    ish2=liof[yid-1]
                    liof[yid-1]=a1 #body-->gebuig body
                elif rot==True and yid>=1:
                    liof[yid-2]=sb
                    rot=False

                if rot2==True and yiu<lens+1 and yiu>=1:
                    if yiu>1:
                        liof[yiu-2]=sb
                    ish3=liof[yiu-1]
                    liof[yiu-1]=a2 #body-->gebuig body
                elif rot2==True and yiu>=1:
                    liof[yiu-2]=sb
                    rot2=False

                if rot4==True and xil<lens+1 and xil>=1:
                    if xil>1:
                        liof[xil-2]=pygame.transform.rotate(sb,90)
                    ish4=liof[xil-1]
                    liof[xil-1]=a3 #body-->gebuig body
                elif rot4==True and xil>=1:
                    liof[xil-2]=pygame.transform.rotate(sb,90)
                    rot4=False

                if len(pos)>3:
                    for g in pos[:-1]:
                        if g[0]==x and g[1]==y:
                            sur=False #harakiri function
                
                if timb==True: #timer begining
                    timing=time.time()
                    timb=False

                if food==crab:
                    if time.time()-timing>5.0: #timer process
                        timing=time.time()
                        foode=False
                if ((x+40>=rx and x<=rx) or (x>=rx and x-40<=rx)) and ((y<=ry and y+40>=ry) or (y>=ry and y-40<=ry)):
                    rx=random.randint(xs[0],xs[1])
                    ry=random.randint(ys[0],ys[1])
                    for m in pos:
                        while (m[0]+40>=rx and m[0]<=rx) or (m[0]>=rx and m[0]-40<=rx) and ((m[1]<=ry and m[1]+40>=ry) or (m[1]>=ry and m[1]-40<=ry)):
                            rx=random.randint(xs[0],xs[1])
                            ry=random.randint(ys[0],ys[1]) #due to it food dont have same position with snake
                    
                    liof.append(yui) #push rotated body
                    pos.insert(0,iea) 
                    lens+=1
                    if food==meat:
                        scor+=1
                    elif food==gap:
                        scor+=2
                    else:
                        scor+=4
                        fi=0
                    if fi!=5:
                        food=random.choice((meat,gap))
                    else: #to get great food
                        food=crab
                        timb=True
                    fi+=1
                elif food==crab and foode==False: #if time is over
                    food=random.choice((meat,gap))
                    fi=0
                    rx=random.randint(xs[0],xs[1])
                    ry=random.randint(ys[0],ys[1])
                    for m in pos:
                        while (m[0]+40>=rx and m[0]<=rx) or (m[0]>=rx and m[0]-40<=rx) and ((m[1]<=ry and m[1]+40>=ry) or (m[1]>=ry and m[1]-40<=ry)):
                            rx=random.randint(xs[0],xs[1])
                            ry=random.randint(ys[0],ys[1])
                    foode=True
                sctxt=wer.render(f"score  {scor}",False,"Green")
                scr.blit(ship,(0,0))

                scr.blit(sh,(x,y))
                for j in range(0,len(liof)):
                    scr.blit(liof[j],pos[lens-j])
                scr.blit(st,(pos[0]))
                scr.blit(food,(rx,ry))
                scr.blit(sctxt,(550,70))
                scr.blit(wer.render(f"score to next {sct}",False,"Blue"),(510,120))
                scr.blit(wer.render(f"lvl: {lv}",False,"Yellow"),(900,70))
                k=x
                p=y
                iea=pos[0] #save position for tail if there will new part of body
                pos.pop(0) 
                pos.append((k,p))
                i+=1
                yid+=1
                yiu+=1
                xil+=1

                if bo(x,y,xs,ys) and det==True:
                    sur=False
                if det==False and (x<xs[0] or x>xs[1]):
                    sur=False
                if det==False and y<0:
                    y=H
                if det==False and y>H:
                    y=0
            elif pause==True:
                scr.blit(ship,(0,0))

                scr.blit(sh,(x,y))
                for j in range(0,len(liof)):
                    scr.blit(liof[j],pos[lens-j])
                scr.blit(st,(pos[0]))
                scr.blit(food,(rx,ry))
                scr.blit(sctxt,(550,70))
                scr.blit(wer.render(f"score to next {sct}",False,"Blue"),(510,120))
                scr.blit(wer.render(f"lvl: {lv}",False,"Yellow"),(900,70))
        elif nex==False and cong==False: #restart window
            pygame.draw.rect(scr,"Red",pygame.Rect(0, 0, W, H))
            scr.blit(go,(400,250))
            scr.blit(pres,(370,400))
        elif cong==False: #next level window
            pygame.draw.rect(scr,"Blue",pygame.Rect(0, 0, W, H))
            scr.blit(wer.render("press n to next lvl",False,"Red"),(300,300))
        else: #win window
            scr.blit(pygame.transform.scale(pygame.image.load("images/youwin.jpg"),(1200,850)),(0,0))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
except Exception as _ex:
    print("[INFO]: ERROR",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO]: closed")
