"""
Code for COMP422 Project 1 Task 3.1: Object Recognition: Classication of Hand-Written Digits
Put the values of these extracted features together to form a tabular data set
Author: Shi Tao, student number: 300409943
"""

import csv
import glob
import scipy.signal


def data_process(f0, f1, f2, f3, f4, f5):
    """Process the 6 extracted feature sets"""
    filedata0 = open(f0)
    data0 = filedata0.readlines()
    filedata0.close()
    filedata1 = open(f1)
    data1 = filedata1.readlines()
    filedata1.close()
    filedata2 = open(f2)
    data2 = filedata2.readlines()
    filedata2.close()
    filedata3 = open(f3)
    data3 = filedata3.readlines()
    filedata3.close() 
    filedata4 = open(f4)
    data4 = filedata4.readlines()
    filedata4.close() 
    filedata5 = open(f5)
    data5 = filedata5.readlines()
    filedata5.close()     

    data_list = []
    for line in data0[:]:
        obj = line.split()
        attributes = []
        for i in range(76):
            attributes.append(obj[i])
        data_list.append(attributes)
    n = 0
    for line in data1[:]:
        obj = line.split()
        for i in range(216):
            data_list[n].append(obj[i])
        n += 1
    n = 0
    for line in data2[:]:
        obj = line.split()
        for i in range(64):
            data_list[n].append(obj[i])
        n += 1
    n = 0
    for line in data3[:]:
        obj = line.split()
        for i in range(240):
            data_list[n].append(obj[i])
        n += 1
    n = 0
    for line in data4[:]:
        obj = line.split()
        for i in range(47):
            data_list[n].append(obj[i])
        n += 1
    n = 0
    for line in data5[:]:
        obj = line.split()
        for i in range(6):
            data_list[n].append(obj[i])
        n += 1
    n = 0
    for digit in range(10):
        for i in range(200):
            data_list[n].append(digit)
            n += 1 
    return data_list
    #print(len(data_list[1999]))
        
        
def main():
    """ Gets the job done """
    data = data_process('mfeat-fou', 'mfeat-fac', 'mfeat-kar', 'mfeat-pix', 'mfeat-zer', 'mfeat-mor')
    with open("C:/Users/Administrator/Desktop/422 Data Mining/project/project1-images/3.1/mfeat-digits/digitdata.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    
main()