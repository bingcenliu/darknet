# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:55:11 2018

@author: jon
"""
import cv2 as cv
import os
import argparse


# detect if iamge is blurry
def main():
    
    parser = argparse.ArgumentParser(description="Eliminate blurry pictures")
    parser.add_argument("inputFolder", help="Path of folder containing images to classify", type=str)
    parser.add_argument("blurryFolder", help="Path of folder where blurry images will be sent", type=str)
    parser.add_argument("notBlurryFolder", help="Path of folder where non blurry images will be sent", type=str)
    parser.add_argument("threshold", help="Threshold for blurry detection, default is 200", type=int, default = 200)

    args = parser.parse_args()

    input_embs = args.embeddings
    vocab_file = args.vocab
    output_embs = args.output_embeddings
    #folder infos
    dataFolder=args.inputFolder
    #dataFolder=r"/home/jon/ObjectDetection/Blurry/DataFolder/"
    blurryFolder=args.blurryFolder
    goodFolder=args.notBlurryFolder
    
    #threshold
    threshold=args.threshold
    
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

if __name__ == "__main__":
    main()