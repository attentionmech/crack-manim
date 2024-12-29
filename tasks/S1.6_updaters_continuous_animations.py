from manim import *
import numpy as np

class UpdatersAndContinuousAnimations(Scene):
    def construct(self):
        # Create a dot
        dot = Dot()
        self.add(dot)

        # Create a traced path for the dot
        path = TracedPath(dot.get_center, stroke_color=[YELLOW,RED], stroke_width=8)
        self.add(path)

        # Define an updater function to move the dot in a sine wave path
        def update_dot(mob, dt):
            mob.shift(RIGHT * dt)
            mob.shift(UP * np.sin(10*mob.get_center()[0])/50)

        # Add the updater to the dot
        dot.add_updater(update_dot)

        # Wait for a moment to observe the animation
        self.wait(10)

        # Remove the updater
        dot.remove_updater(update_dot)

        # Fade out the dot and the path
        self.play(FadeOut(dot), FadeOut(path))
