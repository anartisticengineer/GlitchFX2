import cv2 as cv
import numpy as np

orientationExcep = "orientation argument in scanline function should be \"h\" or \"v\""


def noisy(srcImg, strength):
    gauss = np.random.normal(0, strength, srcImg.size)
    ch = (srcImg.shape[0], srcImg.shape[1], srcImg.shape[2])
    gauss = gauss.reshape(ch[0], ch[1], ch[2]).astype('uint8')
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
        raise Exception(orientationExcep)
    return srcImg


def highpass(srcImg):
    kernel = np.ones((3, 3), dtype=np.float32)
    kernel[1, 1] = 4
    kernel[1, 0::2] = -1
    kernel[0::2, 1] = -1
    kernel /= 5
    dstImg = cv.filter2D(srcImg, -1, kernel)
    return dstImg
