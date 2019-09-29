import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter
im=Image.open('1111.png')


Lim=im.convert('L')

threshold=100
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
bim=Lim.point(table,'1')
bim.save('11111.png')
im=cv.imread('11111.png')
img=cv.resize(im,(28,28))
cv.imshow("1",img)
cv.waitKey(0)