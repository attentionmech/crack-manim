from manim import *
from manim import config

class FreeFallAnimation(MovingCameraScene):
    def construct(self):
        # Create a circle to represent the falling object
        ball = Circle(radius=0.2, color=BLUE).shift(UP * 3)
        
        # Create the ground
        ground = Line(start=LEFT * 4, end=RIGHT * 4).shift(DOWN * 3)
        
        # Add the ball and ground to the scene
        self.add(ball, ground)
        
        # Define the acceleration due to gravity
        g = 9.8
        # Initial velocity
        v = 0
        # Time step
        dt = 0.1
        # Coefficient of restitution (bounciness)
        e = 0.8

        # Updater function to simulate free fall and bouncing
        def update_ball(mob, dt):
            nonlocal v
            v += g * dt
            mob.shift(DOWN * v * dt)
            if mob.get_bottom()[1] <= ground.get_top()[1]:
                v = -v * e
                mob.shift(UP * (ground.get_top()[1] - mob.get_bottom()[1]))


        self.camera.frame.set(width= 30*ball.get_width())
        # Add the updater to the ball
        ball.add_updater(update_ball)

        # Run the animation for 10 seconds
        self.wait(10)

        # Remove the updater after the animation
        ball.remove_updater(update_ball)
