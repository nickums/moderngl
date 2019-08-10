import moderngl

import _example
from _print_memory import print_memory


class Example(_example.Example):
    title = 'Color Triangle'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330

                in vec2 in_vert;
                in vec4 in_color;
                out vec4 v_color;

                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330

                in vec4 v_color;
                out vec4 f_color;

                void main() {
                    f_color = v_color;
                }
            ''',
        )

        vertex_data = moderngl.pack([
            0, 16000, 255, 0, 0, 255,
            -12000, -16000, 0, 255, 0, 255,
            12000, -16000, 0, 0, 255, 255,
        ], layout='2i2 4u1')

        print('%2s%5s%5s%3s%3s%3s' % ('x', 'y', 'r', 'g', 'b', 'a'))
        print_memory(vertex_data, 3, [2, 4, 4, 5, 6, 7])

        self.vbo = self.ctx.buffer(vertex_data)
        self.vao = self.ctx.vertex_array(self.prog, [
            self.vbo.bind('in_vert', 'in_color', layout='2ni2 4nu1'),
        ])

    def render(self, time, frame_time):
        self.ctx.screen.clear((1.0, 1.0, 1.0))
        self.vao.render()


if __name__ == '__main__':
    Example.run()
