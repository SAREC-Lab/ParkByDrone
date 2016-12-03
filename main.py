from imgRecognize import CVision
import math

###############
# Drone stuff #
###############

class location(object): # temp class, simulating the dronekit location one
	def __init__(self, lat, lon):
		self.latitude = lat
		self.longitude = lon

loc = location(4.12, 43.8)

vision = CVision('photos/target.JPG', 'photos/capture.png')
# TODO: what to do if none found?
lat, lon = vision.get_coordinates(10, loc)
print lat, lon
# drone fly to lat, lon

