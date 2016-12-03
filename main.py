from imgRecognize import CVision
import math

###############
# Drone stuff #
###############

def get_coordinates(height, current_location):
	vision = CVision('photos/target.JPG', 'photos/capture.png')
	pic_height, pic_width = vision.get_image_size()
	vision.plot = True
	x,y = vision.find_image()
	# now convert from m to degrees
	dw = get_dwidth(height, pic_width, x[0]) / 1.113195e5
	dh = get_dheight(height, pic_height, x[1]) / 1.113195e5
	return current_location.latitude + dw, current_location.longitude + dh


def get_dwidth(height, pic_width, x):
	# uses FOV angle to find the real life distance of half the picture
	opp = math.tan(118.2 * 2 * math.pi) * height 
	# ratio of real life to picture
	ratio = 2 * opp / pic_width 
	# center of picture in pixels
	center = pic_width / 2
	# difference between found spot and center of picture
	dw = x - center
	# returns the actual horizontal distance from found target
	return dw * ratio

def get_dheight(height, pic_height, y):
	# uses FOV angle to find the real life distance of half the picture
	opp = math.tan(69.5 * 2 * math.pi) * height 
	# ratio of real life to picture
	ratio = 2 * opp / pic_height
	# center of picture in pixels
	center = pic_height / 2
	# difference between found spot and center of picture
	dh = y - center
	# returns the actual vertical distance from found target
	return dh * ratio

class location(object):
	def __init__(self, lat, lon):
		self.latitude = lat
		self.longitude = lon

loc = location(4.12, 43.8)
print get_coordinates(10, loc)

