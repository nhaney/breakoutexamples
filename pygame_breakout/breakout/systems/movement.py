import esper

from breakout.components.components import Position, Velocity, Shape


class MovementProcessor(esper.Processor):
    def __init__(self, min_x, max_x, min_y, max_y):
        super().__init__()

        self.min_x = min_x
        self.max_x = max_x

        self.min_y = min_y
        self.max_y = max_y

    def process(self, *args, **kwargs):
        for ent, (pos, shape, vel) in self.world.get_components(Position, Shape, Velocity):
            if not shape.type:
                min_x = 0
                max_x = self.max_x - shape.rect.width

                min_y = 0
                max_y = self.max_y - shape.rect.height
            else:
                min_x = shape.radius
                max_x = self.max_x - shape.radius

                min_y = shape.radius
                max_y = self.max_y - shape.radius

            pos.x += vel.x
            pos.y += vel.y

            pos.x = max(min_x, pos.x)
            pos.x = min(max_x, pos.x)

            pos.y = max(min_y, pos.y)
            pos.y = min(max_y, pos.y)




