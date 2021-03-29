from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
all_snakes = []
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

for position in starting_position:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    all_snakes.append(snake)


#snake.turtlesize(1, 3)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for snake_i in range(len(all_snakes)-1, 0, -1):
        new_x = all_snakes[snake_i - 1].xcor()
        new_y = all_snakes[snake_i - 1].ycor()
        all_snakes[snake_i].goto(new_x, new_y)
    all_snakes[0].forward(20)
screen.exitonclick()
