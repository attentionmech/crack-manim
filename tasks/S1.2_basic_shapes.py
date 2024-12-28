from manim import *

class BasicShapes(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # Create a square
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=1)

        # Create text
        text = Text("Hello, Manim!")
        text.next_to(square, DOWN, buff=1)

        # Add shapes and text to the scene
        self.play(Create(circle), Create(square), Write(text))
        
        self.wait(2)
        
        # do em in separate order
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Write(text))
        
        self.wait(2)