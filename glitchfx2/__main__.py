import os
from cv2 import waitKey, imwrite
from glitchfx2.initialize.gfx import GlitchFX
from glitchfx2.util.prompts import Prompt
from glitchfx2.util.argparser import ImageInputParser

if __name__ == "__main__":
    if not os.path.isdir("../src"):
        absPath = os.path.abspath("../glitch-fx-2")
        Prompt().cant_find_src(absPath)
        os.mkdir("../src")
    else:
        os.chdir("../src")

        # choose a file already in the src folder
        fileIn = Prompt().get_input_file()
        parser = ImageInputParser(fileIn)
        (file_name, scale) = (parser.fileIn, parser.scale)
        # pass the absolute path into GlitchFX: this will be the read image
        gfx = GlitchFX(os.path.join(os.getcwd(), file_name), scale=scale)
        print(gfx)
        gfx.apply_effects()
        gfx.display_dst()

        k = waitKey()
        # ~~~~~press s to save the image~~~~~~~
        if k == ord("s") or k == ord("S"):
            os.chdir("/")
            # create dest folder if it doesn't exist
            if not os.path.isdir("../dest"):
                os.mkdir("../dest")
            os.chdir("../dest")
            print("Saving to " + os.getcwd())
            destFileName = Prompt().get_output_file_name(f)
            imwrite(destFileName, gfx.dest)
            print("Successfully saved to " + os.path.join(os.getcwd(), destFileName))
        del gfx
