from manim import *

class AdvancedCameraWork(MovingCameraScene):
    def construct(self):
        # Create a square and a circle
        square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT)
        circle = Circle(color=RED, fill_opacity=0.5).shift(RIGHT)
        
        # Add the shapes to the scene
        self.add(square, circle)
        
        # Apply a camera zoom
        self.play(self.camera.frame.animate.scale(0.5).move_to(square))
        self.wait(1)
        
        # Rotate the camera around the square
        self.play(Rotate(self.camera.frame, angle=PI/4, about_point=square.get_center()))
        self.wait(1)
        
        # Move the camera to the circle
        self.play(self.camera.frame.animate.move_to(circle))
        self.wait(1)
        
        # Follow a path
        path = ArcBetweenPoints(start=square.get_center(), end=circle.get_center(), angle=PI/2)
        self.play(MoveAlongPath(self.camera.frame, path))
        self.wait(1)
        
        # Reset the camera
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(1)