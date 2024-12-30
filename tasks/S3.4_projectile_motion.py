from manim import *
import numpy as np

class ProjectileMotion(Scene):
    def construct(self):
        # Constants
        G = 9.8  # Acceleration due to gravity (m/s^2)
        INITIAL_VELOCITY = 5  # m/s
        LAUNCH_ANGLE = 45 * DEGREES  # degrees
        SIMULATION_TIME = 2  # seconds

        # Calculate Initial Velocity Components
        vx = INITIAL_VELOCITY * np.cos(LAUNCH_ANGLE)
        vy = INITIAL_VELOCITY * np.sin(LAUNCH_ANGLE)

        # Projectile
        projectile = Dot(radius=0.1, color=BLUE)
        
        self.add(projectile)

        # Ground
        ground = Line(start=[-5, -3, 0], end=[5, -3, 0], color=GREEN)
        self.add(ground)

        # Trajectory Trace
        trajectory_trace = VMobject(color=YELLOW, stroke_width=2)
        trajectory_trace.start_new_path(projectile.get_center()) #Initialize trace starting at projectile's position
        self.add(trajectory_trace)

        # Time variable for the updater
        time = 0

        # Updater function for projectile motion
        def projectile_updater(mobject, dt):
            nonlocal time  # Access and modify the time variable in outer scope
            time += dt
            if time > SIMULATION_TIME:
                mobject.clear_updaters() #remove updater to stop simulation
                return
            x = vx * time
            y = vy * time - 0.5 * G * time**2
            mobject.move_to([x, y, 0])
            trajectory_trace.append_points([mobject.get_center()])

        # Add the updater to the projectile
        projectile.add_updater(projectile_updater)
        self.wait(SIMULATION_TIME + 1) #Wait a bit longer so we can see the end result