from tkinter import CENTER, font
from manim import *
from matplotlib import animation, image
from scipy.fftpack import shift

class Mylogo(Scene):

    def construct(self):
        '''开头'''
        title = Tex("环境指数评估及预测模型", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        nomo =Tex("Environmental Index Evaluation and Prediction Model",color=BLUE,font_size=20)
        VGroup(title,nomo).arrange(DOWN)
        img =ImageMobject('Xihua_University_logo.png')

        self.wait()
        self.play(FadeIn(img),run_time=2)
        self.play(
            Write(title),
            FadeIn(nomo,shift=DOWN),
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

        '''内容部分'''
        section1 = Tex("第一部分：", tex_template=TexTemplateLibrary.ctex, font_size=20, color=RED_E).to_edge(LEFT+UP*2.5)
        self.play(Write(section1))
        self.wait()
        self.play(Unwrite(section1))
        section2 = Tex("第二部分：", tex_template=TexTemplateLibrary.ctex, font_size=20, color=RED_E).to_edge(LEFT+UP*2.5)
        self.play(Write(section2))
        self.wait()
        self.play(Unwrite(section2))
        section3 = Tex("第三部分：", tex_template=TexTemplateLibrary.ctex, font_size=20, color=RED_E).to_edge(LEFT+UP*2.5)
        self.play(Write(section3))
        self.wait()
        self.play(Unwrite(section3))
        section4 = Tex("第四部分：", tex_template=TexTemplateLibrary.ctex, font_size=20, color=RED_E).to_edge(LEFT+UP*2.5)
        self.play(Write(section4))
        self.wait()
        self.play(Unwrite(section4))

        '''结尾'''

        support = Tex(r"This video is supported by Manim CE and \LaTeX",font_size=40)
        codesource = Tex(r"项目代码和视频代码已经全部上传至\\https://github.com/Elonisme/ELManim", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        references = Tex(
            r"References\\(1)The Manim Community v0.15.0 Reference Manual\\",
            "(2)Miktex ORG",
            font_size=20)
        references[1].next_to(references[0],DOWN,aligned_edge=LEFT)

        teamsname = Tex(r"成员名单\\李毅龙\\陈铭璇\\李兴雨",tex_template=TexTemplateLibrary.ctex,font_size = 20)

        grateful = Tex("感谢您的观看", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        teamsup = Tex(r"自然选择前进四全体成员致上", tex_template=TexTemplateLibrary.ctex, font_size=20, color=BLUE).shift(DOWN)

        self.play(Write(support))
        self.wait()
        self.play(FadeOut(support))
        self.play(Write(codesource))
        self.wait()
        self.play(FadeOut(codesource))
        self.play(Write(references),run_time = 2)
        self.wait(2)
        self.play(FadeOut(references))
        self.wait()
        self.play(Write(teamsname),run_time = 2)
        self.wait()
        self.play(FadeOut(teamsname))
        self.wait()
        self.play(Write(grateful),run_time = 2)
        self.wait()
        self.play(FadeOut(grateful))
        self.wait()
        self.play(
            FadeOut(img)
            )
        self.wait()
        img.move_to(ORIGIN).scale(1.5)
        self.play(
            ReplacementTransform(transform_title,teamsup),
            FadeIn(img)
            )
        self.wait()
        self.play(
            FadeOut(teamsup),
            FadeOut(img),
            run_time = 3
            )
        self.wait()






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