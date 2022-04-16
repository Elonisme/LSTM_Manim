from manim import *
from sklearn.preprocessing import scale
from torch import lstm

class axes(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[0,10,2],
            y_range=[0,10,2],
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers":True,
                "font_size":30,
                "include_tip":True,
                "numbers_to_exclude":[0],
                "numbers_with_elongated_ticks":[0,2]
            }
        )

        self.add(ax)

        LSTMlearn1 = Tex("前125次的学习率设置为0.0005，后125次的学习率设置为0.25。")
        self.play(Write(LSTMlearn1))
        self.play(FadeOut(LSTMlearn1))

        REMSE = Tex("训练结束后，将预测数据与测试数据进行对比，计算根均方差，结果如下。")
        self.play(Write(REMSE))
        self.play(FadeOut(REMSE))
        REMSEImage = ImageMobject(r"ForecasetWithUpdates.png").scale(0.7)
        self.play(FadeIn(REMSEImage))
        self.play(FadeOut(REMSEImage))

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


