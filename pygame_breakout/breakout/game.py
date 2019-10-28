import os

import pygame
import esper

from breakout.components import *
from breakout.systems import *

FPS = 60
RESOLUTION = 720, 480


def run():
    # Initialize Pygame stuff
    pygame.init()
    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Breakout")
    clock = pygame.time.Clock()

    # Initialize Esper world, and create a "player" Entity with a few Components.
    world = esper.World()
    player = world.create_entity(
        Velocity(),
        Position(360.0, 450),
        Shape(0, rect=pygame.Rect((360, 450), (100, 20))),
        Renderable(pygame.Color(255, 0, 0)),
        Input()
    )
    world.add_processor(InputProcessor(player))
    world.add_processor(MovementProcessor(0, 720, 0, 450))
    world.add_processor(RenderProcessor(window))

    running = True
    p_t = pygame.time.get_ticks()

    while running:
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - p_t) / 1000.0
        p_t = t

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # A single call to world.process() will update all Processors:
        world.process(delta=delta)


run()
pygame.quit()
