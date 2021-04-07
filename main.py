from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# snake.turtlesize(1, 3)

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_game()

    # Detect collision with tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_game()
screen.exitonclick()
