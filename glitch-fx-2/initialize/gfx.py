import cv2 as cv
from filters import basic, distort


class GlitchFX:
    def __init__(self, imagePath):
        self.srcPath = imagePath
        self.src = cv.imread(self.srcPath)
        self.dest = self.src
        print(self.srcPath)

    def applyEffects(self):
        pass

    def displaySrc(self):
        cv.imshow("Glitch FX src", self.src)

    def displayDst(self):
        cv.imshow("Glitch FX dst", self.dest)
