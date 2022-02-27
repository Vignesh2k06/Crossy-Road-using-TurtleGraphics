from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list = []
        self.cars()

    def cars(self):
        num = random.randint(0, len(COLORS)-1)
        new_y = random.randint(-200, 200)
        if random.randint(1, 6) == 1:
            self.sree = Turtle()
            self.sree.shape("square")
            self.sree.pu()
            self.sree.shapesize(stretch_wid=1, stretch_len=2)
            self.sree.color(COLORS[num])
            self.sree.goto(300, new_y)
            self.sree.setheading(180)
            self.sree.speed("fastest")
            self.list.append(self.sree)

    def move(self):
        for i in self.list:
            i.fd(STARTING_MOVE_DISTANCE)

