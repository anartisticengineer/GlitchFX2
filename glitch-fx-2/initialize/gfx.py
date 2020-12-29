import cv2 as cv


class GlitchFX:
    def __init__(self, imagePath):
        print("Glitch FX started")
        print(imagePath)
        self.src = cv.imread(imagePath)
        cv.imshow("Glitch FX", self.src)
