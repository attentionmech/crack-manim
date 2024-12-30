from manim import *

class ForceVectors(Scene):
    def construct(self):
        # Create an object (a circle for example)
        object_circle = Circle(radius=0.5, color=BLUE).shift(LEFT * 2)
        object_label = Text("Object").scale(0.5).next_to(object_circle, DOWN)

        # Add the object to the scene
        self.play(Create(object_circle), Write(object_label))
        
        # Create force vectors (arrows)
        force_1 = Arrow(start=object_circle.get_center(),
                        end=object_circle.get_center() + RIGHT * 2,
                        color=RED, buff=0)
        force_label_1 = MathTex("F_1").scale(0.6).next_to(force_1, UP)

        force_2 = Arrow(start=object_circle.get_center(),
                        end=object_circle.get_center() + UP * 1.5,
                        color=GREEN, buff=0)
        force_label_2 = MathTex("F_2").scale(0.6).next_to(force_2, RIGHT)

        # Animate forces appearing
        self.play(GrowArrow(force_1), Write(force_label_1))
        self.play(GrowArrow(force_2), Write(force_label_2))
        
        # Simulate a resulting force
        resultant_force = Arrow(start=object_circle.get_center(),
                                 end=object_circle.get_center() + RIGHT * 1.5 + UP * 1,
                                 color=YELLOW, buff=0)
        resultant_label = MathTex("F_{\\text{resultant}}").scale(0.6).next_to(resultant_force, UP)

        # Animate the resultant force
        self.play(GrowArrow(resultant_force), Write(resultant_label))

        # Add a brief pause for clarity
        self.wait(2)

        # Cleanup the scene
        self.play(FadeOut(force_1, force_label_1, force_2, force_label_2, resultant_force, resultant_label, object_circle, object_label))
