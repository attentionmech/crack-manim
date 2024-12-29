from manim import *

class SpiralInception(MovingCameraScene):
    
    def construct(self):
        spiral = VGroup()
        colors = [RED, GREEN, BLUE]
        num_turns = 20
        num_points = 1000
        radius = 0.000001
        z_increment = 0.00  # Increment in the z-direction

        for i in range(num_points):
            angle = i * TAU / num_points * num_turns
            x = radius * i * np.cos(angle)
            y = radius * i * np.sin(angle)
            z = z_increment * i  # Increment in the z-direction
            if i > 0:
                prev_angle = (i - 1) * TAU / num_points * num_turns
                prev_x = radius * (i - 1) * np.cos(prev_angle)
                prev_y = radius * (i - 1) * np.sin(prev_angle)
                prev_z = z_increment * (i - 1)  # Previous z-coordinate
                line = Line(start=[prev_x, prev_y, prev_z], end=[x, y, z], color=colors[i % len(colors)], stroke_width=2)
                spiral.add(line)
                

        def update_spiral(mob, alpha):
            mob.rotate(TAU * alpha, axis=OUT)
            for i, line in enumerate(mob):
                line.set_color(colors[(i + int(alpha * num_points)) % len(colors)])

        
        # move camera to a 3d corner and point at spiral
        self.camera.frame.set(width=2* spiral.get_width())
        
        self.play(
            UpdateFromAlphaFunc(spiral, update_spiral),
            Create(spiral, run_time=5, rate_func=linear),
        )
        self.wait()