from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.collision=0;
        self.hideturtle()
        self.color("white")
        self.goto(-20,250)
        self.update()
    def update(self):
        self.clear()
        self.write("Score: "+str(self.collision),False,align="center",font=('Arial', 15, 'normal'))
        self.collision=self.collision+1
    def over(self):
        self.clear()
        self.write("GAME OVER !! Final score:"+str(self.collision-1), False, align="center", font=('Arial', 15, 'normal'))