from manim import *

class AnimatingMultipleObjects(Scene):
    def construct(self):
        # Create objects
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # Position objects
        circle.to_edge(LEFT)
        square.to_edge(RIGHT)
        triangle.to_edge(DOWN)

        # Define updaters
        circle.add_updater(lambda m: m.set_fill(RED, opacity=0.5))
        square.add_updater(lambda m: m.set_fill(BLUE, opacity=0.5))
        triangle.add_updater(lambda m: m.set_fill(GREEN, opacity=0.5))

        # Create animations
        circle_animation = circle.animate.shift(RIGHT * 2)
        square_animation = square.animate.shift(LEFT * 2)
        triangle_animation = triangle.animate.shift(UP * 2)

        # Synchronize animations
        self.play(circle_animation, square_animation, triangle_animation)
        self.wait()

        # Remove updaters
        circle.clear_updaters()
        square.clear_updaters()
        triangle.clear_updaters()
        # Add individual animations
        self.play(circle.animate.rotate(PI), run_time=2)
        self.play(square.animate.scale(0.5), run_time=2)
        self.play(triangle.animate.shift(LEFT * 2), run_time=2)