# import the necessary packages

from pyimagesearch.shapedetector import ShapeDetector

import argparse

import imutils

import cv2
import numpy as np

 

# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,

	help="path to the input image")

args = vars(ap.parse_args())


# load the image and resize it to a smaller factor so that

# the shapes can be approximated better

image = cv2.imread(args["image"])

resized = imutils.resize(image, width=300)

ratio = image.shape[0] / float(resized.shape[0])

# Convert input image to HSV
print image
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
blueMask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image,image, mask= blueMask)

cv2.imshow('image',image)
cv2.imshow('blueMask',blueMask)
cv2.imshow('result',result)
cv2.waitKey(0)
