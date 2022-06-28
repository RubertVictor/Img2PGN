import cv2
import numpy as np
from scipy.spatial import distance
import os
from projectar import projecta
from PGNreader import read_PGN
from slicer import slice

#Img2PGN


#Obrim l'arxiu
dirname = os.path.dirname(__file__)
arxiu = '1654968224833'
name_jpg = 'Fotos planilles\\'+arxiu+'.jpg'
name_pgn = 'PGN\\'+arxiu+'.pgn'
filename_jpg = os.path.join(dirname,name_jpg)
filename_pgn = os.path.join(dirname,name_pgn)

ground_truth = read_PGN(filename_pgn)
planilla = projecta(filename_jpg)
jugades_img = slice(planilla)


print(planilla.shape)

cv2.imshow('Planilla',jugades_img[37-1])
cv2.waitKey()