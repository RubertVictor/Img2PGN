import cv2
from projectar import projecta
import os


def slice(img):
    jugades = [0]*60
    altura_bn = 25
    altura = 26
    ample = int(img.shape[1]/2)
    for i in range(30):
        jugades[i] = img[altura_bn+altura*i:altura_bn+altura*(i+1),0:ample]
    for i in range(30):
        jugades[i+30] = img[altura_bn+altura*i:altura_bn+altura*(i+1),ample:2*ample]
    return jugades




if __name__=="__main__":
    dirname = os.path.dirname(__file__)

    name = 'Fotos planilles\\1654968224771.jpg'
    filename = os.path.join(dirname,name)

    img = projecta(filename)
    cv2.imshow('planilla sencera',img)
    jugades = slice(img)
    for i in range(14,18):
        cv2.imshow(str(i+1),jugades[i])
    cv2.waitKey()
       