# takes in input args and parses them to determine which
# effects to apply
from util.exstatements import scaleExcep, invalidInputSizeExcep


class ArgParser:
    def __init__(self):
        self.effect = ""
        self.args = []
        self.argDict = {}

    def getInputArray(self, argString):
        argString = argString.strip()
        self.effect, *self.args = argString.split(" ")

    def parse(self):
        conversion = {
            "-p": "pct",
            "-or": "orientation",
            "-a": "amp",
            "-k": "kernelSize",
            "-s": "start",
            "-e": "end",
            "-t": "type",
            "-f": "factor",
        }
        if len(self.args) % 2 != 0:
            # must be even number of args
            invalidInputSizeExcep()
        else:
            self.argDict.clear()
            for i in range(0, len(self.args), 2):

                def formatArg(x):
                    return x if x.isalpha() else float(x)

                key_i = conversion[self.args[i]]
                val_i = formatArg(self.args[i + 1])
                self.argDict[key_i] = val_i

    def getEffect(self):
        return self.effect

    def getArgDict(self):
        return self.argDict


class ImageInputParser:
    def __init__(self, argString):
        argArr = argString.split(" ")
        argArrLen = len(argArr)
        self.fileIn = argArr[0]
        self.scale = 1.0
        if argArrLen == 1:
            pass
        elif argArrLen == 2:
            self.scale = float(argArr[1])
            if self.scale <= 0.0:
                scaleExcep()

    def getFileIn(self):
        return self.fileIn

    def getScale(self):
        return self.scale