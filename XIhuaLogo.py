from manim import *

class XihuaLogo(Scene):
    config = {
    "camera_config":{"background_color": "#ffffff"}
    } 
    def construct(self):
        logo = ImageMobject(r"Xihua_University_logo.png").shift(UP*0.5)
        title = Tex(r"Environmental Assessment \\and Prediction System").move_to(logo).shift(DOWN)
        self.add(logo)
        self.add(title)

