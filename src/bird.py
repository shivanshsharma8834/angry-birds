import pymunk as pmk

class Bird:

    def __init__(self) -> None:
        self.life = 20 
        self.mass = 5 
        self.radius = 12 
        self.inertia = pmk.moment_for_circle(self.mass, 0, self.radius, (0, 0))

        