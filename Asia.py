import imp
from lib2to3.pgen2.token import DOT
from manim import *
from pyparsing import line
from scipy.fftpack import shift
class Asia(Scene):
    def construct(self):
        dot1=Dot(UP*3+LEFT*3,radius=0.1,color=RED)
        dot2=Dot(UP*3,radius=0.1,color=RED)
        dot3=Dot(UP*3+RIGHT*3,radius=0.1,color=RED)
        dot4=Dot(LEFT*3,radius=0.1,color=RED)
        dot5=Dot(radius=0.1,color=RED)
        dot6=Dot(RIGHT*3,radius=0.1,color=RED)
        dot7=Dot(DOWN*3+LEFT*3,radius=0.1,color=RED)
        dot8=Dot(DOWN*3,radius=0.1,color=RED)
        dot9=Dot(DOWN*3+RIGHT*3,radius=0.1,color=RED)

        dotm1=Dot(UP*1.5+RIGHT*3,radius=0.1,color=BLUE)
        dotm2=Dot(DOWN*1.5+LEFT*3,radius=0.1,color=RED)
        dotm3=Dot(UP*0.75+RIGHT*1.5,radius=0.05,color=BLUE)
        dotm4=Dot(RIGHT*1.5,radius=0.05,color=BLUE)

        dots=VGroup(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dotm1,dotm2,dotm3,dotm4)
        self.play(Create(dots),run_time=2)
        self.add(dots)

        l1=Line(dot1,dot3,color=RED)
        l2=Line(dot1,dot7,color=RED)
        l3=Line(dot7,dot9,color=RED)
        l4=Line(dot3,dot9,color=RED)
        lm=Line(dot5,dotm1,color=BLUE)
        lm2=Line(dotm3,dotm4,color=BLUE)

        ls=VGroup(l1,l2,l3,l4,lm,lm2)
        self.play(Create(ls),run_time=2)
        self.add(ls)

        dashl1=DashedLine(dot1,dot9,color=RED)
        dashl2=DashedLine(dot3,dot7,color=RED)
        dashl3=DashedLine(dot2,dot8,color=RED)
        dashl4=DashedLine(dot4,dot6,color=RED)

        dashm=DashedLine(dotm1,dotm2,color=BLUE)
        dashls=VGroup(dashl1,dashl2,dashl3,dashl4,dashm)
        self.play(Create(dashls),run_time=2)
        self.add(dashls)

        region1=Tex("Region1").next_to(dot4).shift(DOWN*0.5).scale(0.5)
        region2=Tex("Region2").next_to(dot7).shift(UP*0.5).scale(0.5)
        region3=Tex("Region3").next_to(dot8).shift(UP*0.5).scale(0.5)
        region4=Tex("Region4").next_to(dot6).shift(DOWN*0.5+LEFT*2).scale(0.5)

        region5=Tex("Region1").next_to(dot3).shift(DOWN*1.5+LEFT*2).scale(0.5)
        region6=Tex("Region2").next_to(dot2).shift(DOWN*0.5).scale(0.5)
        region7=Tex("Region3").next_to(dot2).shift(DOWN*0.5+LEFT*2).scale(0.5)
        region8=Tex("Region4").next_to(dot1).shift(DOWN*1.5+LEFT*0.5).scale(0.5)

        regions=VGroup(region1,region2,region3,region4,region5,region6,region7,region8)
        self.play(Write(regions),run_time=2)
        self.add(regions)

        mathtex1=MathTex("g_{xy}(i,j-1)").scale(0.5).next_to(dot4).shift(LEFT*2)
        mathtex2=MathTex("g_{down}(i,j)").scale(0.5).next_to(dotm2).shift(LEFT*2)
        mathtex3=MathTex("g_{xy}(i+1,j-1)").scale(0.5).next_to(dot7).shift(LEFT*2.5)

        mathtex4=MathTex("g_{xy}(i-1,j+1)").scale(0.5).next_to(dot3)
        mathtex5=MathTex("g_{up}(i,j)").scale(0.5).next_to(dotm2).shift(RIGHT*2)
        mathtex6=MathTex("g_{xy}(i,j+1)").scale(0.5).next_to(dot6)

        mathtex7=MathTex("g_{xy}(i,j)").scale(0.5).next_to(dotm3)
        mathtex8=MathTex("g_{x}(i,j)").scale(0.5).next_to(dot5)
        mathtex9=MathTex("g_{y}(i,j)").scale(0.5).next_to(dotm4)
        mathtex10=MathTex(r"t = \frac{|g_{y}(i,j)|}{|g_{x}(i,j)|}").scale(0.5).next_to(dot6).shift(UP*0.5)
        mathtexs=VGroup(mathtex1,mathtex2,mathtex3,mathtex4,mathtex5,mathtex6,mathtex7,mathtex8,mathtex9,mathtex10)
        self.play(Write(mathtexs),run_time=2)
        self.add(mathtexs)

