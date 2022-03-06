from ast import Store
from cProfile import label
from manim import *


class Graphing(Scene):
    def construct(self):
        
        plane = NumberPlane(
            x_range= [-4,4,2],x_length=7,y_range=[0,16,4],y_length=8
        ).to_edge(DOWN)
        labels = plane.get_axis_labels(x_label="x",y_label="f(x)")
        
        parab=plane.plot(lambda x : x**2, x_range =[-4, 4],color = GREEN)
        func_label = MathTex("f(x)={x}^{2}").scale(0.6).next_to(parab,UR,buff=0.5).set_color(GREEN)

        area= plane.get_riemann_rectangles(
            graph= parab,x_range=[-2,3],stroke_width=0.1,stroke_color=WHITE
            )
        
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(parab,func_label,labels)))
        self.wait()
        self.play(Create(area))
        self.wait()