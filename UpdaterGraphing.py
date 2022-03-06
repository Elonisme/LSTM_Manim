from manim import *


class UpdaterGraphing(Scene):
    def construct(self):
        
        k=ValueTracker(-4)
        ax = Axes(
            x_range= [0,10,1],y_range=[0,20,2],x_length=10,y_length=10
        ).to_edge(DOWN)

        func= ax.plot(lambda x : 0.1 * (x - 2) * (x - 5) * (x - 7) + 7, x_range=[0,10],color=BLUE)
        
        # func = ax.plot(lambda x: x**2, x_range=[-4,4],color = BLUE)

        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
                x =k.get_value(),
                graph=func,dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=3
            )
        )

        pt =always_redraw(
            lambda:Dot().move_to(ax.c2p(k.get_value(),func.underlying_function(k.get_value())))
        )

        self.add(ax,func,slope,pt)
        self.wait()
        self.play(k.animate.set_value(4),run_time=4)
