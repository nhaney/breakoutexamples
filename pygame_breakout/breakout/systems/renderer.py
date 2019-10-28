import esper
import pygame

from breakout.components.components import Position, Renderable, Shape


class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self, *args, **kwargs):
        # clear window
        self.window.fill(self.clear_color)
        for ent, (pos, render, shape) in self.world.get_components(Position, Renderable, Shape):
            if shape.type == 0:
                self.render_rect(pos, render, shape)
            elif shape.type == 1:
                self.render_circle(pos, render, shape)
        # flip the framebuffers
        pygame.display.flip()

    def render_circle(self, pos, render, shape):
        pygame.draw.circle(self.window, render.color, (pos.x, pos.y), shape.radius)

    def render_rect(self, pos, render, shape):
        pygame.draw.rect(self.window, render.color, (pos.x, pos.y, shape.rect.width, shape.rect.height))



