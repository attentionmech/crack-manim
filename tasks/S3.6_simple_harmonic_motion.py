from manim import *

class SimpleHarmonicMotion(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )

        # Create labels
        labels = axes.get_axis_labels(x_label="t", y_label="x(t)")

        # Create the graph of the harmonic motion
        graph = axes.plot(lambda t: np.sin(t), color=YELLOW)

        # Create a dot to represent the moving object
        dot = Dot().move_to(axes.c2p(0, 0))
        dot2 = Dot().move_to(axes.c2p(0, 0))
        dot2.scale(3)

        # Create a vertical line to show the phase
        vertical_line = always_redraw(lambda: axes.get_vertical_line(
            dot.get_center(), color=WHITE, line_func=Line
        ))

        # Create a horizontal line to show the phase
        horizontal_line = always_redraw(lambda: axes.get_horizontal_line(
            dot.get_center(), color=WHITE, line_func=Line
        ))

        # Create a time updater for the dot
        self.time = 0

        def update_dot(d, dt):
            d.move_to(axes.c2p(self.time, np.sin(self.time)))
            self.time += dt


        def update_dot2(d, dt):
            #set only y value to sin
            d.move_to(axes.c2p(0, np.sin(self.time)))
            #set x cooridnator to 0
            
            self.time += dt


        dot.add_updater(update_dot)
        dot2.add_updater(update_dot2)

        # Add all elements to the scene
        self.add(axes, labels, graph, dot, dot2, vertical_line, horizontal_line)
        self.wait(10)