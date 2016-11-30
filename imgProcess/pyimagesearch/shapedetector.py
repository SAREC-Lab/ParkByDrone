#import the neccesary package
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the countour 
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04* peri, True)

		# otherwise, we assume the shape is a circle
		if len(approx) > 7:
			shape = "circle"

		return shape

