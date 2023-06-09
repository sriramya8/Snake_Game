from turtle import Screen,Turtle
import time
from food import Food
s= Screen()
s.tracer(0)
s.setup(600,600)
s.bgcolor("black")

class Snake:
    t_lst = []
    flag = True

    def __init__(self):

        for i in range(0, 3):
            t = Turtle("square")

            t.color("white")
            t.penup()
            t.goto(-i * 20, 0)
            self.t_lst.append(t)
    def move(self):

            for i in range(len(self.t_lst) - 1, 0, -1):
                x_coor = self.t_lst[i - 1].xcor()
                y_coor = self.t_lst[i - 1].ycor()
                self.t_lst[i].goto(x_coor, y_coor)

            self.t_lst[0].forward(20)




    def up(self):

        if(self.t_lst[0].heading()!=270):
            self.t_lst[0].setheading(90)
            self.move()

    def back(self):
        if (self.t_lst[0].heading() != 0):
            self.t_lst[0].setheading(180)
            self.move()

    def front(self):
        if (self.t_lst[0].heading() != 180):
            self.t_lst[0].setheading(0)
            self.move()

    def down(self):
        if (self.t_lst[0].heading() != 90):
            self.t_lst[0].setheading(270)
            self.move()
    def grow(self):
        newt= Turtle("square")
        newt.color("white")
        newt.penup()
        self.t_lst.append(newt)
        self.move()
