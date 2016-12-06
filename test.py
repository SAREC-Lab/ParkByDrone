import unittest
from matplotlib import pyplot as plt 
import cv2
from imgRecognize import CVision

# usage: python test.py -v

class VisionTest(unittest.TestCase):
	def test_constructor(self):
		vision = CVision()
		self.assertEqual(vision.image, None)
		self.assertEqual(vision.template, None)

		vision = CVision('photos/orange.png', 'photos/find.JPG')
		self.assertEqual(vision.image_str, 'photos/orange.png')
		self.assertEqual(vision.template_str, 'photos/find.JPG')

	def test_set_image(self):
		vision = CVision()
		vision.set_image('photos/orange2.jpg', gray = True)
		self.assertEqual(vision.image.all(), cv2.imread('photos/orange2.jpg', 0).all())

		vision = CVision('photos/orange.png', 'photos/find.JPG')
		vision.set_image('photos/small.jpg', gray = True)
		self.assertEqual(vision.image.all(), cv2.imread('photos/small.jpg', 0).all())

	def test_set_template(self):
		vision = CVision()
		vision.set_template('photos/orange2.jpg', gray = True)
		self.assertEqual(vision.template.all(), cv2.imread('photos/orange2.jpg', 0).all())

		vision = CVision('photos/orange.png', 'photos/find.JPG')
		vision.set_template('photos/small.jpg', gray = True)
		self.assertEqual(vision.template.all(), cv2.imread('photos/small.jpg', 0).all())

	def test_find_image(self):
		vision = CVision('photos/small.jpg', 'photos/find.JPG')
		x,y = vision.find_image()
		self.assertIsNotNone(x)
		self.assertIsNotNone(y)

	def test_get_coordinates(self):
		pass
		# TODO: write this test

if __name__ == "__main__":
	unittest.main()