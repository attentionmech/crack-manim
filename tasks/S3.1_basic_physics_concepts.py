from manim import *

class BasicPhysicsConcepts(Scene):
    def construct(self):
        title = Text("Basic Physics Concepts").to_edge(UP)
        self.play(Write(title))
        
        velocity_text = Text("Velocity", font_size=36).shift(UP*2)
        velocity_formula = MathTex(r"v = \frac{d}{t}", font_size=36).next_to(velocity_text, DOWN)
        
        acceleration_text = Text("Acceleration", font_size=36).shift(DOWN*2)
        acceleration_formula = MathTex(r"a = \frac{\Delta v}{\Delta t}", font_size=36).next_to(acceleration_text, DOWN)
        
        self.play(Write(velocity_text))
        self.play(Write(velocity_formula))
        self.wait(2)
        
        self.play(Write(acceleration_text))
        self.play(Write(acceleration_formula))
        self.wait(2)
        
        self.play(FadeOut(velocity_text), FadeOut(velocity_formula), FadeOut(acceleration_text), FadeOut(acceleration_formula))
        
        # Velocity demonstration
        ball1 = Dot().set_color(RED).shift(LEFT*4)
        ball2 = Dot().set_color(BLUE).shift(LEFT*4 + DOWN)
        speed1 = Text("v1", font_size=24).next_to(ball1, UP)
        speed2 = Text("v2", font_size=24).next_to(ball2, UP)
        
        self.play(FadeIn(ball1), FadeIn(ball2), Write(speed1), Write(speed2))
        
        # Define updater functions for velocity
        v1 = 2  # units per second
        v2 = 4  # units per second
        ball1.add_updater(lambda b, dt: b.shift(RIGHT * v1 * dt))
        ball2.add_updater(lambda b, dt: b.shift(RIGHT * v2 * dt))
        
        self.wait(4)  # wait for 4 seconds to simulate the movement
        
        ball1.remove_updater(lambda b, dt: b.shift(RIGHT * v1 * dt))
        ball2.remove_updater(lambda b, dt: b.shift(RIGHT * v2 * dt))
        
        self.play(FadeOut(ball1), FadeOut(ball2), FadeOut(speed1), FadeOut(speed2))
        
        # Acceleration demonstration
        ball3 = Dot().set_color(GREEN).shift(LEFT*4 + DOWN*2)
        ball4 = Dot().set_color(YELLOW).shift(LEFT*4 + DOWN*3)
        accel1 = Text("a1", font_size=24).next_to(ball3, UP)
        accel2 = Text("a2", font_size=24).next_to(ball4, UP)
        
        self.play(FadeIn(ball3), FadeIn(ball4), Write(accel1), Write(accel2))
        
        # Define updater functions for acceleration
        a1 = 1  # units per second^2
        a2 = 5  # units per second^2
        
        velocity1 = [0]  # Use a mutable container to allow updates within the lambda
        velocity2 = [0]

        # Add updaters for ball3 and ball4
        ball3.add_updater(lambda b, dt: (
            velocity1.__setitem__(0, velocity1[0] + a1 * dt),  # Update velocity1
            b.shift(RIGHT * velocity1[0] * dt)                # Update position
        )[1])  # Return the second item to avoid issues in the lambda

        ball4.add_updater(lambda b, dt: (
            velocity2.__setitem__(0, velocity2[0] + a2 * dt),  # Update velocity2
            b.shift(RIGHT * velocity2[0] * dt)                # Update position
        )[1])  # Return the second item to avoid issues in the lambda

        
        self.wait(4)  # wait for 4 seconds to simulate the movement
        
        # ball3.remove_updater(lambda b, dt: b.shift(RIGHT * 0.5 * a1 * dt**2))
        # ball4.remove_updater(lambda b, dt: b.shift(RIGHT * 0.5 * a2 * dt**2))
        
        self.play(FadeOut(ball3), FadeOut(ball4), FadeOut(accel1), FadeOut(accel2))
        self.play(FadeOut(title))