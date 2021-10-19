import cv2 as cv
from glitchfx2.util.argparser import ArgParser
from glitchfx2.util.prompts import Prompt
from glitchfx2.filters.fxdictionary import effects


class GlitchFX:
    def __init__(self, image_path, scale=1.0):
        self._src_path = image_path
        self._parser = ArgParser()
        self._src = cv.imread(image_path)
        (w, h) = (self._src.shape[1], self._src.shape[0])
        new_size = (int(w * scale), int(h * scale))
        self._src = cv.resize(self._src, new_size, cv.INTER_CUBIC)
        self._dest = self._src

    def __str__(self):
        (w, h) = (self._src.shape[1], self._src.shape[0])
        return f"\nNew GlitchFX\nSource: {self._src_path}\nW:{w}px, H:{h}px"

    def __del__(self):
        print("Done")

    def glitch(self, req, src_img, **kwargs):
        try:
            self._dest = effects[req](src_img, **kwargs)
        except KeyError:
            raise Exception("invalid effect")

    def apply_effects(self):
        next_fx = Prompt().enter_effect()
        while next_fx != "x":
            self._parser.getInputArray(next_fx)
            self._parser.parse()
            self.glitch(self._parser.effect, self._dest, **self._parser.argDict)
            next_fx = Prompt().enter_effect()

    def display_src(self):
        cv.imshow("Glitch FX src", self._src)

    def display_dst(self):
        cv.imshow("Glitch FX dst", self._dest)