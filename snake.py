from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def move(self):
        for snake_i in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[snake_i - 1].xcor()
            new_y = self.all_snakes[snake_i - 1].ycor()
            self.all_snakes[snake_i].goto(new_x, new_y)
        self.all_snakes[0].forward(20)

        def up(self):
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.setheading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.setheading() != RIGHT:
            self.head.setheading(LEFT)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_snakes.append(snake)

    def extend(self):
        self.add_snake(self.all_snakes[-1].position())
