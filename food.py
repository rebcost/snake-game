from turtle import Turtle
from random import randint

W_SIZE = 0.5
H_SIZE = 0.5
FOOD_SHAPE = "circle"
FOOD_COLOR = "red"
SPEED = "fastest"

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(W_SIZE, H_SIZE)
        self.color(FOOD_COLOR)
        self.speed(SPEED)
        self.refresh()
        
    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)        
        self.goto(x=random_x, y=random_y)