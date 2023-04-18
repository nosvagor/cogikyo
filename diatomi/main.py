from manim import *
from vagari import c


class intro(Scene):
    def construct(self):
        Text.set_default(font="Archivo")
        frame_width = self.camera.frame_width  # type: ignore
        frame_height = self.camera.frame_height  # type: ignore

        padding_ratio = 0.05
        rect_width = frame_width * (1 - padding_ratio)  # type: ignore
        rect_height = frame_height * (1 - 1.5 * padding_ratio)  # type: ignore
        section_card = RoundedRectangle(
            corner_radius=0.5, width=rect_width, height=rect_height
        )
        section_card.set_fill(c["bg"], opacity=1)
        section_card.set_stroke(c["rby_1"], width=2)

        header = Text("Inroduction", font="Archivo")
        header.scale(1.5)
        header.set_colors_by_radial_gradient([2, 1, 0], 5, c["rby_1"], c["orn_3"])

        self.play(Write(header), run_time=1)
        # self.wait()
        self.play(header.animate.scale(0.25).to_edge(RIGHT + UP, buff=0.75))
        header.set_z_index(1)
        self.play(Create(section_card), run_time=0.5)

        self.wait()

        question = Text("What is the purpose of", font="Archivo")
        question.set_colors_by_radial_gradient([5, -1, 0], 5, c["blu_3"], c["fg"])
        emphasis = Text("coneversation?", font="Archivo")
        emphasis.set_colors_by_radial_gradient([0, -2, 0], 4, c["orn_1"], c["orn_4"])
        combined_text = VGroup(question, emphasis).arrange(RIGHT, buff=0.2)  # type: ignore
        emphasis.shift(0.06 * UP)

        self.play(
            Write(combined_text), run_time=1.8, rate_func=rate_functions.ease_out_sine
        )
        self.play(
            emphasis.animate.scale(1.4).shift(LEFT * 0.16),
            question.animate.scale(0.83).shift(LEFT * 0.5 + DOWN * 0.08),
        )
        self.play(FadeOut(question), run_time=0.5)
        self.play(
            emphasis.animate.scale(1.5).move_to(ORIGIN),
            run_time=1,
            rate_func=rate_functions.ease_in_out_cubic,
        )

        self.wait(5)
