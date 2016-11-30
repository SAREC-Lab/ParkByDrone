import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import sys
# from pyimagesearch.shapedetector import ShapeDetector


class CVision(object):
	def __init__(self, image = None, template = None):
		self.image = None
		self.image2 = None
		self.template = None
		self.width = None
		self.height = None
		self.plot = False
		self.set_image(image)
		self.set_template(template)
		# self.methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
		self.methods = ['cv2.TM_CCOEFF']

	def set_image(self, image):
		# so the interface can change the images
		if self.image is None:
			self.image = cv2.imread(image,0)
			self.image2 = self.image.copy()

	def set_template(self, template):
		# so the interface can change the template
		if self.template is None:
			self.template = cv2.imread(template,0)
			self.width, self.height = self.template.shape[::-1]

	def find_image(self, image = None):
		if image is None:
			self.set_image(image)
		for m in self.methods:
			# self.image = self.image2.copy()
			tl, br = self.use_method(m)
			print tl, br

	def use_method(self, meth):
		method = eval(meth)
		# Apply template Matching
		res = cv2.matchTemplate(self.image, self.template, 4)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
		if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
			top_left = min_loc
		else:
			top_left = max_loc
		bottom_right = (top_left[0] + self.width, top_left[1] + self.height)
		# plot result if self.plot is set to True
		if self.plot:
			# show rectangle of where the target is 
			cv2.rectangle(self.image, top_left, bottom_right, (0,200,50), 10)
			plt.subplot(121),plt.imshow(res,cmap = 'gray')
			plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
			plt.subplot(122),plt.imshow(self.image,cmap = 'gray')
			plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
			plt.suptitle(meth)
			plt.show()

		return top_left, bottom_right
		
if __name__ == "__main__":
	vision = CVision(sys.argv[1], sys.argv[2])
	# vision.plot = False
	vision.find_image()
