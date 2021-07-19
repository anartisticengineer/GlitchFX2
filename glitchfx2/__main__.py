import os
from cv2 import waitKey, imwrite
from initialize.gfx import GlitchFX
from util.prompts import Prompt
from util.argparser import ImageInputParser

if __name__ == "__main__":
    if os.path.isdir("src") == False:
        absPath = os.path.abspath("../glitch-fx-2")
        Prompt().cantFindSrc(absPath)
        os.mkdir("src")
    else:
        os.chdir("src")

        # choose a file already in the src folder
        fileIn = Prompt().getInputFile()
        parser = ImageInputParser(fileIn)
        (f, s) = (parser.getFileIn(), parser.getScale())
        # pass the absolute path into GlitchFX: this will be the read image
        gfx = GlitchFX(os.path.join(os.getcwd(), f), scale=s)
        print(gfx)
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
            destFileName = Prompt().getOutputFileName(f)
            imwrite(destFileName, gfx.dest)
            print("Sucessfully saved to " + os.path.join(os.getcwd(), destFileName))
        del gfx
