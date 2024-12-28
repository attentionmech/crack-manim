from manim import *

class BasicTransitions(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(square.animate.shift(RIGHT))
        self.play(Rotate(square, angle=PI/4))
        self.play(square.animate.set_fill(RED, opacity=0.5))
        self.play(square.animate.scale(2))
        self.play(FadeOut(square))
        
        self.play(FadeIn(square))
        self.play(square.animate.scale(0.5))
        self.play(square.animate.set_fill(BLACK, opacity=0.0))
        self.play(Rotate(square, angle=3*PI/4))
        self.play(square.animate.shift(LEFT))
        self.play(FadeOut(square))
        

