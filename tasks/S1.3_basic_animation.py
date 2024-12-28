from manim import *

class BasicAnimation(Scene):
    def construct(self):
        square = Square()

        self.play(
            square.animate.shift(RIGHT * 2),  # Move to the right
        )
        
        self.play(
            square.animate.rotate(PI/4)
        )
        
        self.play(
            square.animate.scale(2)
        )

        self.wait(5)