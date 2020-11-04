import urllib.request
from cv2 import cv2
import numpy as np
import time



URL = "Camera-Ip-Address-Link-here"     #I used the IP Webcam for the camera needs Any video Cam can be used



mycolors= [0, 145, 189, 8,204, 255]            #Need to add different values for specific color tracing[hue_min, sat_min, val_min, hue_max, sat_max, val_max]. Find the values using test1.py

mypoints= []
newpoints=[]

def findcolor(img, mycolors):
    imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    lower= np.array(mycolors[0:3])
    upper= np.array(mycolors[3:6])

    mask= cv2.inRange(imgHSV,lower,upper)
    x,y= getContours(mask)
    x1 = int(x)
    if(x!=0):
       cv2.circle(imgResult,(x1+448,y),20,(0,0,255),cv2.FILLED)
    else:
       cv2.circle(imgResult,(x1,y),20,(0,0,255),cv2.FILLED)

    if x!=0 and y!=0 :
        newpoints.append([x,y])
    
    return newpoints
    
    #cv2.imshow('IPWebcam',mask)


def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h= 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area>500):
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri= cv2.arcLength(cnt,True)
            approx= cv2.approxPolyDP(cnt,0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return (x+w)//2, y


def drawLine(mypoints):
    for point in mypoints:
        cv2.circle(imgResult,(point[0]+450,point[1]),20,(0,0,255),cv2.FILLED)




while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    imgResult= img.copy()
    newpoints= findcolor(img, mycolors)
    if len(newpoints)!=0 :
        for n in newpoints:
            mypoints.append(n)
    if len(mypoints)!=0:
        drawLine(mypoints)

    cv2.imshow('Final',imgResult)
    

    
    
    cv2.waitKey(1)
    
        