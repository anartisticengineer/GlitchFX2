def orientationExcep():
    raise Exception('orientation argument in scanline function should be "h" or "v"')


def invalidKernelSizeExcep():
    raise Exception("Kernel size should be an odd integer over 1")

def invalidInputSizeExcep():
    raise Exception("Input modifications are invalid")

def scaleExcep():
    raise Exception("Scale should be greater than 0.0")


def percentageExcep():
    raise Exception("Percentage -p should be between 0.0 and 1.0")


def boundExcep():
    raise Exception("End bound -e should be greater than -s otherwise None")
