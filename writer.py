import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2 as cv
import os
from random import randint, uniform, choice,gauss
from os.path import basename
from math import floor
from matplotlib import pyplot as plt

#load path
path='/home/oumaima/Pictures/'


    # load images
for pic in os.listdir(path):
   #read image
   img = cv.imread(path+pic)

   #get shape
   height, weight, channels = img.shape

   # Create a white image
   img_white = np.zeros((height, weight, 3), np.uint8)
   img_white[:] = (255, 255, 255)

   # list of fonts
   list=[cv.FONT_HERSHEY_SIMPLEX, cv.FONT_HERSHEY_PLAIN, cv.FONT_HERSHEY_SIMPLEX, cv.FONT_HERSHEY_DUPLEX, cv.FONT_HERSHEY_COMPLEX,cv.FONT_HERSHEY_SIMPLEX, cv.FONT_HERSHEY_TRIPLEX, cv.FONT_HERSHEY_COMPLEX_SMALL,cv.FONT_HERSHEY_SCRIPT_SIMPLEX,  cv.FONT_HERSHEY_SCRIPT_COMPLEX]

   #Localization of text
   bottom=randint(50,height-50)
   left=randint(0,weight-50)

   #text caracteristics
   font = choice(list)
   fontScale =uniform(0.3, 6.5)
   lineType = randint(1, 5)

   #random color
   u = gauss(0, 1)
   v = gauss(0, 1)
   z = gauss(0, 1)

   R=abs(int(40*u))
   G=abs(int(30*v))
   B=abs(int(30*z))

   fontColor = (R, G, B)


   #number of lines
   nb_lines=randint(1,5)

   #in case of little image apply an average fontscale
   if height < 200:
       fontScale = uniform(0.3, 3.5)

   #foreach line
   for j in range(1, nb_lines):
    #choose a text
    words = open('/etc/dictionaries-common/words').read().splitlines()

    line=""
    while line=="":
     for k in range(1,randint(1,4)):
       x=choice(words)
       line += x+" "


    #for visibility of text
    if (fontScale < 1):
        lineType = 1

    bottomLeftCornerOfText = (left, bottom)

    #write the text
    cv.putText(img, line,
               bottomLeftCornerOfText,
               font,
               fontScale,
               fontColor,
               lineType)

    cv.putText(img_white, line,
               bottomLeftCornerOfText,
               font,
               fontScale,
               fontColor,
               lineType)

    #create a directory to hold data_set
    if not os.path.exists("data_set_directory"):
        os.makedirs("data_set_directory")

    #name of image without the extension
    img_name = basename("/a/b/c"+os.path.splitext(path+pic)[0])

    #save image
    cv.imwrite("data_set_directory/"+ img_name +".jpg", img)
    cv.imwrite("data_set_directory/"+ img_name + "_out_white.jpg", img_white)

    #for next line
    if(nb_lines>1) :
       # load image to write next line
       img = cv.imread("data_set_directory/" + img_name + ".jpg")
       img_white = cv.imread("data_set_directory/" + img_name + "_out_white.jpg")

       #make space between lines
       if(fontScale<4):
         bottom=bottom+90

       else:
           bottom=bottom+120


       if (bottom>height-90):
            break

    #blurImg = cv.blur(img, (3, 3))  # You can change the kernel size as you want
    #cv.imshow('blurred image', blurImg)
    #cv.imwrite("data_set_directory/" + img_name + "new.jpg", img)

cv.waitKey(0)
