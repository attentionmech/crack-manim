from manim import *
import random 

class FluidDynamicsSimulation(Scene):
    def construct(self):
        # Constants
        NUM_PARTICLES = 100
        RADIUS = 0.05
        DT = 0.5
        SPACE_BOUNDS = 6  # Space boundary for simulation

        # Initialize particles with random positions and velocities
        particles = VGroup(*[
            Dot(
                radius=RADIUS, 
                color=interpolate_color(BLUE, YELLOW, random.random())
            ).move_to([
                random.uniform(-SPACE_BOUNDS, SPACE_BOUNDS),
                random.uniform(-SPACE_BOUNDS, SPACE_BOUNDS),
                0
            ])
            for _ in range(NUM_PARTICLES)
        ])

        velocities = [
            np.array([
                random.uniform(-1, 1), 
                random.uniform(-1, 1), 
                0
            ]) for _ in range(NUM_PARTICLES)
        ]

        # Add particles to the scene
        self.add(particles)

        # Function to calculate particle interactions (simple repulsion model)
        def update_particles(mob, dt):
            nonlocal velocities
            for i, particle in enumerate(mob):
                position = particle.get_center()
                
                # Update position based on velocity
                velocities[i] += self.calculate_forces(mob, position, i) * dt
                position += velocities[i] * DT

                # Boundary conditions
                for dim in range(2):  # Only x and y
                    if abs(position[dim]) > SPACE_BOUNDS:
                        velocities[i][dim] *= -1.0
                        position[dim] = np.clip(position[dim], -SPACE_BOUNDS, SPACE_BOUNDS)

                # Update particle position
                particle.move_to(position)

        # Add updater to the particle group
        particles.add_updater(update_particles)

        # Run simulation for some time
        self.wait(10)

    def calculate_forces(self, particles, position, index):
        """Calculate forces between particles (simple repulsion model)."""
        force = np.array([0.0, -5, 0.0])
        for j, other_particle in enumerate(particles):
            if j == index:
                continue
            other_position = other_particle.get_center()
            distance = np.linalg.norm(position - other_position)
            if distance < 0.1:  # Repulsion only at short distances
                direction = (position - other_position) / distance
                force += direction * (0.1 - distance)  # Repulsion force
        return force
