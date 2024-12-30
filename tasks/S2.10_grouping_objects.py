from manim import *
from manim import config

class GroupingObjects(Scene):
    def construct(self):
        # Create some shapes
        circle = Circle().set_color(RED)
        square = Square().set_color(BLUE)
        triangle = Triangle().set_color(GREEN)

        # Position the shapes
        circle.shift(LEFT)
        square.shift(RIGHT)
        triangle.shift(UP)

        # Group the shapes together
        group = VGroup(circle, square, triangle)

        # Apply transformations to the group
        self.play(group.animate.shift(DOWN))
        self.play(group.animate.scale(0.5))
        self.play(group.animate.rotate(PI / 4))

        # Display the group
        self.play(FadeIn(group))
        self.wait(2)
        self.play(FadeOut(group))
