import cv2 as cv
import numpy as np
import glitchfx2.util.exstatements as ex

# NOISY


def noisy(src_img, **kwargs):
    _pct = kwargs.get("pct") or 0.1
    if _pct < 0.0 or _pct > 1.0:
        ex.percentageExcep()
    poisson = np.random.poisson(_pct * 100, src_img.size)
    poisson = poisson.reshape(src_img.shape[0], src_img.shape[1], src_img.shape[2]).astype(
        np.uint8
    )
    dst_img = cv.add(src_img, poisson)
    return dst_img


# SCANLINE


def scanline(src_img, **kwargs):
    _orientation = kwargs.get("orientation") or "h"
    if _orientation == "h":
        max_i = src_img.shape[0]
        # every row is all zeros
        src_img[0:max_i:2] = [0, 0, 0]
    elif _orientation == "v":
        max_i = src_img.shape[1]
        src_img[:, 0:max_i:2] = [0, 0, 0]
    else:
        ex.orientationExcep()
    return src_img


# HIGHPASS


def highpass(src_img, **kwargs):
    _pct = kwargs.get("pct") or 1.0
    _amp = kwargs.get("amp") or 1.0
    _kernelSize = kwargs.get("kernelSize") or 3
    # kernel size should be odd and greater than 1
    if (_kernelSize % 2 == 0) or (_kernelSize <= 1):
        ex.invalidKernelSizeExcep()
    # calculate midpoint from kernel size
    midpoint = int(_kernelSize / 2)
    filt = np.ones((_kernelSize, _kernelSize), dtype=np.float32)
    filt *= -1.0 * _pct
    filt[midpoint, midpoint] = (_kernelSize ** 2) * _amp
    dstImg = cv.filter2D(src_img, -1, filt)
    return dstImg
