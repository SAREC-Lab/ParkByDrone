from Naked.toolshed.shell import execute_js, muterun_js
import urllib2
import urllib
import time
from PIL import Image
#success = execute_js('takePhoto.js')
#print("turning camera on")
#url_response = urllib2.urlopen('http://10.13.226.157:8080?key=setCameraOn&value=true')
#time.sleep(5)

#print("setting camera mode")
#url_response = urllib2.urlopen('http://localhost:8080?key=setCameraMode&value=photo')
#time.sleep(5)

print("taking photo")
url_response = urllib2.urlopen('http://localhost:8080?key=setRecordingOn&value=true')
time.sleep(5)

urllib.urlretrieve("http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR0052.JPG", "localPicutre.jpg")


#photoFile = urllib2.urlopen('http://localhost:8080?key=getLastCapturedMediaItem')
#image = urllib2.urlopen('http://localhost:8080?key=downloadMediaFromCamera&value=photoFile')

#print (photoFile)
#print (image)

#print("photo downloaded")

#img = Image.open(image)
#img.show()

print("done")

