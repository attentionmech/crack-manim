from manim import *

class UnderstandingScene(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        square.next_to(circle, RIGHT)
        
        self.play(Create(circle), Create(square))
        self.wait(1)
        
        self.play(Transform(circle, square))
        self.wait(1)
        
        self.play(FadeOut(circle), FadeOut(square))
        self.wait(1)
        triangle = Triangle()
        triangle.set_fill(PINK, opacity=0.5)
        
        self.play(Create(triangle))
        self.wait(1)
        
        self.play(triangle.animate.shift(UP))
        self.wait(1)
        
        self.play(Rotate(triangle, angle=PI/4))
        self.wait(1)
        
        self.play(FadeOut(triangle))
        self.wait(1)
        