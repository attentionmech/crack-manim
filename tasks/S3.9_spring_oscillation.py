from manim import *
from manim import config

class SpringOscillation(Scene):
    def construct(self):
        # Create the spring
        spring = Line(ORIGIN, UP * 2, color=BLUE)

        # Create the mass
        mass = Square(side_length=0.5, color=RED, fill_opacity=1)
        mass.next_to(spring, UP, buff=0)
        self.time = 0

        # Function to update the spring length and mass position
        def update_spring_and_mass(mob, dt):
            self.time += dt
            new_y = 2 + 1.5 * np.sin(self.time * 4)  # Increased amplitude and frequency
            spring.put_start_and_end_on(ORIGIN, UP * new_y)
            mass.move_to(spring.get_end() + UP * (mass.get_height() / 2))

        # Add the updater to the spring and mass
        spring.add_updater(update_spring_and_mass)

        # Add the spring and mass to the scene
        self.add(spring, mass)

        # Animate the spring oscillation
        self.play(ApplyMethod(mass.shift, DOWN * 2, rate_func=there_and_back, run_time=2))
        self.wait(2)

        # Remove the updater after the animation
        spring.remove_updater(update_spring_and_mass)
