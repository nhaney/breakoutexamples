class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def reset(self):
        self.x, self.y = 0, 0


class Position:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Shape:
    """
    If type is 0, it is a rectangle
    If type is 1, it is a circle
    """
    def __init__(self, type=0, *, rect=None, radius=None):
        # validate component
        if type not in (0, 1):
            raise AttributeError("Invalid type! Choices are 0 (rect) and 1 (circle)")

        if not rect and not radius:
            raise AttributeError(f"Must specify {'rect' if not type else 'radius'} when initializing.")

        if not rect and not type:
            raise AttributeError("Must specify rect!")

        if not radius and type:
            raise AttributeError("Must specify radius!")

        self.type = type
        self.rect = rect
        self.radius = radius


class Renderable:
    def __init__(self, color):
        self.color = color


class Collidable:
    def __init__(self, mask, collision_mask):
        self.mask = mask
        self.collision_mask = collision_mask


class Input:
    def __init__(self, speed=500):
        self.speed = speed


