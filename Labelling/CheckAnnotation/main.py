# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:14:47 2018

@author: jon
"""
import cv2 as cv
from functions import checkAnnotation
import pathlib

#folders = [201,202,203]
folders = [1000]
for folder in folders:
    annotations = pathlib.Path().glob("../coordination/labels/%s/*.txt" % (folder))
    
    for annotation in annotations:  
        img_path  = "/home/jon/ObjectDetection/coordination/frames/%s/%s.jpg"%(folder, annotation.stem)
        txt_file = "/home/jon/ObjectDetection/coordination/labels/%s/%s.txt"%(folder, annotation.stem)
        final_img="/home/jon/ObjectDetection/coordination/verified_labels/%s/%s.jpg"%(folder, annotation.stem)
        img=cv.imread(img_path)
        print(img_path)
        with open(txt_file, "r") as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.rstrip()
        
       
            tokens = line.split()
            img=checkAnnotation(img,float(tokens[0]),float(tokens[1]),float(tokens[2]),float(tokens[3]),float(tokens[4]))
#img=checkAnnotation(img,0, 0.06406250000000001, 0.32708333333333334, 0.125, 0.24583333333333332)
#img=checkAnnotation(img,0, 0.22734375, 0.2708333333333333,0.060937500000000006, 0.06666666666666667)

        cv.imwrite(final_img,img)