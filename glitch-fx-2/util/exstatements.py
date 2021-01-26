def orientationExcep():
    raise Exception(
        "orientation argument in scanline function should be \"h\" or \"v\"")

def invalidKernelSizeExcep():
    raise Exception("Kernel size should be an odd integer over 1")
