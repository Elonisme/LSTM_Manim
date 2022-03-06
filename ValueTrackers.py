from multiprocessing.sharedctypes import Value
from manim import *


class ValueTrackers(Scene):
    def construct(self):
        
        k = ValueTracker(5)

        num =always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0),run_time=5,rate_func=smooth)