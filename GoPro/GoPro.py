class GoPro(object):
	def __init__(self):
		pass

	def take_picture(self):
		print("taking photo")
		url_response = urllib2.urlopen('http://localhost:8080?key=setRecordingOn&value=true')
		time.sleep(5)

	def download_photo(self):
		photo_number = 52
		urllib.urlretrieve("http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR00 {} .JPG".format(photo_number), "localPicture.jpg")

