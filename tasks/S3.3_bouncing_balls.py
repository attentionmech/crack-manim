from manim import *

class BouncingBalls(Scene):
    def construct(self):
        # Create a closed box
        floor = Line(np.array([-3, -3, 0]), np.array([3, -3, 0]))
        left_wall = Line(np.array([-3, -3, 0]), np.array([-3, 3, 0]))
        right_wall = Line(np.array([3, -3, 0]), np.array([3, 3, 0]))
        ceiling = Line(np.array([-3, 3, 0]), np.array([3, 3, 0]))
        
        self.add(floor, left_wall, right_wall, ceiling)
        
        # Create balls
        balls = VGroup(*[Dot(np.array([0, 0, 0]), color=random_bright_color()) for _ in range(20)])
        for ball in balls:
            ball.velocity = np.random.uniform(-2, 2, size=3)
            ball.velocity[2] = 0  # Ensure motion is in 2D
            self.add(ball)
        
        # Gravity
        gravity = np.array([0, -0.1, 0])
        
        def update_ball(ball, dt):
            ball.velocity += gravity
            ball.shift(ball.velocity * dt)
            
            # Check for collision with walls
            if ball.get_center()[1] <= floor.get_start()[1] or ball.get_center()[1] >= ceiling.get_start()[1]:
                ball.velocity[1] = -ball.velocity[1]
            if ball.get_center()[0] <= left_wall.get_start()[0] or ball.get_center()[0] >= right_wall.get_start()[0]:
                ball.velocity[0] = -ball.velocity[0]
        
        for ball in balls:
            ball.add_updater(update_ball)
        
        self.wait(10)
