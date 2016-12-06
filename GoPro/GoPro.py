from Naked.toolshed.shell import execute_js, muterun_js
import urllib2
import urllib
import time
import os
from PIL import Image

class GoPro(object):
	def __init__(self):
		# static variable that all GoPro instances share
		with open('./GoPro/imageNumber.txt') as f:
			GoPro.photo_number = int(f.read())

	def __del__(self):
		# writes a the new image number to a file so next time the instance can retrieve the correct photo from the GoPro server
                os.remove('./GoPro/imageNumber.txt')
                num = self.get_photo_number()
                string = str(num)
		f = open("./GoPro/imageNumber.txt","w")
                f.write(string)
                f.close()

        def get_photo_number(self):
                return self.photo_number
        
	def take_picture(self):
		# sends post request to go pro server to take a picture
		print("taking photo")
		url_response = urllib2.urlopen('http://localhost:8080?key=setRecordingOn&value=true')
		GoPro.photo_number = GoPro.photo_number + 1
		time.sleep(5)

	def download_photo(self):
		# sends get requets to go pro server to retrieve a photo
		imgLocation = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR00"+str(GoPro.photo_number)+".JPG"	
		#print imgLocation
		urllib.urlretrieve(imgLocation, "localPicture.jpg")
