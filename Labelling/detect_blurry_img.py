# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:55:11 2018

@author: jon
"""
import cv2 as cv
import os


# detect if iamge is blurry

#folder infos
dataFolder=r"/home/jon/ObjectDetection/coordination/frames/204/"
sub='204_'
#dataFolder=r"/home/jon/ObjectDetection/Blurry/DataFolder/"
blurryFolder=r"/home/jon/ObjectDetection/Blurry/Blurry/"
goodFolder=r"/home/jon/ObjectDetection/Blurry/Not_Blurry/"

#threshold
threshold=200

#go through all images in data folder
for file in os.listdir(dataFolder):
    print('Processing image : '+file)
    imageFile=dataFolder+file
    
    image = cv.imread(imageFile)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    fm = cv.Laplacian(gray, cv.CV_64F).var()
#    print(file)
#    print('\t'+str(fm))
    if fm<threshold:
        #blurry
        cv.imwrite(blurryFolder+sub+file,image)
    else:
        #not blurry
        cv.imwrite(goodFolder+sub+file,image)