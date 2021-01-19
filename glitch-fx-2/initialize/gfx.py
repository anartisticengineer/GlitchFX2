import cv2 as cv
from filters import basic, distort
#pylint: disable=no-member


class GlitchFX:
    def __init__(self, imagePath):
        self.srcPath = imagePath
        self.src = cv.imread(self.srcPath)
        self.dest = self.src
        print(self.srcPath)

    def applyEffects(self):
        self.dest = distort.burn(self.dest, 0.3)
        self.dest = basic.noisy(self.dest, 0.4)
        self.dest = basic.highpass(self.dest)
        self.dest = distort.scannerFull(self.dest, 0.9)

    def displaySrc(self):
        cv.imshow("Glitch FX src", self.src)

    def displayDst(self):
        cv.imshow("Glitch FX dst", self.dest)
