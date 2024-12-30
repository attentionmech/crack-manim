from manim import *
from manim import config

class ColorTransition(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(square.animate.set_fill(RED, opacity=0.5))
        self.play(square.animate.set_fill(BLUE, opacity=0.5))
        self.play(square.animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeOut(square))

