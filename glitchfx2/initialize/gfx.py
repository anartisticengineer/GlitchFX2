import cv2 as cv
from util.argparser import ArgParser
from util.prompts import Prompt
from filters import basic, distort


class GlitchFX:
    def __init__(self, imagePath, scale=1.0):
        self.parser = ArgParser()
        self.srcPath = imagePath
        self.src = cv.imread(self.srcPath)
        (w, h) = (self.src.shape[1], self.src.shape[0])
        newSize = (int(w * scale), int(h * scale))
        self.src = cv.resize(self.src, newSize, cv.INTER_CUBIC)
        self.dest = self.src
        print(self.srcPath)

    def glitch(self, req, srcImg, **kwargs):
        if req == "noisy":
            self.dest = basic.noisy(srcImg, **kwargs)
        elif req == "scanline":
            self.dest = basic.scanline(srcImg, **kwargs)
        elif req == "highpass":
            self.dest = basic.highpass(srcImg, **kwargs)
        elif req == "scanner":
            self.dest = distort.scanner(srcImg, **kwargs)
        elif req == "burn":
            self.dest = distort.burn(srcImg, **kwargs)
        elif req == "warp":
            self.dest = distort.warpImage(srcImg, **kwargs)
        elif req == "rshift":
            self.dest = distort.randomShift(srcImg, **kwargs)
        else:
            raise Exception("invalid effect")

    def applyEffects(self):
        nextFx = Prompt().enterEffect()
        while nextFx != "x":
            self.parser.getInputArray(nextFx)
            self.parser.parse()
            self.glitch(self.parser.getEffect(), self.dest, **self.parser.getArgDict())
            nextFx = Prompt().enterEffect()

    def displaySrc(self):
        cv.imshow("Glitch FX src", self.src)

    def displayDst(self):
        cv.imshow("Glitch FX dst", self.dest)

    def __del__(self):
        print("Done")
