from manim import *

class AnimatingWithTime(Scene):
    def construct(self):
        # Create a ValueTracker to keep track of time
        time_tracker = ValueTracker(0)

        # Create a circle
        circle = Circle()

        # Create a dot that will move along the circumference of the circle
        dot = Dot()
        dot.move_to(circle.point_from_proportion(0))

        # Update the dot's position based on the time tracker
        dot.add_updater(lambda d: d.move_to(circle.point_from_proportion(time_tracker.get_value() % 1)))

        # Add the circle and dot to the scene
        self.add(circle, dot)

        # Animate the time tracker from 0 to 1 over 5 seconds
        self.play(time_tracker.animate.set_value(1), run_time=5, rate_func=linear)

        # Keep the final frame for a moment
        self.wait()