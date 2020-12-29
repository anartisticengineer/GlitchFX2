import cv2 as cv


class GlitchFX:
    def __init__(self, imagePath):
        print("Glitch FX started")
        print(imagePath)
        self.srcPath = imagePath

    def displaySrc(self):
        src = cv.imread(self.srcPath)
        cv.imshow("Glitch FX", src)
