from turtle import fillcolor
from manim import *


class Amedee(Scene):
    def construct(self):
        
        name=Tex("Amedee", tex_template=TexTemplateLibrary.ctex, font_size=30).to_edge(UL,buff=1)
        sq=Square(
            side_length=2,
            fill_color=GREEN,
            fill_opacity=0.75
            ).shift(
                LEFT*3
                )
        tri =Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq))
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR),run_time=2)
        self.play(sq.animate.scale(2),tri.animate.to_edge(DL),run_time=3)
        self.wait()