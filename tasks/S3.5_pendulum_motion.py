from manim import *
import numpy as np

class PendulumMotion(Scene):
    def construct(self):
        # Create the pendulum components
        pivot = Dot(ORIGIN)
        bob = Dot(3 * DOWN)
        rod = Line(pivot.get_center(), bob.get_center())

        # Group the components together
        pendulum = VGroup(rod, bob)

        # Add the pivot and pendulum to the scene
        self.add(pivot, pendulum)
        self.time = 0
        self.length = 3  # Length of the pendulum rod
        self.g = 9.8  # Acceleration due to gravity
        self.angle = 1.5  # Initial angle (in radians)
        self.angular_velocity = 0.5  # Initial angular velocity
        self.damping = 0.05  # Damping factor

        # Define the pendulum motion
        def update_pendulum(mob, dt):
            self.time += dt
            # Update the angular velocity and angle using the equations of motion with damping
            self.angular_velocity += (-self.g / self.length * np.sin(self.angle) - self.damping * self.angular_velocity) * dt
            self.angle += self.angular_velocity * dt * 0.01
            # Calculate the new bob position
            new_bob_position = self.length * np.array([np.sin(self.angle), -np.cos(self.angle), 0])
            new_rod = Line(pivot.get_center(), new_bob_position)
            mob[0].become(new_rod)
            mob[1].move_to(new_bob_position)

        # Add the update function to the pendulum
        pendulum.add_updater(update_pendulum)

        # Animate the pendulum motion
        self.play(UpdateFromAlphaFunc(pendulum, update_pendulum), run_time=5, rate_func=linear)
        self.wait()