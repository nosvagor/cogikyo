from manim import *
from vagari import c

class test(Scene):
    def construct(self):
       # Create a RoundedRectangle object
        padding_ratio = 0.05

        # Calculate the dimensions based on the screen size and padding
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height
        rect_width = frame_width * (1 - padding_ratio)
        rect_height = frame_height * (1 - 1.5 * padding_ratio)

        rounded_rect = RoundedRectangle(corner_radius=0.5, width=rect_width, height=rect_height)
        rounded_rect.set_fill(c["bg"], opacity=1)
        rounded_rect.set_stroke(c["rby_1"], width=2)

        # Create a Text object and position it at the center of the screen
        text = Text("Abstract", font="Roboto" )
        text.set_fill(c["rby_1"])
        self.add(text)

        self.wait()

        # Animate the transformation of the rectangle into the text object
        self.play(Transform(text, rounded_rect), run_time=1)

        self.add(rounded_rect)

        self.wait()
