import pymunk as pmk
import pygame as pg

class Bird:

    def __init__(self, game) -> None:
        self.mass = 5 
        # self.radius = 12 
        # self.inertia = pmk.moment_for_circle(self.mass, 0, self.radius, (0, 0))
        self.game = game
        self.body = pmk.Body()
        self.body.position = [500, 0]
        self.poly = pmk.Poly.create_box(self.body)
        self.poly.mass = self.mass
        self.game.space.add(self.body, self.poly)
        self.image = pg.image.load("../assets/images/red-bird.png")
    
    def update(self):
        
        self.game.screen.blit(self.image, self.body.position)
        # self.check_bounds()

    def check_bounds(self):
        # pass

        if self.body.position[1] >= 600:

            self.body.position = pmk.Vec2d(self.body.position[0], 600)
