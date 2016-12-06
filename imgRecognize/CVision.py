########################################################
# Author: Robert Simari                                #
#   Purpose: uses template matching in cv2 to find a   #
#            picture inside another picture and return #
#            the coordinates.                          #
########################################################

import imutils
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import sys
import os
# import math

# Example use: python CVision.py small.jpg find.JPG

class CVision(object):
    def __init__(self, image = None, template = None):
        self.image = None
        self.template = None
        self.width = None
        self.height = None
        self.plot = False
        self.image_str = image
        self.template_str = template
        self.set_image(image)
        self.set_template(template)
        # self.methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        self.methods = ['cv2.TM_CCOEFF']

    def __del__(self):
        pass

    def set_image(self, image, gray = True):
        # so the interface can change the images
        if image is not None and os.path.isfile(image):
            if gray:
                self.image = cv2.imread(image, 0)
            else:
                self.image = cv2.imread(image)
        elif image is not None:
            print "Error: {} not image found".format(image)
            # exit(1)

    def set_template(self, template, gray = True):
        # so the interface can change the template
        if template is not None and os.path.isfile(template):
            if gray:
                self.template = cv2.imread(template, 0)
            else:
                self.template = cv2.imread(template)
            imutils.resize(self.template, width = 300)
            self.width, self.height = self.template.shape[:2]
        elif template is not None:
            print "Error: {} not image found".format(template)
            # exit(1)


    def find_image(self, image = None):
        if image is not None:
            self.set_image(image, gray = True)
        if image is None and self.image is None:
            return -1, -1 # return nothing
        # preps image to make it easier to use
        self.save_image(self.prep_image(), name = 'temp.png')
        self.set_image('temp.png', gray = False)
        self.set_template(self.template_str, gray = False)

        for m in self.methods:
            tl, br = self.use_method(m)
            # remove temp photo temp.png
            os.remove('temp.png')
        # if picture is found
        if tl[0] is not 0 and tl[1] is not 0:
            return tl
        pic_width, pic_height = self.get_image_size()
        # if no picture is found then return the center of image
        return pic_width/2, pic_height/2

    def use_method(self, meth):
        method = eval(meth)
        # Apply template Matching
        res = cv2.matchTemplate(self.image, self.template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_CCOEFF]:
            top_left = max_loc
            bottom_right = top_left
        else:
            bottom_right = (top_left[0] + self.width, top_left[1] + self.height)

        # plot result if self.plot is set to True
        if self.plot:
            # show rectangle of where the target is 
            cv2.rectangle(res, top_left, bottom_right, (0,200,50), 5)
            plt.subplot(121), plt.imshow(res)
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(self.image)
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()

        print top_left, bottom_right
        return top_left, bottom_right

    def prep_image(self):
        copy = cv2.imread(self.image_str)
        # Convert input image to HSV
        hsv_image = cv2.cvtColor(copy, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        blueMask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(copy,copy, mask= blueMask)
        return result

    def save_image(self, image, name = 'temp.png'):
        # saves image to a file, default named temp.png
        if image is not None:
            cv2.imwrite(name, image)

    def get_image_size(self):
        # returns the width, height of self.image
        if self.image is None:
            return -1,-1
        return self.image.shape[:2]

    def get_coordinates(self, height, current_location):
        pic_height, pic_width = self.get_image_size()
        self.plot = True
        x,y = self.find_image()
        # now convert from m to degrees
        dw = self.get_dwidth(height, pic_width, x) / 1.113195e5
        dh = self.get_dheight(height, pic_height, y) / 1.113195e5
        return current_location.lat + dh, current_location.lon + dw

    def get_dwidth(self, height, pic_width, x):
        # uses FOV angle to find the real life distance of half the picture
        # opp = math.tan(118.2 / 2 * math.pi / 180.0) * height 
        opp = 1.670878244512379 * height
        # ratio of real life to picture
        ratio = 2.0 * opp / pic_width 
        # center of picture in pixels
        center = pic_width / 2
        # difference between found spot and center of picture
        dw = x - center
        # returns the actual horizontal distance from found target
        return dw * ratio

    def get_dheight(self, height, pic_height, y):
        # uses FOV angle to find the real life distance of half the picture
        # opp = math.tan(69.5 / 2 * math.pi / 180.0) * height 
        opp = 0.693724684259 * height
        # ratio of real life to picture
        ratio = 2.0 * opp / pic_height
        # center of picture in pixels
        center = pic_height / 2
        # difference between found spot and center of picture
        dh = y - center
        # returns the actual vertical distance from found target
        return dh * ratio

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage: python CVision.py template target"
        exit(1)
    vision = CVision(sys.argv[1], sys.argv[2])
    print vision.find_image()

