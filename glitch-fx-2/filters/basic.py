import cv2 as cv
import numpy as np
from util.exstatements import orientationExcep
#pylint: disable=no-member


def noisy(srcImg, pct):
    gauss = np.random.normal(0, pct, srcImg.size)
    gauss = np.reshape(gauss, srcImg.shape).astype('uint8')
    return srcImg + srcImg * gauss


def scanline(srcImg, orientation="h"):
    if orientation == "h":
        maxI = srcImg.shape[0]
        # every row is all zeros
        srcImg[0:maxI:2] = [0, 0, 0]
    elif orientation == "v":
        maxI = srcImg.shape[1]
        srcImg[:, 0:maxI:2] = [0, 0, 0]
    else:
        raise orientationExcep
    return srcImg


def highpass(srcImg):
    filt = np.ones((3, 3), dtype=np.float32)
    filt[1, 1] = 9.0
    filt[1, 0::2] = -2.5
    filt[0::2, 1] = -2.5
    filt /= 2.0
    dstImg = cv.filter2D(srcImg, -1, filt)
    return dstImg
