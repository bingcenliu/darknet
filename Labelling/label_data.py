# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:36:07 2018

@author: jon
"""

import os
import cv2 as cv
import numpy as np
import shutil
import random
import easygui



# folder of images we want to label
data_folder=r'/home/jon/ObjectDetection/Label_Data/data_folder/'
#folder where labels will be saved
label_folder=r'/home/jon/ObjectDetection/Label_Data/label_folder/'
#folder where annoted images will be saved
annotated_folder=r'/home/jon/ObjectDetection/Label_Data/annotated_img/'
#folder where original imaged is moved to once annotated
final_folder=r'/home/jon/ObjectDetection/Label_Data/labeled_data/'

files=os.listdir(data_folder)
random.shuffle(files)

for file in files:
    print('Processing image : '+file)
    if file[-3:] == 'jpg':
        filename=file[:-3]
    else:
        filename=file[:-4]
    img=cv.imread(data_folder+file)
    boolDone=False
    print(data_folder+file[:-4]+'txt')
    fid=open(label_folder+filename+'txt','w')
    while not boolDone:
        cv.imshow('image',img)
        roi = cv.selectROI('image',img,False)
        if np.max(roi)>0:
            print(roi)
            x=np.round((float(roi[0])+(float(roi[2]))/2)/img.shape[1],2)
            y=np.round((float(roi[1])+(float(roi[3])/2))/img.shape[0],2)
            width=np.round(float(roi[2])/img.shape[1],2)
            height=np.round(float(roi[3])/img.shape[0],2)
        
            annClass=easygui.integerbox('What class? class 0 to quit', 'Class box',lowerbound=0,upperbound=100)
    
        
            if annClass==0:    
                boolDone=True
            else:
                fid.write(str(annClass-1)+' '+str(x)+' '+str(y)+' '+str(width)+' '+str(height)+'\n')
                if annClass==1:
                    cv.rectangle(img, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,255,0), 2)
                elif annClass==2:
                    cv.rectangle(img, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,255,255), 2)
                elif annClass==3:
                    cv.rectangle(img, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (0,0,255), 2)
                elif annClass==4:
                    cv.rectangle(img, (roi[0], roi[1]), (roi[0]+roi[2], roi[1]+roi[3]), (255,255,0), 2)
        else:
            boolDone=True
    fid.close()
    shutil.move(data_folder+file, final_folder+filename+'jpg')
    cv.imwrite(annotated_folder+filename+'jpg',img)

