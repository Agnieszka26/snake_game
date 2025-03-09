import time
from turtle import Screen
with open("high_score.txt") as high_score:
   current_high_score = high_score.read()

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on=True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def end_game():
    global game_is_on
    game_is_on = False
    scoreboard.end_game()

screen.onkey(end_game, "e")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food.
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    #detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        scoreboard.reset()
        snake.reset()
    #Detect collision with tail
    #if head collides with any segment in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
