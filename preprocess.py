import os
import numpy as np
import nibabel as nib
from scipy import ndimage


class ProcessScan():
    def __init__(self):
        pass

    # Read the nifti file
    def read_nifti(self, filename):
        scan = nib.load(filename)
        scan = scan.get_fdata()
        return scan

    # Normalize the scan
    def normalize(self, volume):
        min=-1000
        max=400
        volume[volume<min] = min
        volume[volume>max] = max
        volume = (volume - min)/(max - min)
        volume = volume.astype("float32")
        return volume

    # Resize the volume of the scan
    def resize_volume(self, img):
        d_depth = 64
        d_height = 128
        d_width = 128
        c_depth = img.shape[-1]
        c_height = img.shape[1]
        c_width = img.shape[0]

        depth = c_depth/d_depth
        height = c_height/d_height
        width = c_width/d_width

        depth_factor = 1/depth
        height_factor = 1/height
        width_factor = 1/width

        img = ndimage.rotate(img, 90, reshape=False)
        # Resize along the z axis
        img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=1)

        return img

    # Process the scan
    def process_scan(self, path):
        volume = self.read_nifti(path)
        volume = self.normalize(volume)
        volume = self.resize_volume(volume)
        return volume