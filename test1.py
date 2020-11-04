import urllib.request
from cv2 import cv2
import numpy as np
import time
URL = "Camera_IPAddress_link_here"



cap= cv2.VideoCapture(0)

cap.set(10,3)

def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640,240)
cv2.createTrackbar("Hue Min","Trackbars",119,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)




while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    
    
    h_min= cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max= cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min= cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max= cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min= cv2.getTrackbarPos("Val Min","Trackbars")
    v_max= cv2.getTrackbarPos("Val Max","Trackbars")

    lower= np.array([h_min, s_min, v_min])
    upper= np.array([h_max, s_max, v_max])

    mask= cv2.inRange(imgHSV,lower,upper)
    final_img = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("video", mask)
    cv2.waitKey(1)


