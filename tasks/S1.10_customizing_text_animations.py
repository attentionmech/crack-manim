from manim import *

class CustomizingTextAnimations(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello, Manim!", font_size=48)
        
        # Add the text to the scene with a typing effect
        self.play(Write(text))
        self.wait(1)
        
        # Apply a rotation animation
        self.play(Rotate(text, angle=PI/4))
        self.wait(1)
        
        # Apply a color change animation
        self.play(text.animate.set_color(RED))
        self.wait(1)
        
        # Fade out the text
        self.play(FadeOut(text))
        self.wait(1)

        # Create another text object
        text2 = Text("Customizing Text Animations", font_size=36)
        
        # Add the text to the scene with a typing effect
        self.play(Write(text2))
        self.wait(1)
        
        # Apply a scale animation
        self.play(text2.animate.scale(1.5))
        self.wait(1)
        
        # Apply a move animation
        self.play(text2.animate.shift(UP*2))
        self.wait(1)
        
        # Apply a color gradient animation
        self.play(text2.animate.set_color_by_gradient(BLUE, GREEN))
        self.wait(1)
        
        # Fade out the text
        self.play(FadeOut(text2))
        self.wait(1)
