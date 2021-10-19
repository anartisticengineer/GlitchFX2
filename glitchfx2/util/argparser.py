# takes in input args and parses them to determine which
# effects to apply
from glitchfx2.util.exstatements import scaleExcep, invalidInputSizeExcep


class ArgParser:
    def __init__(self):
        self.__effect = ""
        self.__args = []
        self.__argDict = {}

    def getInputArray(self, argString):
        argString = argString.strip()
        self.__effect, *self.__args = argString.split(" ")

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
        if len(self.__args) % 2 != 0:
            # must be even number of args
            invalidInputSizeExcep()
        else:
            self.__argDict.clear()
            for i in range(0, len(self.__args), 2):

                def formatArg(x):
                    return x if x.isalpha() else float(x)

                key_i = conversion[self.__args[i]]
                val_i = formatArg(self.__args[i + 1])
                self.__argDict[key_i] = val_i

    @property
    def effect(self):
        return self.__effect

    @property
    def argDict(self):
        return self.__argDict


class ImageInputParser:
    def __init__(self, argString):
        argArr = argString.split(" ")
        argArrLen = len(argArr)
        self.__fileIn = argArr[0]
        self.__scale = 1.0
        if argArrLen == 1:
            pass
        elif argArrLen == 2:
            self.__scale = float(argArr[1])
            if self.__scale <= 0.0:
                scaleExcep()

    @property
    def fileIn(self):
        return self.__fileIn

    @property
    def scale(self):
        return self.__scale