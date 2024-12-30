from manim import *

class ElasticCollisions(Scene):
    def construct(self):
        circle1 = Circle(radius=0.5, color=BLUE).shift(LEFT * 3)
        circle2 = Circle(radius=0.5, color=RED).shift(RIGHT * 3)
        velocity1, velocity2 = np.array([2, 0, 0]), np.array([-2, 0, 0])
        circles = VGroup(circle1, circle2)
        self.add(circles)
        dt = 1 / self.camera.frame_rate

        def update_scene(mob, dt):
            nonlocal velocity1, velocity2
            circle1.shift(velocity1 * dt)
            circle2.shift(velocity2 * dt)
            if np.linalg.norm(circle1.get_center() - circle2.get_center()) <= 1:
                velocity1, velocity2 = velocity2, velocity1

        circles.add_updater(update_scene)
        self.wait(3)
