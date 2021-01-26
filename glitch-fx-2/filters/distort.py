import cv2 as cv
import numpy as np
from util.exstatements import orientationExcep
# input: the actual image object, not the path


def scanner(srcImg, **kwargs):
    dstImg = srcImg
    (w, h) = (srcImg.shape[1], srcImg.shape[0])
    # get bound(s) and direction
    _start = kwargs.get("start") or 0.9
    _end = kwargs.get("end") or None
    _orientation = kwargs.get("orientation") or "v"
    if _orientation == "h":
        x0 = int(_start*w)
        xf = int(_end*w) if _end else None
        srcImg = cv.transpose(srcImg)
        dstImg = cv.transpose(dstImg)
        dstImg[x0:xf, :, :] = srcImg[x0, :, :]
        dstImg = cv.transpose(dstImg)
    elif _orientation == "v":
        y0 = int(_start*h)
        yf = int(_end*h) if _end else None
        roi = srcImg[y0, :, :]
        dstImg[y0:yf, :, :] = srcImg[y0, :, :]
    else:
        orientationExcep()
    return dstImg

# BURN


def burn(srcImg, **kwargs):
    dstImg = srcImg
    _pct = kwargs.get("pct") or 0.1
    # get threshold
    grayImg = cv.cvtColor(srcImg, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(grayImg, int(
        _pct*255), 255, cv.THRESH_BINARY_INV)

    thresh.reshape(thresh.shape[0], thresh.shape[1]).astype("?")
    thresh = cv.merge((thresh, thresh, thresh))
    # get inverse
    invImg = cv.cvtColor(srcImg, cv.COLOR_BGR2HSV)
    invImg[:, :, 2] = 255 - invImg[:, :, 2]
    dstImg = cv.bitwise_or(srcImg, cv.bitwise_and(invImg, thresh))
    return dstImg

# WARP IMAGE


def warpImage(srcImg, **kwargs):
    dstImg = srcImg
    (w, h) = (srcImg.shape[1], srcImg.shape[0])
    # get factor and type of warp
    _type = kwargs.get("warptype")
    _factor = kwargs.get("factor") or 0.0
    # functions
    def shearX(_u, _v): return (_u, (_u+int(_factor*_v)) % w)
    def shearY(_u, _v): return ((_u+int(_factor*_v)) % h, _v)

    def rotateX(_u, _v): return(
        _u, int(_u*np.sin(_factor) + _v*np.cos(_factor)) % w)

    def rotateY(_u, _v): return(
        int(_u*np.cos(_factor) - _v*np.sin(_factor)) % h, _v)

    # dictionary of functions based on _type
    f = {"shearX": shearX, "shearY": shearY,
         "rotateX": rotateX, "rotateY": rotateY}
    # do the warp
    for i in range(w*h):
        (u, v) = divmod(i, w)
        (x, y) = f[_type](u, v)
        dstImg[x, y] = srcImg[u, v]
    return dstImg

# NOISE DISTORT


def noiseDistort(srcImg, **kwargs):
    pass
