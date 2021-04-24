import sys
import unittest
sys.path.append('..')
from ImageManipulation.Imgmanip import Imagemanip

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'

class test_Imgmanip(unittest.TestCase):

    def test_img_object (self):
        """ Assert that the image object is created """
        img = Imagemanip(url)
        self.assertIsInstance(img, Imagemanip)

    def test_thresh_val (self):
        """ Assert that the threshold value is between 0 and 255 """
        img = Imagemanip(url)
        img.single_color()
        img.convert_binary(scale=3, thresh_val=200)
        self.assertGreater(img.thresh_val, 0) # thresh_val > 0
        self.assertLess(img.thresh_val, 255) # thresh_val < 255