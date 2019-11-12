import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import json

classes = ["AdultBird","Chick","Egg"]

DATA_DIR="/data/Annotation/"
# Width and height of the image 
w = 1920
h = 1080

# Read the csv file
data = open('/data/Annotation/data.csv')

# Writing all the names of the images to a list file
list_file = open("/data/Annotation/dataset.txt",'w')


count=0

def convert_annotation(a, image_id,size):
    image = image_name.split('.')[0]
    out_file = open(DATA_DIR+"labels/%s.txt" %(image),'w')
    objects = a['objects']
    for obj in objects:
        cls = obj['type']
        cls_id = classes.index(cls)
        if len(obj['boundaries'])==0:
           continue
        m = obj['boundaries'][0]
        for p in m['boundaryPoints']:
           loc=p['edge'].rstrip('\n')
           if loc ==  "Bottom":
                x_b,y_b = p['coords']
           elif loc ==  "Top":
                x_t,y_t = p['coords']
           elif loc == "Right":
                x_r,y_r = p['coords']
           elif loc ==  "Left":
                x_l,y_l = p['coords']
                
        #convert to yolo annotation
        dw = 1./size[0]
        dh = 1./size[1]
        x = (x_r + x_l)/2.0            
        y = (y_t + y_b)/2.0            
        x =  x*dw
        w = (x_r-x_l)*dw
        y = y*dh
        h = (y_t-y_b)*dh
        bb = (x,y,w,h)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
 
    out_file.close()
    
        
# traverse through each line
for line in data:
    if "annotation" in line:
        continue
    image_name = line.split(',',1)[0].strip()
    annotation = line.split(',',1)[1].strip()
    image_file = DATA_DIR +"JPEGImages/"+ image_name +'\n'
    if os.path.exists(image_file.strip()):
        list_file.write(image_file)
    else:
        count=count+1
        print(str(count) +"  " +image_file.strip())

    annotation = annotation.replace('\\"',"\"")
    jstr = json.loads(annotation)
    convert_annotation(jstr, image_name,[w,h])
        
list_file.close()
