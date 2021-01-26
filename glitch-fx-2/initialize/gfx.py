import cv2 as cv
from util.argparser import ArgParser
from filters import basic, distort


class GlitchFX:
    def __init__(self, imagePath):
        self.prompt = "Enter an effect ~ x to finish: "
        self.parser = ArgParser()
        self.srcPath = imagePath
        self.src = cv.imread(self.srcPath)
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
        else:
            raise Exception("invalid effect")

    def applyEffects(self):
        nextFx = input(self.prompt)
        while nextFx != "x":
            self.parser.getInputArray(nextFx)
            self.parser.parse()
            self.glitch(self.parser.getEffect(), self.dest,
                        **self.parser.getArgDict())
            nextFx = input(self.prompt)

    def displaySrc(self):
        cv.imshow("Glitch FX src", self.src)

    def displayDst(self):
        cv.imshow("Glitch FX dst", self.dest)
