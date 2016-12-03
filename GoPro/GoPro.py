class GoPro(object):
	def __init__(self):
		# static variable that all GoPro instances share
		with open('imageNumber.txt') as f:
			GoPro.photo_number = f.read()

	def take_picture(self):
		print("taking photo")
		url_response = urllib2.urlopen('http://localhost:8080?key=setRecordingOn&value=true')
		GoPro.photo_number = GoPro.photo_number + 1
		time.sleep(5)

	def download_photo(self):
		urllib.urlretrieve("http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR00 {} .JPG".format(GoPro.photo_number), "localPicture.jpg")

	def close(self):
		with open('imageNumber.txt') as f:
			f.seek(0)
			f.write(GoPro.photo_number)
