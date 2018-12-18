# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:04:23 2018

@author: jon
"""

import cv2 as cv

def checkAnnotation(img,anClass,x,y,w,h):

    coor_1=[int((x-w*0.5)*img.shape[1]),int((y-h*0.5)*img.shape[0])]
    coor_2=[int((x+w*0.5)*img.shape[1]),int((y+h*0.5)*img.shape[0])]
    if anClass==0:
        cv.rectangle(img, (coor_1[0], coor_1[1]), (coor_2[0], coor_2[1]),(0,255,0), 2)
    elif anClass==1:
        cv.rectangle(img, (coor_1[0], coor_1[1]), (coor_2[0], coor_2[1]),(0,255,255), 2)
    elif anClass==2:
        cv.rectangle(img, (coor_1[0], coor_1[1]), (coor_2[0], coor_2[1]),(0,0,255), 2)
    elif anClass==3:
        cv.rectangle(img, (coor_1[0], coor_1[1]), (coor_2[0], coor_2[1]),(255,255,0), 2)
    return img