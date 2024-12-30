from manim import *

class BallRollingDownHill(Scene):
    def construct(self):
        # Define the hill (curve)
        hill = FunctionGraph(lambda x: 0.2 * x**2, x_range=[-3, 3], color=BLUE)
        self.play(Create(hill))
        
        # Add a label to the hill
        hill_label = MathTex("y = 0.2x^2").next_to(hill, UP)
        self.play(Write(hill_label))

        # Define the ball as a dot
        ball = Dot(radius=0.2, color=RED)
        ball.move_to(hill.point_from_proportion(0))  # Start at the left end of the hill
        self.add(ball)
        
        # Define the path of the ball along the hill
        def ball_update(ball, alpha):
            # Get the position along the hill curve
            point = hill.point_from_proportion(alpha)
            ball.move_to(point)

        # Animate the ball rolling down the hill
        self.play(UpdateFromAlphaFunc(ball, ball_update), run_time=5, rate_func=smooth)

        # Conclude the scene
        self.play(FadeOut(ball), FadeOut(hill), FadeOut(hill_label))
