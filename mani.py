from turtle import Turtle, Screen

screen = Screen()

snake = Turtle(shape="square")

snake.color("white")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake.turtlesize(1, 3)


screen.exitonclick()
