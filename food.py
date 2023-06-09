from turtle import Turtle,Screen
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.goto(randint(-240,240),randint(-240,240))
    def refresh(self):
        self.goto(randint(-240, 240), randint(-240, 240))