from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.all_snakes.append(snake)

    def move(self):
         for snake_i in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[snake_i - 1].xcor()
            new_y = self.all_snakes[snake_i - 1].ycor()
            self.all_snakes[snake_i].goto(new_x, new_y)
        self.all_snakes[0].forward(20)
