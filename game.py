from turtle import Turtle, Screen
import time
from food import Food
from Snake import Snake
from scoreboard import Score
s= Screen()
s.tracer(0)
s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
inp=s.textinput("Choose game Speed","Enter game speed slow medium fast")
snake= Snake()
print(inp)
food= Food()
sb= Score()
if(inp.lower()=="slow"):
    level=0.3
elif(inp.lower()=="medium"):
    level=0.5
elif(inp.lower()=="fast"):
    level=0.08
else:
    print("Enter proper game speed. By default you can play with fast speed ")
    level = 0.08
s.listen()
s.onkey(key="Right",fun=snake.front)
s.onkey(key="Up",fun=snake.up)
s.onkey(key="Left",fun=snake.back)
s.onkey(key="Down",fun=snake.down)
flag=True
while (flag):
    s.update()
    time.sleep(level)
    snake.move()
    if(snake.t_lst[0].distance(food)<20):
        food.refresh()
        snake.grow()
        sb.update()
    if(snake.t_lst[0].xcor()<=-300 or snake.t_lst[0].xcor()>=300 or snake.t_lst[0].ycor()<=-300  or snake.t_lst[0].ycor()>=300  ):
        sb.over()
        flag=False
    for i in range(1,len(snake.t_lst)):
        if(snake.t_lst[0].distance(snake.t_lst[i])<15):
            sb.over()
            flag=False

s.exitonclick()