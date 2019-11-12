import cv2
import numpy as np 

dw = 1920
dh = 1080


image ='/data/Annotation/AnnotationImagesSeabirds/Farallon3_20190605_124725_No002.jpg'
labels  ='/data/Annotation/yolo_annotations/Farallon3_20190605_124725_No002.txt'

label_data = open(labels)
im = cv2.imread(image)
print(im)
for line in label_data:
    x=float(line.split(' ')[1])*dw
    y=float(line.split(' ')[2])*dh
    w=float(line.split(' ')[3])*dw
    h=float(line.split(' ')[4])*dh
    out = cv2.rectangle(im, (int(x-w/2),int(y-h/2)) ,(int(x+w/2),int(y+h/2)), (0,0,255), 2)
 
cv2.imwrite('/data/Annotation/test.jpg',out) 
    

