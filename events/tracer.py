from .events import Event


class Tracer(Event):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
    
    def used_blink(self):
        pass