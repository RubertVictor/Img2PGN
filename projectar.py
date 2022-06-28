import cv2
import numpy as np
from scipy.spatial import distance
import os



def projecta(filename):
    #llegim l'imatge
    img = cv2.imread(filename)

    #Tractam l'imatge per trobar el contorn més gran
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    contours, _  = cv2.findContours(thresh, cv2.RETR_TREE, cv2. CHAIN_APPROX_SIMPLE)


    max_area = 0
    c = 0
    for i in contours:
        area = cv2.contourArea(i)
        if(area> 100):
            if(area> max_area):
                max_area= area
                best_cnt = i
                cmax = c
                
        c+=1

    #Agafam els 4 punts més exteriors, per trobar els vèrtexos del rectangle
    x1 = np.max(best_cnt[:,0,0])
    y1 = np.max(best_cnt[:,0,1])
    x2 = np.min(best_cnt[:,0,0])
    y2 = np.min(best_cnt[:,0,1])

    def find_nearest(punt, array):
        min_dist=1000000
        for segon_punt in array:
            dist = distance.cityblock(punt, segon_punt)
            if(dist<min_dist):
                min_dist = dist
                min_punt = segon_punt
        return min_punt

    #trobam els vèrtexos del rectangle
    punt1 = find_nearest((x1,y1), contours[cmax])[0]
    punt2 = find_nearest((x1,y2), contours[cmax])[0]
    punt3 = find_nearest((x2,y1), contours[cmax])[0]
    punt4 = find_nearest((x2,y2), contours[cmax])[0]

    pts1 = np.float32([[punt4[0],punt4[1]], [punt2[0],punt2[1]], [punt3[0], punt3[1]], [punt1[0],punt1[1]]])
    pts2 = np.float32([[0,0],[650,0],[0,800],[650,800]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(img,M,(650,800))


    return dst
    #cv2.imwrite(filename, dst)
if __name__=="__main__":
    #Obrim l'arxiu
    dirname = os.path.dirname(__file__)

    scale_percent = 20

    name = 'Fotos planilles\\1654968224833.jpg'
    filename = os.path.join(dirname,name)
    resultat = projecta(filename)
    cv2.imshow('Name',resultat)
    
    gray = cv2.cvtColor(resultat, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    contours, _  = cv2.findContours(thresh, cv2.RETR_TREE, cv2. CHAIN_APPROX_SIMPLE)
    cv2.imshow('thresh', thresh)
    cv2.waitKey()