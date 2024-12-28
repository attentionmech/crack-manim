from manim import *

class UnderstandingScene(Scene):
    def construct(self):
        # Title of the animation to explain the Scene class
        title = Text("Understanding the Scene Class").scale(0.8)
        title.to_edge(UP)

        # Explanation of the Scene class
        scene_explanation = Text(
            "The Scene class is the heart of every Manim animation.\n"
            "It defines the setup, components, and animation process."
        ).next_to(title, DOWN).scale(0.5)

        # Display the title and explanation
        self.play(Write(title))
        self.play(Write(scene_explanation))

        # Pause for a while to let the audience absorb the info
        self.wait(2)

        # Breakdown of components of a Scene
        component_title = Text("Components of a Scene").scale(0.8).next_to(scene_explanation, DOWN)
        self.play(Write(component_title))

        # List of components
        component_list = VGroup(
            Text("1. construct method"),
            Text("2. Mobjects (Mathematical Objects)"),
            Text("3. Animations"),
            Text("4. Scene Setup")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(component_title, DOWN).scale(0.5)

        self.play(LaggedStartMap(Write, component_list, lag_ratio=0.5))

        # Pause to show the components
        self.wait(2)

        # Explanation of the 'construct' method
        construct_explanation = Text(
            "'construct' method is where you define the sequence of animations."
        ).next_to(component_list, DOWN).scale(0.5)

        self.play(Write(construct_explanation))
        self.wait(2)

        # Create a simple animation within the construct method
        square = Square()
        self.play(Create(square))  # Create animation

        # Move the square to a new position
        self.play(square.animate.shift(RIGHT * 2))

        # Fade out all elements to end the scene
        self.play(FadeOut(title, scene_explanation, component_title, component_list, construct_explanation, square))

        self.wait(1)

