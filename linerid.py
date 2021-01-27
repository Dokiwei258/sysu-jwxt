import cv2
import numpy as np
def getridofline(path):
    im = cv2.imread(path,1)
    h, w, k = im.shape
    r, g, b = cv2.split(im)
    for x in range(1, h):
        for y in range(1, w):
            if r[x, y] * g[x, y] * b[x, y] < 1:
                r[x, y] = 255
                g[x, y] = 255
                b[x, y] = 255
    im = cv2.merge([r, g, b])
    im=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret,im = cv2.threshold(im,200,255,cv2.THRESH_BINARY)
    kernel = 1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
    im = cv2.filter2D(im,-1,kernel)
    ret, im = cv2.threshold(im, 190, 255, cv2.THRESH_BINARY)
    for y in range(1,w-1):
        for x in range(1,h-1):
            count=0
            if im[x,y-1]>200:
                count=count+1
            if im[x-1,y-1]>200:
                count=count+1
            if im[x+1,y+1]>200:
                count=count+1
            if im[x-1,y+1]>200:
                count=count+1
            if im[x+1,y-1]>200:
                count=count+1
            if im[x,y+1]>200:
                count=count+1
            if im[x-1,y]>200:
                count=count+1
            if im[x+1,y]>200:
                count=count+1
            if count>5:
                im[x,y]=255
    return im