from manim import *
import numpy as np

#Credits:
#https://manimclass.com/3d-manim-animations/

class Axes3DPlot(ThreeDScene):
    def construct(self):
        # Set initial camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=0.6)

        # Create 3D axes
        axes = ThreeDAxes(
            x_range=(-4, 4, 1),
            y_range=(-1.5, 1.5, 0.5),
            z_range=(-2, 2, 1),
            x_length=7,
            y_length=4,
            z_length=5,
            tips=True,
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Add a cosine graph
        cos_graph = axes.plot(lambda x: np.cos(x), x_range=(-PI, PI), color=RED, stroke_width=4)

        # Add a parametric function with gradient color
        gradient_curve = ParametricFunction(
            lambda x: np.array([np.sin(x), np.cos(x), x / 2]),
            t_range=(-TAU, TAU),
            color=BLUE,
            stroke_width=5,
        ).set_color_by_gradient(RED, YELLOW, GREEN)

        # Add text annotation
        title = Text("3D Plot Example", font_size=36).to_edge(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Play animations to introduce axes and labels
        self.play(Write(axes), Write(axes_labels))
        self.play(Write(title))

        # Animate cosine graph
        self.play(Create(cos_graph))
        self.wait(0.5)
        

        # Smoothly move camera to emphasize the parametric curve
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, zoom=1.2)
        self.play(Write(gradient_curve))

        # Highlight a specific point on the curve
        point = Dot3D(axes.c2p(np.sin(PI / 2), np.cos(PI / 2), PI / 4), color=YELLOW)
        point_label = Text("Interesting Point", font_size=24, color=YELLOW).next_to(point, RIGHT)
        self.add_fixed_in_frame_mobjects(point_label)

        self.play(FadeIn(point), Write(point_label))
        self.wait(1)

        # Move camera again for a dynamic view
        self.move_camera(phi=30 * DEGREES, theta=-30 * DEGREES, zoom=0.8)
        self.wait(1)

        # Group objects for a dramatic exit
        all_objects = VGroup(axes, cos_graph, gradient_curve, title, point, point_label, axes_labels)
        self.play(Unwrite(all_objects), run_time=2)
        self.wait()
