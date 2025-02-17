import random


def random_color_decorator(draw_func):
    """Decorator to set random colors for a turtle drawing function."""
    def wrapper(t, *args, **kwargs):
        t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return draw_func(t, *args, **kwargs)
    return wrapper
