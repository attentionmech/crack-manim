from manim import *
from manim import config

class CameraMovements(MovingCameraScene):
    def construct(self):
        # Create a square and a circle
        square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT)
        circle = Circle(color=RED, fill_opacity=0.5).shift(RIGHT)
        
        # Add the shapes to the scene
        self.add(square, circle)
        
        # Wait for a moment
        self.wait(1)
        
        # Move the camera to focus on the square
        self.play(self.camera.frame.animate.move_to(square).set(width=square.width * 2))
        
        # Wait for a moment
        self.wait(1)
        
        # Move the camera to focus on the circle
        self.play(self.camera.frame.animate.move_to(circle).set(width=circle.width * 2))
        
        # Wait for a moment
        self.wait(1)
        
        # Reset the camera to the original position
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width))
        
        # Wait for a moment
        self.wait(1)