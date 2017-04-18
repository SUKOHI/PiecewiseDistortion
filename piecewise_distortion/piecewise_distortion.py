import numpy as np
import skimage.transform
from PIL import Image

class PiecewiseDistortion:

    roi_points = []

    def __init__(self, roi_points):
        self.roi_points = roi_points

    def get_distorted_image(self, pil_im, from_points, to_points):
        pil_im = pil_im.convert('RGBA')
    	from_points = np.concatenate((self.roi_points, from_points))
    	to_points = np.concatenate((self.roi_points, to_points))
    	affin = skimage.transform.PiecewiseAffineTransform()
    	affin.estimate(to_points, from_points)
    	im_array = skimage.transform.warp(pil_im, affin)
    	im_array = np.array(im_array * 255., dtype=np.uint8)

    	if im_array.shape[2] == 1:
    		im_array = im_array.reshape((im_array.shape[0],im_array.shape[1]))

    	warped_im = Image.fromarray(im_array, 'RGBA')
    	pil_im.paste(warped_im, (0, 0), warped_im)
    	return pil_im
