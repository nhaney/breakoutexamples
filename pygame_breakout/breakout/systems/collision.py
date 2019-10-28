import esper
import pygame

from ..components.components import Collidable, Position, Velocity


class CollisionProcessor(esper.Processor):
    """
    Applies all collisions that happen during a frame. Happens after movement.
    """
    def __init__(self):
        pass

    def process(self):
        for ent, (pos, vel, col) in self.world.get_components(Position, Velocity, Collidable):
            pass

