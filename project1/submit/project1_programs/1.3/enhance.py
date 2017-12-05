"""
Code for COMP422 Project 1 Task 1.3: Image Enhancement
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


def laplacian_filter1(im):
    """Apply typical laplacian filter on the image"""
    k = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    g = convolve(im, k)
    return g

def laplacian_filter2(im):
    """Apply another laplacian filter on the image"""
    k = [[1, -2, 1], [-2, 5, -2], [1, -2, 1]]
    g = convolve(im, k)
    return g


def main():
    """ Gets the job done """
    im = scipy.misc.imread('blurry-moon.tif')
    im = im.astype('int32')
    mag = laplacian_filter1(im)
    scipy.misc.imsave('laplacianfilter1.jpg', mag)
    mag = laplacian_filter2(im)
    scipy.misc.imsave('laplacianfilter2.jpg', mag)
    
    
main()