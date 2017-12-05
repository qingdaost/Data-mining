"""
Code for COMP422 Project 1 Task 1.1: Edge Detection
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


def sobel_filter(im):
    """Apply Sobel edge detection operator on the image"""
    rowmask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    colmask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    
    row_result = convolve(im, rowmask)
    col_result = convolve(im, colmask)

    g = np.sqrt(row_result * row_result + col_result * col_result)

    return g


def main():
    """ Gets the job done """
    im = scipy.misc.imread('test-pattern.tif')   #Change the TIFF format of original image to numpy.ndarray in Python for further processing
    im = im.astype('int32')
    mag = sobel_filter(im)            #Convolution process
    mag[mag < 10] = 0                 #Apply thresholding to enhance the edge
    mag[mag >= 10] = 255    
    scipy.misc.imsave('sobel.jpg', mag)   #Save the processed image as jpg format
  
    
    
main()