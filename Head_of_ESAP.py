from email.mime import application
from gzip import WRITE
from tkinter import CENTER, font
from typing_extensions import runtime
from manim import *
from matplotlib import animation, image, transforms
from scipy.fftpack import shift

class HeadofESAP(Scene):

    def construct(self):
        '''开头'''
        self.add_sound(r"bgm\begining.mp3")
        title = Tex("环境指数评估及预测模型", tex_template=TexTemplateLibrary.ctex,color=BLUE,font_size=50).shift(DOWN*2)
        nomo =Tex("Environmental Index Evaluation and Prediction Model",color=BLUE,font_size=20)
        VGroup(title,nomo).arrange(DOWN*2)
        img =ImageMobject('Xihua_University_logo.png').shift(UP)

        self.wait()
        self.play(FadeIn(img),run_time=2)
        #self.add_sound(r'Vincent Rubinetti - The Music of 3Blue1Brown\Vincent Rubinetti - The Music of 3Blue1Brown - 01 Zeta.mp3',time_offset=1,gain=0.01)
        self.play(
            Write(title,shift = DOWN*3),
            FadeIn(nomo,shift=DOWN*4),
            run_time=3
        )
        self.wait(2)

        transform_title = Tex(r"Natural selection \\ moves forward four",font_size=15,color=BLUE)
        transform_title.to_edge(LEFT).shift(UP*3)

        self.play(
            ReplacementTransform(title, transform_title),
            LaggedStart(*(FadeOut(obj, shift=DOWN) for obj in nomo)),
            FadeOut(img),
            run_time=1
        )
        
        img.scale(0.3).next_to(transform_title).shift(UP*0.6+LEFT*1.2)
        self.add(img)
        self.wait()