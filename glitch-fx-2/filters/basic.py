import cv2 as cv
import numpy as np
import util.exstatements as ex

# NOISY


def noisy(srcImg, **kwargs):
    _pct = kwargs.get("pct") or 0.1
    poisson = np.random.poisson(_pct*100, srcImg.size)
    poisson = poisson.reshape(
        srcImg.shape[0], srcImg.shape[1], srcImg.shape[2]).astype(np.uint8)
    dstImg = cv.add(srcImg, poisson)
    return dstImg

# SCANLINE


def scanline(srcImg, **kwargs):
    _orientation = kwargs.get("orientation") or "h"
    if _orientation == "h":
        maxI = srcImg.shape[0]
        # every row is all zeros
        srcImg[0:maxI:2] = [0, 0, 0]
    elif _orientation == "v":
        maxI = srcImg.shape[1]
        srcImg[:, 0:maxI:2] = [0, 0, 0]
    else:
        ex.orientationExcep()
    return srcImg

# HIGHPASS


def highpass(srcImg, **kwargs):
    _pct = kwargs.get("pct") or 1.0
    _amp = kwargs.get("amp") or 1.0
    _kernelSize = int(kwargs.get("kernelSize")) or 3
    # kernel size should be odd and greater than 1
    if (_kernelSize % 2 == 0) or (_kernelSize <= 1):
        ex.invalidKernelSizeExcep()
    # calculate midpoint from kernel size
    midpoint = int(_kernelSize/2)
    filt = np.ones((_kernelSize, _kernelSize), dtype=np.float32)
    filt *= -1.0 * _pct
    filt[midpoint, midpoint] = (_kernelSize ** 2) * _amp
    dstImg = cv.filter2D(srcImg, -1, filt)
    return dstImg
