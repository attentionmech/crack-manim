from manim import *

class AnimatingMultipleTexts(Scene):
    def construct(self):
        # Create text objects
        text1 = Text("Hello,").shift(UP)
        text2 = Text("World!").shift(DOWN)

        # Animate the text objects
        self.play(Write(text1))
        self.play(Write(text2))

        # Synchronize animations
        self.play(
            text1.animate.shift(LEFT),
            text2.animate.shift(RIGHT)
        )

        # Wait for a moment
        self.wait(1)

        # Fade out the text objects
        self.play(
            FadeOut(text1),
            FadeOut(text2)
        )