"""
Code for COMP422 Project 1 Task 2.1: Mining Space Images
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


def mean_filter1(im):
    """Apply mean filter on the image"""
    k = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
    g = convolve(im, k)
    return g


def mean_filter2(im):
    """Apply mean filter on the image"""
    k = [[1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25], 
         [1/25, 1/25, 1/25, 1/25, 1/25]]
    g = scipy.signal.convolve2d(im, k, mode='same', boundary = 'symm', fillvalue=0)
    return g



def thresholding(im, threshold):
    """Apply thresholding to generate binary image"""
    im[im < threshold] = 0
    im[im >= threshold] = 1
    return im

def main():
    """ Gets the job done """
    im = scipy.misc.imread('hubble.tif')
    im = im.astype('int32')
    
    mag0 = mean_filter1(im)
    scipy.misc.imsave('map.jpg', mag0)    #smooth the image by 3*3 mask
    
    mag4 = mean_filter2(im)
    scipy.misc.imsave('map1.jpg', mag4)    #smooth the image by 5*5 mask   
    
    mag1 = mean_filter1(im)
    map50 = thresholding(mag1, 50)
    scipy.misc.imsave('map50.jpg', map50)    #after 3*3 mask and set threshold as 50
    
    mag2 = mean_filter1(im)
    map100 = thresholding(mag2, 100)
    scipy.misc.imsave('map100.jpg', map100)    #after 3*3 mask and set threshold as 100  
    
    mag3 = mean_filter1(im)
    map200 = thresholding(mag3, 200)
    scipy.misc.imsave('map200.jpg', map200)    #after 3*3 mask and set threshold as 200
    
    map200_ws = thresholding(im, 200)
    scipy.misc.imsave('map200ws.jpg', map200_ws)    #without smoothing and set threshold as 200
    
    map200_bm = thresholding(mag4, 200)
    scipy.misc.imsave('map200bm.jpg', map200_bm)    #after 5*5 mask and set threshold as 200
    
    
main()