from turtle import Turtle, Screen
import time
import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

screen.listen()


player = Player()
screen.onkey(player.up, "Up")

game_is_on = True

car_manager = CarManager.CarManager()
scoreboard = Scoreboard()



while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.update()




























screen.exitonclick()
