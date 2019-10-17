import cv2
import numpy as np

def mouse_click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        for i in range (1,height-1):
            for j in range (1,width-1):
                if (i==x and j==y):
                    print img[i,j]
                    break

img=cv2.imread('color-theory.jpg',1)
height = np.size(img, 0)
width = np.size(img, 1)


cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_click)
cv2.imshow('image',img)
cv2.waitKey(0)

    
        
