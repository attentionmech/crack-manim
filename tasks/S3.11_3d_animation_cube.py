from manim import *

# Credits:
# https://manimclass.com/3d-manim-animations/

class CubeAnimation(ThreeDScene):
    def construct(self):
        # Set initial camera orientation
        self.set_camera_orientation(phi=60 * DEGREES, theta=-60 * DEGREES)
        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.4, stroke_color=BLUE, stroke_width=2)
        
        # Draw the cube with a scaling effect
        self.play(cube.animate.scale(1.5).set_color(YELLOW), run_time=2)
        self.wait()
        
        # Move the camera to a bird's-eye view
        self.move_camera(phi=45 * DEGREES, theta=90 * DEGREES, run_time=2)
        self.wait()
        
        # Begin ambient camera rotation and pulse the cube color
        self.begin_ambient_camera_rotation(rate=90 * DEGREES, about="theta")
        self.begin_ambient_camera_rotation(rate=30 * DEGREES, about="phi")
        self.play(cube.animate.set_fill(opacity=0.6).set_color(GREEN), run_time=3)
        self.wait()
        
        # Stop the ambient camera rotation
        self.stop_ambient_camera_rotation(about="theta")
        self.stop_ambient_camera_rotation(about="phi")
        self.wait()
        
        # Add axes and zoom in while rotating the cube
        self.play(Write(axes))
        self.move_camera(zoom=1.2, theta=-30 * DEGREES, run_time=3)
        self.play(Rotate(cube, 180 * DEGREES, axis=UP), run_time=2)
        self.wait()
        
        # Shrink the cube and shift it dynamically
        self.play(cube.animate.scale(0.5).shift(LEFT + OUT), run_time=2)
        self.play(cube.animate.move_to(axes.c2p(2, 2, 2)), run_time=2)
        self.wait()
        
        # Rotate the cube around a custom axis
        self.play(Rotate(cube, 360 * DEGREES, axis=RIGHT + OUT), run_time=3)
        self.wait()
        
        # Move the camera to an angled view and reset cube position
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.9, run_time=3)
        self.play(cube.animate.move_to(axes.c2p(0, 0, 0)).scale(2).set_color(RED), run_time=3)
        self.wait()
