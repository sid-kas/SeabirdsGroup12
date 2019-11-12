import cv2
import numpy as np 
from os.path import isfile, join
from os import listdir

mask = cv2.imread('mask.jpg')

PATH = '/data/Annotation/JPEGImages/'
PATH_new = '/data/Annotation/JPEGImages_masked/'


onlyfiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]

count=0
for name in onlyfiles:
   count+=1
   print(count)
   image = cv2.imread(PATH+name)
   image = image/255
   masked_image = np.multiply(image,mask)
   cv2.imwrite(PATH_new + name, masked_image)

