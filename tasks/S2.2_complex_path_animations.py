from manim import *

class ComplexPathAnimations(Scene):
    def construct(self):
        # Create objects
        dot = Dot().set_color(RED)
        square = Square().set_color(BLUE)
        
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        curve_path = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)

        line_path = Line(LEFT, RIGHT)
        
        
        # Create animations
        line_animation = MoveAlongPath(dot, line_path, run_time=2)
        curve_animation = MoveAlongPath(square, curve_path, run_time=4)
        
        # Add paths to the scene
        self.add(line_path, curve_path)
        
        # Play animations
        self.play(line_animation)
        self.play(curve_animation)
        
        # Keep the final frame
        self.wait()