from manim import *
from manim import config

class EasingFunctions(Scene):
    def construct(self):
        dot = Dot().set_color(RED)
        self.add(dot)

        # Linear movement
        self.play(dot.animate.shift(RIGHT * 4), run_time=2, rate_func=linear)
        self.wait(1)

        # Smooth movement
        self.play(dot.animate.shift(LEFT * 4), run_time=2, rate_func=smooth)
        self.wait(1)

        # Slow into fast movement
        self.play(dot.animate.shift(RIGHT * 4), run_time=2, rate_func=there_and_back)
        self.wait(1)

        # Fast into slow movement
        self.play(dot.animate.shift(LEFT * 4), run_time=2, rate_func=there_and_back_with_pause)
        self.wait(1)

        # Bounce movement
        self.play(dot.animate.shift(RIGHT * 4), run_time=2, rate_func=running_start)
        self.wait(1)

        # Elastic movement
        self.play(dot.animate.shift(LEFT * 4), run_time=2, rate_func=rate_functions.ease_in_elastic)
        self.wait(1)

