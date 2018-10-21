from PIL import Image
import numpy as np
import pylab
import matplotlib.pyplot as plt
import cv2


def calculate_histogram(img):
    hist = np.zeros([256,3], dtype=np.uint32)
    R,C,b = img.shape
    for b in range(3):
        for i in range(0, R):
            for j in range(0, C):
                hist[img[i][j][b],b] += 1
    return hist

def match_histogram(I, J):
    Pj = cdf(J)
    Pi = cdf(I)
    LUT = np.zeros([256,3])
    Gj = 0
    for b in range(3):
        Gj = 0
        for Gi in range(255):
            while Gj < 255 and Pj[Gj,b] <= Pi[Gi,b]:
                Gj = Gj + 1
            LUT[Gi,b] = Gj
    return LUT
    
def cdf(img):
    hist = calculate_histogram(img)
    CDF = np.zeros([256,3])
    for b in range(3):
        for g in range(256):
            CDF[g,b] = np.sum(hist[0:g,b])/np.sum(hist[0:255,b])
    return CDF
