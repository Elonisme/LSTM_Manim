from email.mime import application
from gzip import WRITE
from tkinter import CENTER, font
from typing_extensions import runtime
from manim import *
from matplotlib import animation, image, transforms
from matplotlib.pyplot import table
from scipy.fftpack import shift
from torch import set_flush_denormal
import werkzeug

class ComputerProject(Scene):

    def construct(self):
        '''开头'''
        self.add_sound(r"bgm\begining.mp3")
        title = Tex(r"$TOPSIS$环境评价及\\$PM_{2.5}$含量LSTM神经网络预测模型", tex_template=TexTemplateLibrary.ctex,color=BLUE,font_size=50).shift(DOWN*2.5)
        nomo =Tex("Environmental Index Evaluation and Prediction Model",color=BLUE,font_size=20)
        VGroup(title,nomo).arrange(DOWN*2)
        img =ImageMobject('Xihua_University_logo.png').shift(UP)

        self.wait(2)
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

        '''内容部分'''
        section1 = Tex("项目介绍", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section1))
        self.wait()
        self.play(
            FadeOut(section1)
            )

        algorithm = Tex(r"采用方法\\熵权法\\TOPSIS综合评价法\\LSTM神经网络", tex_template=TexTemplateLibrary.ctex, font_size=40)
        language= Tex(r"采用语言MatLab进行编程", tex_template=TexTemplateLibrary.ctex, font_size=40).move_to(algorithm).shift(DOWN*2)
        AL = VGroup(algorithm,language).shift(UP*0.5)
        self.play(Write(AL))
        self.wait(2)
        self.play(FadeOut(AL))

        section3 = Tex("熵权法", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section3))
        self.wait()
        self.play(
            FadeOut(section3)
            )
        section3.font_size=20
        section3.to_edge(LEFT+UP*2.5)

        self.play(FadeIn(section3))
        Entropy = Tex(r"熵权法是一个客观的赋权方法,可以最大程度上避免主观性赋权对于环境指标量化结果的影响。熵权法权法依据的原理是指标的变异程度，即变异程度越高则对应的权值也就越高。", tex_template=TexTemplateLibrary.ctex, font_size=35)
        EntropyTex1 = Tex(r"首先需要对环境指标数据进行正向化和归一化处理\\其中$z_{ij}$为归一化处理后的变量, $x_{min}$和$x_{max}$分别为每个指标的最大值和最值", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        EntropyMath1 = MathTex(r"z_{ij}=\frac{x_{ij}-x_{min}}{x_{max}-x_{min}}", font_size=20).move_to(EntropyTex1).shift(DOWN)

        EntropyTex2 = Tex(r"第j个环境指标下第i个年份所占权重，将其看作计算信息熵时的概率$p_{ij}$", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        EntropyMath2 = MathTex(r"p_{ij}=\frac{z_{ij}}{\sum_{i=1}^{n}z_{ij}}", font_size=20).move_to(EntropyTex2).shift(DOWN)

        EntropyTex3 = Tex(r"计算第j个环境指标的信息熵$e_j$ ，并计算对应信息效用值$d_j$ ", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        EntropyMath3 = MathTex(r"e_j=-\frac{1}{ln{n}}\sum_{i=1}^{n}{ln{(}p_{ij})}", font_size=20).move_to(EntropyTex3).shift(DOWN)
        EntropyTex4 = Tex(r"此处进行转换的原因是因为信息熵越大代表该环境指标的信息越少，引入$d_j$就可以正向衡量信息量。", tex_template=TexTemplateLibrary.ctex, font_size=35).move_to(EntropyMath3).shift(DOWN)
        EntropyMath4 = MathTex(r"d_j=1-e_j", font_size=20).move_to(EntropyTex4).shift(DOWN)

        EntropyTex5 = Tex(r"最终归一化得到每个环境评价指标的熵权$w_j$", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        EntropyMath5 = MathTex(r"w_j=\frac{d_j}{\sum_{j=1}^{m}d_j}", font_size=20).move_to(EntropyTex5).shift(DOWN)

        MathGruop4 = VGroup(
            EntropyTex1,
            EntropyMath1
        )
        MathGruop5 = VGroup(
            EntropyTex2,
            EntropyMath2
        )
        MathGruop6 = VGroup(
            EntropyTex3,
            EntropyMath3,
            EntropyTex4,
            EntropyMath4
        )
        # MathGruop7 = VGroup(
        #     EntropyTex5,
        #     EntropyMath5
        # )
        self.play(Write(Entropy),run_time = 2)
        self.wait(2)
        self.play(FadeOut(Entropy))

        self.play(
            Write(MathGruop4),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop4))
        
        self.play(
            Write(MathGruop5),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop5))

        self.play(
            Write(MathGruop6),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop6))

        self.play(
            Write(EntropyTex5),
            Write(EntropyMath5),
            run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(EntropyTex5),
            FadeOut(EntropyMath5)
            )

        self.play(FadeOut(section3))
        EntropyText6 = Tex("计算得到权重如下：", tex_template=TexTemplateLibrary.ctex, font_size=35)
        self.play(
            Write(EntropyText6),
            FadeOut(EntropyText6)
            )

        quanzhong = Table(
            [["0.0561", "0.0561","0.2198","0.2309","0.2198","0.2198"]],
            row_labels=[Text("Weights")],
            col_labels=[Text("森林覆盖率"), Text("森林覆盖面积"),Text("林木面积"),Text("涵养水量"),Text("二氧化碳吸收量"),Text("氧气释放量")],
            include_outer_lines=True)
        quanzhong.scale(0.4)
        self.play(quanzhong.create())
        self.wait(2)
        self.play(FadeOut(quanzhong))

        section2 = Tex("TOPSIS综合评价法", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section2))
        self.wait()
        self.play(
            FadeOut(section2),
            )
        section2.font_size=20
        section2.to_edge(LEFT+UP*2.5)
        self.play(FadeIn(section2))
        TOPSIS = Tex(r"TOPSIS法是用来处理指标决策问题的多方案排序和选择的方法,它的基本思想是:依据理想点的理论原理，\\找寻距离理想点最近的方案。并通过计算对象与最优解、最劣解的距离大小，确定顺序。即先设定一个\\ 虚拟的最优解（又称正理想解)和一个最劣解（又称负理想解)，将各备选方案与正负理想解相互比较，\\若方案最靠近最优解即又距最劣解最远, 为最好。TOPSIS方法需要的评价指标决策矩阵和指标权重,\\本项目由熵权法计算给出", tex_template=TexTemplateLibrary.ctex, font_size=20)
        
        TOPSISTex1 = Tex(r"每个环境指标的最大值，记为 ，组成向量:", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E).shift(UP)
        TOPSISMath1 = MathTex(r"z^+ ={z_ {1}^{+},  z_ {2}^ {+},\cdots,z_ {m}^ {+}}", font_size=20).move_to(TOPSISTex1).shift(DOWN)
        TOPSISTex2 =  Tex(r"该向量代表了环境最好的年份。同样的，找出每列也就是每个指标的最小值，记为,组成向量: 该向量代表了环境最差的年份.", tex_template=TexTemplateLibrary.ctex, font_size=20).move_to(TOPSISMath1).shift(DOWN)
        TOPSISMath2 = MathTex(r"z^- ={z_ {1}^{-},  z_ {2}^ {-},\cdots,z_ {m}^ {-}}", font_size=20).move_to(TOPSISTex2).shift(DOWN)


        TOPSISTex3 =  Tex(r"定义第i个年份与理想目标距离为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E).shift(UP)
        TOPSISMath3 = MathTex(r"D_i^+=\sqrt{\sum_{j=1}^{m}{w_j(z_j^+-z_{ij})^2}}", font_size=20).move_to(TOPSISTex3).shift(DOWN)
        TOPSISTex4 =  Tex(r"定义第i个年份与不理想目标距离为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E).move_to(TOPSISMath3).shift(DOWN)
        TOPSISMath4 = MathTex(r"D_i^-=\sqrt{\sum_{j=1}^{m}{w_j(z_j^--z_{ij})^2}}", font_size=20).move_to(TOPSISTex4).shift(DOWN)

        TOPSISTex5 =  Tex(r"定义第i个年份的得分为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E).shift(UP)
        TOPSISMath5 = MathTex(r"S_i=\frac{D_i^-}{D_i^++D_i^-}", font_size=20).move_to(TOPSISTex5).shift(DOWN)
        TOPSISTex6 = Tex(r" 当Si越接近于1，说明此年份i距离理想化目标越近,该年份环境就越好。反之，当 越接近于0，说明年份i距离理想化目标越远,该年份环境就越差.", tex_template=TexTemplateLibrary.ctex, font_size=20).move_to(TOPSISMath5).shift(DOWN)

        MathGruop1 = VGroup(
            TOPSISTex1,
            TOPSISMath1,
            TOPSISTex2,
            TOPSISMath2,
            )

        MathGruop2 = VGroup(
            TOPSISTex3,
            TOPSISMath3,
            TOPSISTex4,
            TOPSISMath4,
        )

        MathGruop3 = VGroup(
            TOPSISTex5,
            TOPSISMath5,
            TOPSISTex6
        )
        self.play(
            Write(TOPSIS)
            )
        self.wait(2)
        self.play(
            FadeOut(TOPSIS)
            )

        self.play(
            Write(MathGruop1),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop1))

        self.play(
            Write(MathGruop2),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop2))

        self.play(
            Write(MathGruop3),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop3))
        saihanba = Tex("计算后得塞罕坝历年的发展曲线", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(saihanba))
        self.wait(1)
        self.play(FadeOut(saihanba))


        saihanbapic = ImageMobject(r"saihanba.png").scale(0.9)
        self.play(
            FadeIn(saihanbapic)
            )
        self.wait(2)
        self.play(FadeOut(saihanbapic))

        demo1 = Tex("计算过程演示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(
            Write(demo1)
            )
        self.wait(1)
        self.play(FadeOut(demo1))

        self.play(FadeOut(section2))

        section4 = Tex("大气环境综合评价", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section4))
        self.wait()
        self.play(
            FadeOut(section4)
            )
        section4.font_size=20
        section4.to_edge(LEFT+UP*2.5)
        self.play(Write(section4))

        AQI = Tex(r"空气质量指数（Air Quality Index，简称AQI），是一个用来定量描述空气质量水平的数值。AQI的取值范围位于0-500 之间。环境空气污染物的种类有很多，参与AQI指数评价的有二氧化硫(SO2)、二氧化氮(NO2)、一氧化碳(CO)、臭氧(O3)、PM2.5、PM10。", tex_template=TexTemplateLibrary.ctex, font_size=35)
        self.play(Write(AQI))
        self.play(FadeOut(AQI))
        AQI2 = Tex(r"空气质量指数的值在不同的区间，就代表了不同的空气质量水平。比如0-50之间，代表良好；51-100之间，代表中等；101-150之间代表轻度污染等等。为了更直观起见，每个区间都有一个固定的颜色值与它对应：", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        AQIimg = ImageMobject(r"AQItable.png").move_to(AQI2).shift(DOWN*2)

        self.play(
            Write(AQI2),
            FadeIn(AQIimg)
            )
            
        self.wait(2)
        self.play(
            FadeOut(AQI2),
            FadeOut(AQIimg)
            )
        AQI25 = Tex(r"AQI的折算公式如下：", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        AQIMath = MathTex(r"I=\frac{I_{high}-I_{low}}{C_{high}-C_{low}}(C-C_{low})+I_{low})", font_size=20).move_to(AQI25).shift(DOWN)
        AQI3 = Tex(r"其中I等于空气质量指数，即AQI，输出值；C为污染物浓度，输入值； $C_{low}$为小于或等于C的浓度限值； $C_{high}$为大于或等于C的浓度限值； $I_{low}$对应于$C_{low}$的指数限值；$I_{high}$为对应于$C_{high}$的指数限值。", tex_template=TexTemplateLibrary.ctex, font_size=35).move_to(AQIMath).shift(DOWN)
        AQIGruop2 = VGroup(
            AQI25,
            AQIMath,
            AQI3
        )
        self.play(Write(AQIGruop2))
        self.wait(2)
        self.play(FadeOut(AQIGruop2))

        Evaluation = Tex(r"利用熵权法和TOPSIS模糊综合评价计算出全中国各个省份的大气质量评价值，\\并绘制出各省环境质量排名图", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        self.play(Write(Evaluation))
        self.wait(2)
        self.play(FadeOut(Evaluation))

        Rangeimg = ImageMobject(r"geshengpaiming.png").scale(1.5)
        self.play(
            FadeIn(Rangeimg)
            )
        self.wait(2)
        self.play(FadeOut(Rangeimg))

        MatlabMap = Tex("使用Matlab将排名进行可视化，得到热力图", tex_template=TexTemplateLibrary.ctex, font_size=35)
        self.play(
            Write(MatlabMap)
            )
        self.wait(2)
        self.play(FadeOut(MatlabMap))


        ChinaMap = ImageMobject(r"ChinaMap.png").scale(0.7)
        MapExplain = Tex(r"从热力图中可以看出我国南方地区普遍空气质量较好，\\除开新疆沙漠的原因导致的气候异常，\\华北平原和华中平原目前属于环境空气污染较为严重的地区。", tex_template=TexTemplateLibrary.ctex, font_size=35)
        self.play(
            FadeIn(ChinaMap),
            )
        self.wait(2)
        self.play(
            FadeOut(ChinaMap),
            )
        self.play(FadeIn(MapExplain))
        self.play(FadeOut(MapExplain))

        self.play(FadeOut(section4))

        demo1 = Tex("计算过程演示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(
            Write(demo1)
            )
        self.wait(1)
        self.play(FadeOut(demo1))
        self.wait(4)


        section5 = Tex("空气质量变化预测分析", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section5))
        self.wait()
        self.play(
            FadeOut(section5)
            )
        section5.font_size=20
        section5.to_edge(LEFT+UP*2.5)
        self.play(Write(section5))
        self.play(FadeOut(section5))
        analyze = Tex(r"本文使用了了China-OPenAQ的Beijing US Embassy项目中北京市朝阳区50764数据，\\清洗后的数据如下图所示。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(analyze))
        self.wait(2)
        self.play(FadeOut(analyze))
        clearPM25 = ImageMobject("DailyPM25ofhickenpoxeps.png").scale(0.3)
        self.play(FadeIn(clearPM25))
        self.wait(2)
        self.play(FadeOut(clearPM25))
        analyze2 = Tex("将清洗后的数据使用中国气象局的标准转换为空气质量指标，并绘制饼图", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(analyze2))
        self.wait(2)
        self.play(FadeOut(analyze2))
        bar = ImageMobject("pie.png").scale(0.3)
        self.play(FadeIn(bar))
        self.wait(2)
        self.play(FadeOut(bar))

        self.play(FadeOut(section5))


        section6 = Tex("RNN神经网络介绍", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section6))
        self.wait()
        self.play(
            FadeOut(section6)
            )
        section6.font_size=20
        section6.to_edge(LEFT+UP*2.5)
        self.play(Write(section6))

        RNN1 = Tex(r"处理与事件发生的时间轴有关系的问题时，比如自然语言处理，文本处理，文字的上下文是有一定的关联性的；时间序列数据，如连续几天的气状况，当日的天气情况与过去的几天有某些联系；又比如语音识别，机器翻译等。在考虑这些和时间轴相关的问题时，传统的神经网络就无能为力了", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(RNN1))
        self.play(FadeOut(RNN1))
        RNN2 = Tex(r"RNN之所以被称为循环神经网络是因为一个序列的输出与前一时刻的输出有关，前面数据信息会影响后一个输出，隐含层的节点是相互关联的。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(RNN2))
        self.play(FadeOut(RNN2))
        RNN3 = Tex(r"RNN的结构如下", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(RNN3))
        self.play(FadeOut(RNN3))
        RNNPicture = ImageMobject("RNMNetStructural.png")
        self.play(FadeIn(RNNPicture))
        self.play(FadeOut(RNNPicture))

        self.play(FadeOut(section6))
        

        section7 = Tex("LSTM神经网络介绍", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section7))
        self.wait()
        self.play(
            FadeOut(section7)
            )
        section6.font_size=20
        section6.to_edge(LEFT+UP*2.5)

        LSTM1 = Tex(r"长短期记忆(Long short-term memory,LSTM)是一种改进的RNN,主要是为了解决长序列训练过程中的梯度消失和梯度爆炸问题。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTM1))
        self.play(FadeOut(LSTM1))
        LSTM2 = Tex(r"LSTM中将网络的状态分为内部状态和外部状态两种。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTM2))
        self.play(FadeOut(LSTM2))
        LSTM3 = Tex(r"LSTM的外部状态类似于一般结构的循环神经网络中的状态，即该状态既是当前时刻隐藏层的输出，也是下一时刻隐藏层的输入。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTM3))
        self.play(FadeOut(LSTM3))
        LSTM4 = Tex(r"LSTM的内部结构如下", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTM4))
        self.play(FadeOut(LSTM4))
        LSTMPicture =ImageMobject("LSTMNetStructural.png")
        self.play(FadeIn(LSTMPicture))
        self.play(FadeOut(LSTMPicture))

        self.play(Unwrite(section7))

        section8 = Tex("LSTM神经网络实时预测", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section8))
        self.wait()
        self.play(
            FadeOut(section8)
            )
        section8.font_size=20
        section8.to_edge(LEFT+UP*2.5)
        self.play(Write(section8))

        IntroLSTM = Tex("实时预测LSTM神经网络结构如下所示", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(IntroLSTM))
        self.play(FadeOut(IntroLSTM))
        lstmSturcut1 = Table(
            [["1"],
            ["200"],
            ["200"],
            ["0.2"],
            ["200"],
            ["1"],
            ["1"]],
            row_labels=[Text("Input Layer"),Text("Fully Connected Layer"),Text("LSTM Layer"),Text("Dropout Layer"),Text("Fully Connected Layer"),Text("Fully Connected Layer"),Text("Regression Layer")],
            col_labels=[Text("LSTM Struct")],
            include_outer_lines=True).scale(0.3)
        self.play(lstmSturcut1.create())
        self.wait(2)
        self.play(FadeOut(lstmSturcut1))

        LSTMlearn1 = Tex("本模型共训练250次,前125次的学习率设置为0.0005，后125次的学习率设置为0.25。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTMlearn1))
        self.play(FadeOut(LSTMlearn1))

        REMSE = Tex("训练结束后，将预测数据与测试数据进行对比，计算根均方差，结果如下。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        REMSE1rs = Tex("$REMS=0.2889$").move_to(REMSE).shift(DOWN)
        self.play(
            Write(REMSE),
            Write(REMSE1rs))
        self.wait()
        self.play(
            FadeOut(REMSE),
            FadeOut(REMSE1rs)
            )
        REMSEImage = ImageMobject(r"ForecasetWithUpdates.png").scale(0.3)
        self.play(FadeIn(REMSEImage))
        self.wait(2)
        self.play(FadeOut(REMSEImage))

        Result1 = Tex("计算结果如表格所示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(Result1))
        self.play(FadeOut(Result1))
        P24table = Table(
            [["优", "优"],
            ["优","优"],
            ["优","优"],
            ["优","优"],
            ["...","..."],
            ["优","优"],
            ["优","优"],
            ["优","优"],
            ["优","优"]
            ],
            row_labels=[Text("第1个小时"),Text("第2个小时"),Text("第3个小时"), Text("第4个小时"),Text("..."),Text("第21个小时"), Text("第22个小时"),Text("第23个小时"),Text("第24个小时")],
            col_labels=[Text("C1"), Text("C2")],
            include_outer_lines=True).scale(0.3)
        self.play(P24table.create())
        self.wait(2)
        self.play(FadeOut(P24table))


        self.play(FadeOut(section8))
        #demo1 = Tex("计算过程演示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(
            Write(demo1)
            )
        self.wait()
        self.play(FadeOut(demo1))
        self.wait(4)

        section9 = Tex("LSTM神经网络72小时预测", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(section9))
        self.wait()
        self.play(
            FadeOut(section9)
            )
        section9.font_size=20
        section9.to_edge(LEFT+UP*2.5)
        self.play(Write(section9))

        #IntroLSTM = Tex("实时预测LSTM神经网络结构如下所示", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        self.play(Write(IntroLSTM))
        self.play(FadeOut(IntroLSTM))

        lstmSturcut2 = Table(
            [["1"],
            ["200"],
            ["200"],
            ["0.2"],
            ["200"],
            ["1"],
            ["1"]],
            row_labels=[Text("Input Layer"),Text("Fully Connected Layer"),Text("LSTM Layer"),Text("Dropout Layer"),Text("Fully Connected Layer"),Text("Fully Connected Layer"),Text("Regression Layer")],
            col_labels=[Text("LSTM Struct")],
            include_outer_lines=True).scale(0.3)
        self.play(lstmSturcut2.create())
        self.wait(2)
        self.play(FadeOut(lstmSturcut2))

        LSTMlearn2 = Tex("本模型共训练100次,前50次的学习率设置为0.0005，后50次的学习率设置为0.25。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(LSTMlearn2))
        self.play(FadeOut(LSTMlearn2))

        REMSE2 = Tex("训练结束后，将预测数据与测试数据进行对比，计算根均方差，结果如下。", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        REMSE2rs = Tex("$REMS=0.8862$").move_to(REMSE2).shift(DOWN)
        self.play(
            Write(REMSE2),
            Write(REMSE2rs)
            )
        self.play(
            FadeOut(REMSE2),
            FadeOut(REMSE2rs)
            )
        REMSEImage = ImageMobject(r"untide2.png").scale(0.3)
        self.play(FadeIn(REMSEImage))
        self.wait(2)
        self.play(FadeOut(REMSEImage))

        Result1 = Tex("计算结果如表格所示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(Write(Result1))
        self.play(FadeOut(Result1))

        P72table = Table(
            [["优", "优"],
            ["优","优"],
            ["优","优"],
            ["优","优"],
            ["...","..."],
            ["轻度污染","暂无数据"],
            ["轻度污染","暂无数据"],
            ["轻度污染","暂无数据"],
            ["轻度污染","暂无数据"]
            ],
            row_labels=[Text("第1个小时"),Text("第2个小时"),Text("第3个小时"), Text("第4个小时"),Text("..."),Text("第69个小时"), Text("第70个小时"),Text("第71个小时"),Text("第72个小时")],
            col_labels=[Text("预测空气质量"), Text("实际空气质量")],
            include_outer_lines=True).scale(0.3)
        self.play(P72table.create())
        self.wait(2)
        self.play(FadeOut(P72table))

        self.play(FadeOut(section9))
        #demo1 = Tex("计算过程演示", tex_template=TexTemplateLibrary.ctex, font_size=35, color=RED_E)
        self.play(
            Write(demo1)
            )
        self.wait()
        self.play(FadeOut(demo1))
        self.wait(4)

        # gray = Tex(r"一次累加生成序列：
        # ", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        # GrayMath = MathTex("x^{(0)}=(x^{(0)}(1),x^{(0)}(2),...,x^{(0)}(10))", font_size=20).move_to(gray).shift(DOWN)
        # AQIGruop3 = VGroup(
        #     gray,
        #     GrayMath
        # )
        # self.play(Write(AQIGruop3))
        # self.wait(2)
        # self.play(FadeOut(AQIGruop3))
        # gray2 = Tex(r"$x^{(1)}$的均值生成序列", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        # GrayMath2 = MathTex("z^{(1)}=(z^{(1)}(2),z^{(1)}(3),...,z^{(1)}(n))", font_size=20).move_to(gray2).shift(DOWN)
        # AQIGruop4 = VGroup(
        #     gray2,
        #     GrayMath2
        # )
        # self.play(Write(AQIGruop4))
        # self.wait()
        # self.play(FadeOut(AQIGruop4))
        # Garymin = Tex(r"建立灰微分方程", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP*2)
        # GarymimMath = MathTex("x^{(0)}(k)+az^{(1)}(k)=b,k=2,3,...,10", font_size=20).move_to(Garymin).shift(DOWN)
        # Whitemin = Tex(r"建立白微分方程", tex_template=TexTemplateLibrary.ctex, font_size=35).move_to(GarymimMath).shift(DOWN)
        # WhiteminMath = MathTex(r"\frac{dx^{(1)}}{dt}+ax^{(1)}(t)=b", font_size=20).move_to(Whitemin).shift(DOWN)
        # AQIGruop5 = VGroup(
        #     Garymin,
        #     GarymimMath,
        #     Whitemin,
        #     WhiteminMath
        # )
        # self.play(Write(AQIGruop5))
        # self.wait()
        # self.play(FadeOut(AQIGruop5))
        
        # GRAYMath3 = Tex(r"于是得到方程：", tex_template=TexTemplateLibrary.ctex, font_size=35).shift(UP)
        # GRAYMath3Model = MathTex(r"\hat{x}(k+1)=(x^{(0)}(1)-\frac{\hat{b}}{\hat{a}})e^{-\hat{a}k}+\frac{\hat{b}}{\hat{a}},k=0,1,...,10", font_size=20).move_to(GRAYMath3).shift(DOWN)
        # AQIGruop6 = VGroup(
        #     GRAYMath3,
        #     GRAYMath3Model
        # )
        # self.play(Write(AQIGruop6))
        # self.wait()
        # self.play(FadeOut(AQIGruop6))
        # GaryResult = Tex(r"计算得到发展系数$a_1=\mathrm{0.0119639}$ 灰色作用量$b_1=\mathrm{95.7210532}$ ", tex_template=TexTemplateLibrary.ctex, font_size=35)
        # self.play(Write(GaryResult))
        # self.wait()
        # self.play(FadeOut(GaryResult))

        # self.play(FadeOut(section4))
        

        # SceneFileWriter.get_resolution_directory(r"media\videos\NetWorks\2160p60\mynetwork.mp4")

        # section5 = Tex("BP神经网络预测", tex_template=TexTemplateLibrary.ctex, font_size=40, color=RED_E)
        # self.play(Write(section5))
        # self.wait()
        # self.play(
        #     FadeOut(section5)
        #     )
        # section5.font_size=20
        # section5.to_edge(LEFT+UP*2.5)
        # self.play(FadeIn(section5))
       
        # self.play(FadeOut(section5))


        '''结尾'''

        self.add_sound(r"bgm\ending.mp3")

        support = Tex(r"This video is supported by",font_size=40).shift(UP)
        Latexbird = ImageMobject(r"latexbird.jpg").move_to(support).shift(DOWN+LEFT).scale(0.35)
        Latex = Tex(r"\LaTeX",font_size = 40).move_to(Latexbird).shift(DOWN)

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
        referencesTop = Title("References",include_underline=False).align_to(CENTER).to_edge(UP)
        references = Tex(
            r"\\(1)The Manim Community v0.15.0 Reference Manual\\",
            r"\\(2)李丽. 基于数据挖掘的城市环境空气质量决策支持系统设计与实现[D].山东师范大学,2006.\\",
            r"\\(3)马媛媛,孙世群.模糊综合评价在合肥市大气环境评价中的应用[J].环境科学与管理,2012,37(05):188-191.\\",
            r"\\(4)Endah Kristiani, Hao Lin, Jwu-Rong Lin, Yen-Hsun Chuang, Chin-Yin Huang and Chao-Tung Yang.5Short-Term Prediction of $PM_{2.5}$ Using LSTM Deep Learning Methods[J].Sustainability 2022, 14, 2068.\\",
            r"\\(5)金文彪,姚永杰,金哲植.基于主成分分析的大气环境预测研究[J].科教导刊(中旬刊),2016(32):148-150.DOI:10.16400/j.cnki.kjdkz.2016.11.071.\\",
            r"\\(6)北京大学统计科学中心，北京大学光华管理学院.北京城区2010-2014年$PM_{2.5}$污染状况研究[J].2015.3.\\",
            r"\\(7)邬红娟,林子扬,郭生练.人工神经网络方法在资源与环境预测方面的应用[J].长江流域资源与环境,2000(02):237-241.\\",
            r"\\(8)袁冲.基于熵权法的江苏省各市经济高质量发展评价分析[J].商业经济,2022(04):19-20+42.DOI:10.19905/j.cnki.syjj1982.2022.04.061.\\",
            r"\\(9)杨悦,杨森,杨放晴,陈鸿平,陈林,刘友平.熵权 TOPSIS 模型在竹叶花椒药材质 量 综 合 评 价 中 的 应 用 [J]. 成 都 中 医 药 大 学 学 报 ,2022,45(01):5-10.DOI:10.13593/j.cnki.51-1501/r.2022.01.005.\\",
            tex_template=TexTemplateLibrary.ctex,
            font_size=20).shift(DOWN)
             
        # referencesTop.move_to(references[0]).shift(UP)
        references[0].next_to(referencesTop,DOWN)
        references[1].next_to(references[0],DOWN)
        references[2].next_to(references[1],DOWN)
        references[3].next_to(references[2],DOWN)
        references[4].next_to(references[3],DOWN,aligned_edge=LEFT)
        references[5].next_to(references[4],DOWN,aligned_edge=LEFT)
        references[6].next_to(references[5],DOWN,aligned_edge=LEFT)
        references[7].next_to(references[6],DOWN,aligned_edge=LEFT)
        references[8].next_to(references[7],DOWN,aligned_edge=LEFT)

        
        teamTop = Tex("成员名单",tex_template=TexTemplateLibrary.ctex,font_size =40)
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
            FadeOut(Latex),
            FadeOut(Latexbird),
            Uncreate(Manimlogo),
            FadeOut(Manim),
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