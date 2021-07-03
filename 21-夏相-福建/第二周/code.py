import cv2
import numpy as np
def function(img):
    height,width,channels=img.shape
    emptylmage=np.zeros((800,800,channels),np.uint8)
    sh=800/height
    sw=800/width
    for i in range (800):
        for j in range(800):
            x=int(i/sh)
            y=int(j/sw)
            emptylmage[i,j]=img[x,y]
    return emptylmage

img=cv2.imread("lenna.png")
zoom=function(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest sharp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)