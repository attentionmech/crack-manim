from manim import *

class SimultaneousAnimations(MovingCameraScene):
    def construct(self):
        # Create objects
        square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT)
        circle = Circle(color=RED, fill_opacity=0.5).shift(RIGHT)

        # Add objects to the scene
        self.add(square, circle)

        # Create animations
        square_animation = square.animate.shift(RIGHT * 2)
        circle_animation = circle.animate.shift(LEFT * 2)

        # Play animations simultaneously
        self.play(square_animation, circle_animation)

        # Wait for a moment
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(square).set(width=square.width * 2))

        # Wait for a moment to observe the camera movement
        self.wait(1)
        
        self.play(self.camera.frame.animate.move_to(circle).set(width=square.width * 2))
        
        self.wait(1)
        
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width))
