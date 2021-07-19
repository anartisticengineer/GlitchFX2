from . import basic, distort

effects = {
    "noisy": basic.noisy,
    "scanline": basic.scanline,
    "highpass": basic.highpass,
    "scanner": distort.scanner,
    "burn": distort.burn,
    "warp": distort.warpImage,
    "rshift": distort.randomShift,
    "hueshift": distort.hueShift,
}