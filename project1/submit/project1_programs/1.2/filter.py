"""
Code for COMP422 Project 1 Task 1.2: Noise Cancellation
Author: Shi Tao, student number: 300409943
"""

import numpy as np
import scipy.signal


def convolve(im, mask):
    """Convolution process"""
    y, x = im.shape
    y = y - 2
    x = x - 2
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(im[i:i+3, j:j+3] * mask)
    return new_image


def mean_filter(im):
    """Apply mean filter on the image"""
    k = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
    g = convolve(im, k)
    return g

def median_filter(im):
    """Apply median filter on the image"""
    y, x = im.shape
    y = y - 2
    x = x - 2
    new_image = np.zeros((y,x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.median(im[i:i+3, j:j+3])
    return new_image

def main():
    """ Gets the job done """
    im = scipy.misc.imread('ckt-board-saltpep.tif')
    im = im.astype('int32')
    mag = mean_filter(im)
    scipy.misc.imsave('meanfilter.jpg', mag)
    mag = median_filter(im)
    scipy.misc.imsave('medianfilter.jpg', mag)
    
    
main()