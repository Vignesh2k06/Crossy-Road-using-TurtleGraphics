from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.pu()
        self.speed("fastest")
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def move_front(self):
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.backward(MOVE_DISTANCE)

    def next_level(self):
        self.setpos(STARTING_POSITION)

