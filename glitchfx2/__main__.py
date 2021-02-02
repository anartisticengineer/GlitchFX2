# pylint: disable=no-name-in-module
import os
from cv2 import waitKey, imwrite
from initialize.gfx import GlitchFX
from util.prompts import Prompt

if __name__ == "__main__":
    if os.path.isdir("src") == False:
        absPath = os.path.abspath("../glitch-fx-2")
        Prompt().cantFindSrc(absPath)
        os.mkdir("src")
    else:
        os.chdir("src")

        # choose a file already in the src folder
        fileIn = Prompt().getInputFile()
        # pass the absolute path into GlitchFX: this will be the read image
        gfx = GlitchFX(os.path.join(os.getcwd(), fileIn))
        gfx.applyEffects()
        gfx.displayDst()

        k = waitKey()
        # ~~~~~press s to save the image~~~~~~~
        if k == ord("s") or k == ord("S"):
            os.chdir("../")
            # create dest folder if it doesn't exist
            if os.path.isdir("dest") == False:
                os.mkdir("dest")
            os.chdir("dest")
            print("Saving to " + os.getcwd())
            (_, ext) = os.path.splitext(fileIn)
            destFileName = Prompt().getOutputFileName(fileIn)
            imwrite(destFileName + ext, gfx.dest)
            print("Sucessfully saved to " + os.path.join(os.getcwd(), destFileName))
        del gfx
        print("Done")
