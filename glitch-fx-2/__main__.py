import os
from cv2 import waitKey
from initialize.gfx import GlitchFX

if __name__ == "__main__":
    if (os.path.isdir("src") == False):
        absPath = os.path.abspath("../glitch-fx-2")

        print("I couldn't find a src folder, so I made one for you to store your photos")
        print("Creating the src folder here: {}".format(absPath))
        print("Run the program again and you should be good!")

        os.mkdir("src")
    else:
        os.chdir("src")

        # choose a file already in the src folder
        fileIn = input("Choose an input image file: ")
        # pass the absolute path into GlitchFX: this will be the read image
        gfx = GlitchFX(os.path.join(os.getcwd(), fileIn))
        gfx.displaySrc()

        waitKey()
        print("Done")
