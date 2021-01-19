import cv2 as cv
import numpy as np
from util.exstatements import orientationExcep
#pylint: disable=no-member
# input: the actual image object, not the path


def scannerFull(srcImg, pct, orientation="v"):
    dstImg = srcImg
    if orientation == "v":
        borderRowInd = int((srcImg.shape[0] - 1) * pct)
        borderRow = srcImg[borderRowInd, :]
        dstImg[borderRowInd:, :] = borderRow
    elif orientation == "h":
        borderColInd = int((srcImg.shape[1] - 1) * pct)
        borderCol = srcImg[:, borderColInd]
        dstImg[:, borderColInd:] = borderCol
    else:
        raise orientationExcep
    del srcImg
    return dstImg


def burn(srcImg, pct):
    dstImg = srcImg
    grayImg = cv.cvtColor(srcImg, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(grayImg, int(pct*255), 255, cv.THRESH_BINARY)
    del grayImg
    del ret
    thresh.reshape(thresh.shape[0], thresh.shape[1]).astype("?")
    for i in range(3):
        dstImg[:, :, i] = (srcImg[:, :, i] * thresh)
    del srcImg
    return dstImg
