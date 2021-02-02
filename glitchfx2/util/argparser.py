# takes in input args and parses them to determine which
# effects to apply
class ArgParser:
    def __init__(self):
        self.effect = ""
        self.args = []
        self.argDict = {}

    def getInputArray(self, argString):
        argString = argString.strip()
        self.effect, *self.args = argString.split(" ")

    def parse(self):
        conversion = {"-p": "pct", "-or": "orientation", "-a": "amp",
                      "-k": "kernelSize", "-s": "start", "-e": "end", "-t": "type", "-f": "factor"}
        if (len(self.args) % 2 != 0):
            # must be even number of args
            raise Exception("")
        else:
            self.argDict.clear()
            for i in range(0, len(self.args), 2):
                def formatArg(x): return x if x.isalpha() else float(x)
                key_i = conversion[self.args[i]]
                val_i = formatArg(self.args[i+1])
                self.argDict[key_i] = val_i

    def getEffect(self):
        return self.effect

    def getArgDict(self):
        return self.argDict
