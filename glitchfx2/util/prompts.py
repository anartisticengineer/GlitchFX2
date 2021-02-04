from os import path


class Prompt:
    def __init__(self):
        pass

    # ask where to find the file
    def getInputFile(self):
        # FIRST PROMPT
        return input("\nChoose an input image file... ")

    def cantFindSrc(self, _pathName):
        print("I couldn't find a src folder.")
        print("So I made one for you to store your photos~")
        print("Creating your src folder at " + _pathName)
        print("Run the program again and you should be good!")

    def enterEffect(self):
        return input("\nEnter an effect ~ x to finish... ")

    # ask what to save the file as
    def getOutputFileName(self, _originalFileName):
        (origName, ext) = path.splitext(_originalFileName)
        defaultName = origName + "-glitched"
        print("\nEnter an output file name...")
        return (input("Or leave blank for the default name... ") or defaultName) + ext