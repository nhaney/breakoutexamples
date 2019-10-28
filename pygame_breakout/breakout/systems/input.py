import esper
import pygame

from breakout.components.components import Input, Velocity


class InputProcessor(esper.Processor):
    def __init__(self, player):
        super().__init__()

        self.player = player

    def process(self, *args, **kwargs):
        # find player component
        for ent, (input, vel) in self.world.get_components(Input, Velocity):
            delta = kwargs.get('delta')
            pygame.event.poll()
            keys = pygame.key.get_pressed()

            vel.reset()
            # only need to move left or right in breakout
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                vel.x -= input.speed * delta

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                vel.x += input.speed * delta
