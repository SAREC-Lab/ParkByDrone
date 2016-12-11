from imgRecognize import CVision
from GoPro import GoPro
import os
#Take a picture using the GoPro

camera = GoPro()

camera.take_picture()

camera.download_photo()

if not os.path.isfile('localPicture.jpg'):
    print "Error: Image not downloaded"
    exit(1)
vision = CVision('localPicture.jpg', './photos/target.JPG')
vision.find_image()
