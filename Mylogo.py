from tkinter import font
from manim import *
from matplotlib import animation
from scipy.fftpack import shift

class Mylogo(Scene):

    def construct(self):
        introduce = Text('Hello I am Elon Li', gradient=(RED, BLUE, GREEN), font_size = 96)
        Elon_Li = Text('Elon Li', color=GREEN,font_size=96)
        E_L =Tex(
            "E", "L").scale(2)
        self.play(Write(introduce),run_time=3)
        self.wait(1)
        self.play(FadeOut(introduce),run_time=3)
        self.play(Write(Elon_Li),run_time = 1)
        self.play(FadeOut(Elon_Li),run_time=3)
        self.wait(1)
        animations = [
            FadeIn(E_L[0],target_position=Elon_Li),
            FadeIn(E_L[1], target_position=Elon_Li)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))