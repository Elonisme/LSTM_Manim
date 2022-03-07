from tkinter import font
from manim import *
from matplotlib import animation
from scipy.fftpack import shift

class Mylogo(Scene):

    def construct(self):
        E_L =Tex( "E", "L").shift(UP*3+LEFT*3)
        animations = [
            FadeIn(E_L[0],shift=UP*3+LEFT*3),
            FadeIn(E_L[1],shift=UP*3+LEFT*3),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5),run_time = 3)

        square = Square()
        circle = Circle()
        anno = Text("欢迎收看我的频道")
        anno.shift(2 * DOWN)
        self.add(anno)
        self.add(square)
        self.play(ClockwiseTransform(square, circle))


        vb = Text("VIODE BEGIN", font="Noto Sans", color=RED)
        self.play(FadeIn(vb))
        self.play(FadeOut(vb))
        # introduce = Text('Hello I am Elon Li', gradient=(RED, BLUE, GREEN), font_size = 96)
        # Elon_Li = Text('Elon Li', color=GREEN,font_size=96)
        # E_L =Tex(
        #     "E", "L").scale(2)
        # self.play(Write(introduce),run_time=3)
        # self.wait(1)
        # self.play(FadeOut(introduce),run_time=3)
        # self.play(Write(Elon_Li),run_time = 1)
        # self.play(FadeOut(Elon_Li),run_time=3)
        # self.wait(1)
        # animations = [
        #     FadeIn(E_L[0],target_position=Elon_Li),
        #     FadeIn(E_L[1], target_position=Elon_Li)
        # ]
        # self.play(AnimationGroup(*animations, lag_ratio=0.5))
        # self.play(FadeOut(AnimationGroup(*animations, lag_ratio=0.5)),run_time=3)