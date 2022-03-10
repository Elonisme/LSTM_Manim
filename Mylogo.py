from email.mime import application
from tkinter import CENTER, font
from typing_extensions import runtime
from manim import *
from matplotlib import animation, image
from scipy.fftpack import shift

class ComputerProject(Scene):

    def construct(self):
        '''开头'''
        self.add_sound(r"bgm\begining.mp3")
        title = Tex("环境指数评估及预测模型", tex_template=TexTemplateLibrary.ctex, font_size=50, color=RED_E)
        nomo =Tex("Environmental Index Evaluation and Prediction Model",color=BLUE,font_size=20)
        VGroup(title,nomo).arrange(DOWN)
        img =ImageMobject('Xihua_University_logo.png')

        self.wait()
        self.play(FadeIn(img),run_time=2)
        # self.add_sound(r'Vincent Rubinetti - The Music of 3Blue1Brown\Vincent Rubinetti - The Music of 3Blue1Brown - 01 Zeta.mp3',time_offset=1,gain=0.01)
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
        self.add_sound(r"bgm\miding.mp3")
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

        self.add_sound(r"bgm\ending.mp3")

        support = Tex(r"This video is supported by",font_size=40).shift(UP)
        Latexbird = ImageMobject(r"latexbird.jpg").move_to(support).shift(DOWN+LEFT).scale(0.25)
        Latex = Tex(r"\LaTeX",font_size = 30).move_to(Latexbird).shift(DOWN)

        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        Manimlogo = VGroup(triangle, square, circle, ds_m)  # order matters
        Manimlogo.move_to(Latexbird).shift(RIGHT*1.5).scale(0.20)
        Manim = Tex("Manim CE",font_size = 20).move_to(Manimlogo).shift(DOWN)

        codesource = Tex(r"项目代码和视频代码已经全部上传至\\https://github.com/Elonisme/ELManim", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        referencesTop = Tex("References",font_size = 30)
        references = Tex(
            r"\\(1)The Manim Community v0.15.0 Reference Manual\\",
            "(2)Miktex ORG",
            font_size=20).shift(UP)

        references[1].next_to(references[0],DOWN,aligned_edge=LEFT)
        referencesTop.move_to(references).shift(UP*1.2)
        
        teamTop = Tex("成员名单",tex_template=TexTemplateLibrary.ctex,font_size =30)
        teamsname = Tex(r"\\李毅龙\\陈铭璇\\李兴雨",tex_template=TexTemplateLibrary.ctex,font_size = 20)
        teamTop.move_to(teamsname).shift(UP)

        grateful = Tex("感谢您的观看", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        teamsup = Tex(r"自然选择前进四全体成员致上", tex_template=TexTemplateLibrary.ctex, font_size=20, color=BLUE).shift(DOWN)

        self.play(
            Write(support),
            Write(Latex),
            FadeIn(Latexbird),
            Create(Manimlogo),
            Write(Manim),
            run_time = 2
            )
        self.wait()
        self.play(
            FadeOut(support),
            Unwrite(Latex),
            FadeOut(Latexbird),
            Uncreate(Manimlogo),
            Unwrite(Manim),
            run_time = 2
            )
        self.play(Write(codesource))
        self.wait()
        self.play(FadeOut(codesource))
        self.play(
            Write(referencesTop),
            Write(references),
            run_time = 2
            )
        self.wait(2)
        self.play(
            FadeOut(referencesTop),
            FadeOut(references),
            run_time = 2
            )
        self.wait()
        self.play(
            Write(teamTop),
            Write(teamsname),
            run_time = 2)
        self.wait()
        self.play(
            FadeOut(teamTop),
            FadeOut(teamsname)
            )
        self.wait()
        self.play(Write(grateful),run_time = 2)
        self.wait()
        self.play(FadeOut(grateful))
        self.wait()
        # img.move_to(ORIGIN).scale(1.5)
        self.play(
            ReplacementTransform(transform_title,teamsup),
            img.animate.move_to(ORIGIN).scale(1.5),
            runtime = 2
            )
        self.wait()
        self.play(
            FadeOut(teamsup),
            FadeOut(img),
            run_time = 2
            )
        self.wait(2)






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