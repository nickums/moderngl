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
                in vec3 in_color;
                out vec3 v_color;

                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330

                in vec3 v_color;
                out vec4 f_color;

                void main() {
                    f_color = vec4(v_color, 1.0);
                }
            ''',
        )

        vertex_data = moderngl.pack([
            0.0, 0.8, 255, 0, 0,
            -0.6, -0.8, 0, 255, 0,
            0.6, -0.8, 0, 0, 255,
        ], layout='2f 3u1', stride=12)

        print('%4s%9s%7s%3s%3s%10s' % ('x', 'y', 'r', 'g', 'b', 'padding'))
        print_memory(vertex_data, 3, [4, 8, 8, 9, 10, 11, 11])

        self.vbo = self.ctx.buffer(vertex_data)
        self.vao = self.ctx.vertex_array(self.prog, [
            self.vbo.bind('in_vert', 'in_color', layout='2f 3nu1', stride=12),
        ])

    def render(self, time, frame_time):
        self.ctx.screen.clear((1.0, 1.0, 1.0))
        self.vao.render()


if __name__ == '__main__':
    Example.run()
