from imgRecognize import CVision
# from GoPro import GoPro
# from dronekit import connect,VehicleMode, LocationGlobalRelative, time
import os

class Location(object):
	def __init__(self, lat, lon, h):
		self.lat = lat
		self.lon = lon
		self.height = h
# go = GoPro()
# if os.path.isfile('./localPicture.png'):
# 	os.remove('./localPicture.png')	
# go.take_picture()
# Dowloads into the file "localPicture.png"
# go.download_photo()
#######################################################################$
# Pass Photo To Image Recognition
#######################################################################$
# if not os.path.isfile('localPicture.jpg'):
# 	print "Error: image not downloaded correctly"
# 	exit(1)
vision = CVision('./imgProcess/testParkingLot.png', './photos/target.JPG')
# test = LocationGlobalRelative(41.000,42.000,0)
test = Location(41.00, 42.00, 0)
print vision.get_coordinates(30, test)

# open_spot_location = LocationGlobalRelative(lat, lon, 10)

