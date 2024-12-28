from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, World!")
        self.play(Write(text))
        self.wait(2)