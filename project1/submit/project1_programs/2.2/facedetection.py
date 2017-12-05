"""
Code for COMP422 Project 1 Task 2.2: Face Detection
Feature Extraction and Creating Tabular Data Sets
Author: Shi Tao, student number: 300409943
"""

import csv
import glob
import scipy.signal


def upper_left(im):
    """Fetch the min, max and total values of pixels in upper left area as the 
    feature of lefteyeball, white of the lefteye and the whole upper left sub-image"""
    seg = []
    for row in im[:9]:
        for col in row[:9]:
            seg.append(col)
    return (min(seg), max(seg), sum(seg))


def upper_right(im):
    """Fetch the min, max and total values of pixels in upper right area as the 
    feature of righteyeball, white of the righteye and the whole upper right sub-image"""
    seg = []
    for row in im[:9]:
        for col in row[10:]:
            seg.append(col)
    return (min(seg), max(seg), sum(seg))


def nose(im):
    """Fetch the biggest value of pixels and its location in middle area as the 
    feature of nose"""    
    seg = []
    for row in im[7:12]:
        for col in row[7:12]:
            seg.append(col)
    return (max(seg), seg.index(max(seg)) % 5)


def lower_left(im):
    """Fetch the information of lower left area"""
    seg = []
    for row in im[10:]:
        for col in row[:9]:
            seg.append(col)
    return seg


def lower_right(im):
    """Fetch the information of lower right area"""
    seg = []
    for row in im[10:]:
        for col in row[10:]:
            seg.append(col)
    return seg


def similarity(seg):
    """Fetch the four statistic features of lower left area and lower right 
    area in according to handout""" 
    c = seg[40]
    x = seg[4] + seg[13] + seg[22] + seg[31] + seg[49] + seg[58] + seg[67] + seg[76]
    + seg[36] + seg[37] + seg[38] + seg[39] + seg[41] + seg[42] + seg[43] + seg[44]
    y = seg[0] + seg[10] + seg[20] + seg[30] + seg[50] + seg[60] + seg[70] + seg[80]
    + seg[8] + seg[16] + seg[24] + seg[32] + seg[48] + seg[56] + seg[64] + seg[72]
    z = sum(seg) - c - x - y           
    return (c, x / 16, y / 16, z / 48)


def feature_extraction(im_list):
    """Extracte the features from the image"""
    lefteyeball, lefteyewhite, upperleft = upper_left(im_list)
    righteyeball, righteyewhite, upperright = upper_right(im_list)
    (lc, lx, ly, lz) = similarity(lower_left(im_list))
    (rc, rx, ry, rz) = similarity(lower_right(im_list))
    
    #The difference between two eyeballs
    eyeball_diff = abs(lefteyeball - righteyeball)
    #The difference between two eyewhites
    eyewhite_diff = abs(lefteyewhite - righteyewhite)
    #The difference between upper-left subimage and upper-right subimage
    upper_diff = abs(upperleft - upperright)
    #The brightness and location of nose tip
    (noselip_bright, noselip_loc) = nose(im_list)
    #The difference between similarity features of two lower sides
    lowerc_diff = abs(lc - rc)
    lowerx_diff = abs(lx - rx)
    lowery_diff = abs(ly - ry)
    lowerz_diff = abs(lz - rz)
    return [eyeball_diff, eyewhite_diff, upper_diff, noselip_bright, noselip_loc,
            lowerc_diff, lowerx_diff, lowery_diff, lowerz_diff]
    
    

def main():
    """ Gets the job done """
    train_example = []
    for filename in glob.glob('*.pgm'):
        im = scipy.misc.imread(filename)
        im = im.astype('int32')
        train_example.append((feature_extraction(im) + [1]))
    print(train_example)    
    with open("C:/Users/Administrator/Desktop/422 Data Mining/project/project1-images/2.2/train_face.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(train_example)    
    
    
main()