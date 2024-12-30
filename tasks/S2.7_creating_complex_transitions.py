from manim import *

class ComplexTransitions(Scene):
    def construct(self):
        # Create some objects
        square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT)
        circle = Circle(color=RED, fill_opacity=0.5).shift(RIGHT)
        
        # Display objects
        self.play(Create(square), Create(circle))
        self.wait(1)
        
        # Apply some transformations
        self.play(square.animate.shift(RIGHT * 2), circle.animate.shift(LEFT * 2))
        self.wait(1)
        
        # Rotate and change color
        self.play(Rotate(square, angle=PI/4), circle.animate.set_fill(YELLOW))
        self.wait(1)
        
        # Fade out and scale down
        self.play(FadeOut(square), circle.animate.scale(0.5))
        self.wait(1)

        # Bring back the square with a different color and position
        new_square = Square(color=GREEN, fill_opacity=0.5).shift(UP)
        self.play(FadeIn(new_square))
        self.wait(1)
        
        # Apply combined transformations
        self.play(new_square.animate.shift(DOWN * 2).rotate(PI/2).set_fill(PURPLE))
        self.wait(1)
        
        # Final fade out
        self.play(FadeOut(new_square), FadeOut(circle))
        self.wait(1)