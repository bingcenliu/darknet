# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:14:47 2018

@author: jon
"""
import cv2 as cv
from functions import checkAnnotation
import pathlib
import argparse
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description="Visually check label of images")
    parser.add_argument("inputImage", help="Path of image to check", type=str)
    parser.add_argument("inputLabel", help="Path of label to check", type=str)

    args = parser.parse_args()

    img_path = Path(args.inputImage)
    txt_file = Path(args.inputLabel)

    if not img_path.is_file():
        print("{} is not a file".format(img_path))
        sys.exit(1)

    if not txt_file.is_file():
        print("{} is not a file".format(txt_file))
        sys.exit(1)    
    
    
    
    img=cv.imread(img_path)
    with open(txt_file, "r") as f:
        lines = f.readlines()
            
    for line in lines:
        line = line.rstrip()
        tokens = line.split()
        img=checkAnnotation(img,float(tokens[0]),float(tokens[1]),float(tokens[2]),float(tokens[3]),float(tokens[4]))
    #cv.imwrite(final_img,img)
            
if __name__ == "__main__":
    main()