import random
import pygame
import math
import sys
from PIL import Image
import numpy as np

####################################SCREEN
pygame.init()
width=1000
height=600
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Raycasting")

start=True

mapping=np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2 ],
                  [2, 0, 0, 0, 0, 0, 3, 0, 0, 2 ],
                  [2, 0, 0, 0, 0, 0, 3, 0, 0, 2 ],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2 ],
                  [2, 0, 1, 1, 0, 1, 0, 0, 0, 2 ],
                  [2, 0, 1, 0, 0, 1, 0, 0, 0, 2 ],
                  [2, 0, 1, 0, 0, 1, 0, 0, 0, 2 ],
                  [2, 0, 0, 0, 2, 2, 2, 2, 2, 2 ],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2 ],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]])
X=15
Y=15
rotation=0
field=60
while start:
    pygame.draw.rect(win,(231,100,135),(0,height/2,width,height/2),0)    
    pygame.draw.rect(win,(114,165,200),(0,0,width,height/2),0)    
    keys= pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            start=False
    delta=1
    posX=X
    posY=Y
    view=0
    if keys[pygame.K_e]:
        rotation+=5
    if keys[pygame.K_q]:
        rotation-=5
    if keys[pygame.K_w]:
        anglew=np.deg2rad(rotation)
        X+=delta*0.8*math.cos(anglew)
        Y+=delta*0.8*math.sin(anglew)
    if keys[pygame.K_s]:
        angles=np.deg2rad(rotation)
        X-=delta*0.8*math.cos(angles)
        Y-=delta*0.8*math.sin(angles)
    if keys[pygame.K_d]:
        angled=np.deg2rad(rotation+90)
        X+=delta*0.8*math.cos(angled)
        Y+=delta*0.8*math.sin(angled)
    if keys[pygame.K_a]:
        anglea=np.deg2rad(rotation-90)
        X+=delta*0.8*math.cos(anglea)
        Y+=delta*0.8*math.sin(anglea)
    if rotation>360:
        rotation=0
    if rotation>0 and rotation<180:
       color=(200,200,200)
    else:
        color=(190,190,190)
    for i in range(field*2):
        xint=1
        yint=1
        posX=X
        posY=Y
        angle=rotation+i/2
        angle=np.deg2rad(angle)
        dx=delta*math.cos(angle)/5
        dy=delta*math.sin(angle)/5
        while mapping[xint][yint]==0:
            ##print(xint,yint,mapping[xint][yint])
            posX+=dx
            posY+=dy
            xint=int(posX/10)
            yint=int(posY/10)
        distanta=math.sqrt((posX-X)**2+(posY-Y)**2)
        inaltime= height*4/distanta
        distanta/=5
        fact=int(distanta)
        if fact<2:
            fact=2
        if fact>9:
            fact=9
        color=(abs(200/fact-fact),abs(150/fact-2*fact),abs(80/fact+1*fact))
        if mapping[xint][yint]==1:
            pygame.draw.rect(win,color,(view,height-300,width/60,inaltime),0)
            pygame.draw.rect(win,color,(view,height-300-inaltime+1,width/60,inaltime),0)
        if mapping[xint][yint]==2:
            pygame.draw.rect(win,color,(view,height-300,width/60,inaltime),0)
            pygame.draw.rect(win,color,(view,height-300-inaltime+1,width/60,inaltime),0)
        if mapping[xint][yint]==3:
            pygame.draw.rect(win,color,(view,height-300,width/60,inaltime),0)
            pygame.draw.rect(win,color,(view,height-300-inaltime+1,width/60,inaltime),0)    
            
        view+=10
    pygame.display.update() 
        
pygame.quit()
sys.exit()