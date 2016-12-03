from imgRecognize import CVision
# from GoPro import GoPro
import math

###############
# Drone stuff #
###############

class location(object): # temp class, simulating the dronekit location one
	def __init__(self, lat, lon):
		self.latitude = lat
		self.longitude = lon

loc = location(4.12, 43.8)
height = 10

# go pro
# go = GoPro()
# go.take_picture()
# go.download_photo()

vision = CVision('./photos/capture.png', './photos/target.JPG')
lat, lon = vision.get_coordinates(height, loc) # pass in vehicle.location
print lat, lon

if lat is loc.latitude and lon is loc.longitude:
	pass
	# keep flying like it was (not found)

# drone fly to lat, lon
