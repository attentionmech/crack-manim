from manim import *

class NewtonianGravity(Scene):
    def construct(self):
        # Constants
        G = 3  # Gravitational constant (scaled for simulation)
        dt = 0.05  # Time step for simulation
        
        # Masses and positions of the two bodies
        m1, m2 = 5, 1
        pos1, pos2 = np.array([-1, 0.0, 0]), np.array([1, 0.0, 0])
        vel1, vel2 = np.array([0, 0.5, 0]), np.array([0, -1.5, 0])
        
        # Create Mobjects for visualization
        body1 = Dot(pos1, color=BLUE).scale(m1 * 0.1)
        body2 = Dot(pos2, color=RED).scale(m2 * 0.1)
        
        # Add trails for orbits
        trail1 = TracedPath(body1.get_center, stroke_color=BLUE)
        trail2 = TracedPath(body2.get_center, stroke_color=RED)
        
        self.add(body1, body2, trail1, trail2)
        
        # Simulate gravitational motion
        for _ in range(200):  # Run for 200 time steps
            # Calculate the distance and direction vector between the bodies
            r = pos2 - pos1
            distance = np.linalg.norm(r)
            direction = r / distance
            
            # Compute gravitational force
            force = G * m1 * m2 / distance**2
            force_vec = force * direction
            
            # Update velocities
            vel1 += force_vec / m1 * dt
            vel2 -= force_vec / m2 * dt
            
            # Update positions
            pos1 += vel1 * dt
            pos2 += vel2 * dt
            
            # Update Mobject positions
            body1.move_to(pos1)
            body2.move_to(pos2)
            
            # Pause for animation
            self.wait(0.01)
