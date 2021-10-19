import cv2 as cv
import numpy as np
from glitchfx2.util.exstatements import orientationExcep
from glitchfx2.util.generators import pixels_generator

# input: the actual image object, not the path


def scanner(src_img, **kwargs):
    dst_img = src_img
    (w, h) = (src_img.shape[1], src_img.shape[0])
    # get bound(s) and direction
    _start = kwargs.get("start") or 0.9
    _end = kwargs.get("end") or None
    _orientation = kwargs.get("orientation") or "v"
    if _orientation == "h":
        x0 = int(_start * w)
        xf = int(_end * w) if _end else None
        src_img = cv.transpose(src_img)
        dst_img = cv.transpose(dst_img)
        dst_img[x0:xf, :, :] = src_img[x0, :, :]
        dst_img = cv.transpose(dst_img)
    elif _orientation == "v":
        y0 = int(_start * h)
        yf = int(_end * h) if _end else None
        roi = src_img[y0, :, :]
        dst_img[y0:yf, :, :] = src_img[y0, :, :]
    else:
        orientationExcep()
    return dst_img


# BURN


def burn(srcImg, **kwargs):
    dst_img = srcImg
    _pct = kwargs.get("pct") or 0.1
    # get threshold
    grayImg = cv.cvtColor(srcImg, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(grayImg, int(_pct * 255), 255, cv.THRESH_BINARY_INV)

    thresh.reshape(thresh.shape[0], thresh.shape[1]).astype("?")
    thresh = cv.merge((thresh, thresh, thresh))
    # get inverse
    inv_img = cv.cvtColor(srcImg, cv.COLOR_BGR2HSV)
    inv_img[:, :, 2] = 255 - inv_img[:, :, 2]
    dst_img = cv.bitwise_or(srcImg, cv.bitwise_and(inv_img, thresh))
    return dst_img


# WARP IMAGE


def warpImage(srcImg, **kwargs):
    dstImg = srcImg
    (w, h) = (srcImg.shape[1], srcImg.shape[0])
    # get factor and type of warp
    _type = kwargs.get("warptype") or "shearX"
    _factor = kwargs.get("factor") or 0.0
    # functions
    shearX = lambda _u, _v: (_u, (_u + int(_factor * _v)) % w)
    shearY = lambda _u, _v: ((_u + int(_factor * _v)) % h, _v)
    rotateX = lambda _u, _v: (_u, int(_u * np.sin(_factor) + _v * np.cos(_factor)) % w)
    rotateY = lambda _u, _v: (int(_u * np.cos(_factor) - _v * np.sin(_factor)) % h, _v)

    # dictionary of functions based on _type
    f = {"shearX": shearX, "shearY": shearY, "rotateX": rotateX, "rotateY": rotateY}
    # do the warp
    for u, v in pixels_generator(w, h):
        (x, y) = f[_type](u, v)
        dstImg[x, y] = srcImg[u, v]
    return dstImg


# NOISE DISTORT


def randomShift(srcImg, **kwargs):
    dstImg = srcImg
    (w, h) = (srcImg.shape[0], srcImg.shape[1])
    # get the kwargs
    _pct = kwargs.get("pct") or 0.1
    _start = kwargs.get("start") or 0.4
    _end = kwargs.get("end") or 0.6
    for y in range(int(_start * h), int(_end * h)):
        shift = np.random.randint(int(-w * _pct), int(w * _pct))
        u = srcImg[:, y]
        x = [u[(i + shift) % w] for i in range(w)]
        dstImg[:, y] = x[:]
    return dstImg


# HUE SHIFT


def hueShift(srcImg, **kwargs):
    dstImg = srcImg
    (w, h) = (srcImg.shape[1], srcImg.shape[0])
    # get kwargs
    _pct = kwargs.get("pct", 0.1)
    dstImg = cv.cvtColor(srcImg, cv.COLOR_BGR2HSV)
    hueImg = np.zeros(srcImg.shape, dtype=np.uint8)
    _, thresh = cv.threshold(srcImg, int(_pct * 255), 255, cv.THRESH_BINARY_INV)
    # converts array to boolean
    thresh = thresh != 0
    toHue = lambda val, maxVal: int((val / maxVal) * 179)
    for x, y in pixels_generator(w, h):
        hueImg[x, y] = [toHue(x, w), 255, 255]
    dstImg = srcImg + thresh * hueImg
    return dstImg