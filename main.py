import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_front, "Up")
screen.onkey(player.move_back, "Down")

car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # finish line
    if player.ycor() > 280:
        player.next_level()
        score.level += 1
        score.score()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

    for i in car.list:
        if player.distance(i) < 30:
            score.game_over()
            game_is_on = False
    # cars
    car.cars()
    car.move()

screen.exitonclick()
