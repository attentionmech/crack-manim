from manim import *

class AnimatingMultipleLayers(Scene):
    def construct(self):
        # Create different layers
        layer1 = VGroup()
        layer2 = VGroup()

        # Add objects to layer1
        square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT)
        circle = Circle(color=RED, fill_opacity=0.5).shift(RIGHT)
        layer1.add(square, circle)

        # Add objects to layer2
        triangle = Triangle(color=GREEN, fill_opacity=0.5).shift(UP)
        hexagon = RegularPolygon(n=6, color=YELLOW, fill_opacity=0.5).shift(DOWN)
        layer2.add(triangle, hexagon)

        # Add layers to the scene
        self.add(layer1, layer2)

        # Animate layer1
        self.play(
            square.animate.shift(RIGHT * 2),
            circle.animate.shift(LEFT * 2),
            run_time=2
        )

        # Animate layer2
        self.play(
            triangle.animate.shift(DOWN * 2),
            hexagon.animate.shift(UP * 2),
            run_time=2
        )

        # Animate both layers together
        self.play(
            layer1.animate.shift(UP * 2),
            layer2.animate.shift(DOWN * 2),
            run_time=2
        )

        self.play(
            layer1.animate.shift(LEFT * 2),
            layer2.animate.shift(RIGHT * 2),
            run_time=2
        )

        # Wait for a moment before ending the scene
        self.wait(2)