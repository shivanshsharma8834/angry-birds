import os
import sys
import math
import time
import pymunk as pmk
import pygame as pg 
from bird import Bird


class Game:


    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        
        self.space = pmk.Space()
        self.space.gravity = 0, 0.981 


    def load_assets(self):

        # self.redBird = pg.image.load("../assets/images/red-bird.png")
        self.backGround = pg.image.load("../assets/images/background.png")


    def run(self):

        self.load_assets()

        # body = pmk.Body()

        # body.position = 500, 0
        # poly = pmk.Poly.create_box(body)
        # poly.mass = 10 
        # self.space.add(body, poly)

        bird = Bird(self)

        floor = pmk.Body(body_type=pmk.Body.STATIC)
        floor.position = [0, 600]
        floorShape = pmk.Poly.create_box(floor, (1280,10))
        self.space.add(floor,floorShape)


        running = True

        while running:

            for event in pg.event.get():

                if event.type == pg.QUIT:

                    running = False 

            self.screen.fill("black")
            self.screen.blit(self.backGround, (0,0))


            bird.update()

            self.space.step(0.50)

            
            pg.display.flip()

            self.clock.tick(60)

            pg.display.set_caption("fps: " + str(self.clock.get_fps()))


        pg.quit()



game = Game()

game.run()







