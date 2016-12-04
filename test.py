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

		vision = CVision('imgRecognize/orange.png', 'imgRecognize/find.JPG')
		self.assertEqual(vision.image_str, 'imgRecognize/orange.png')
		self.assertEqual(vision.template_str, 'imgRecognize/find.JPG')

	def test_set_image(self):
		vision = CVision()
		vision.set_image('imgRecognize/orange2.jpg')
		self.assertEqual(vision.image.all(), cv2.imread('imgRecognize/orange2.jpg', 0).all())

		vision = CVision('imgRecognize/orange.png', 'imgRecognize/find.JPG')
		vision.set_image('imgRecognize/small.jpg')
		self.assertEqual(vision.image.all(), cv2.imread('imgRecognize/small.jpg', 0).all())

	def test_set_template(self):
		vision = CVision()
		vision.set_template('imgRecognize/orange2.jpg')
		self.assertEqual(vision.template.all(), cv2.imread('imgRecognize/orange2.jpg', 0).all())

		vision = CVision('imgRecognize/orange.png', 'imgRecognize/find.JPG')
		vision.set_template('imgRecognize/small.jpg')
		self.assertEqual(vision.template.all(), cv2.imread('imgRecognize/small.jpg', 0).all())

	def test_find_image(self):
		vision = CVision('imgRecognize/small.jpg', 'imgRecognize/find.JPG')
		x,y = vision.find_image()
		self.assertIsNotNone(x)
		self.assertIsNotNone(y)


if __name__ == "__main__":
	unittest.main()