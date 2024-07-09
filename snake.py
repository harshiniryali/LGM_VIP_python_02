import turtle
import time
import random
screen=turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
snake_head=turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0,0)
snake_direction="up"
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290,290),
          random.randint(-290,290))
score=0
snake_segments=[]
def move():
    if snake_direction=="up":
        snake_head.sety(snake_head.ycor()+20)
    elif snake_direction=="down":
        snake_head.sety(snake_head.ycor()-20)
    elif snake_direction=="left":
        snake_head.setx(snake_head.xcor()-20)
    elif snake_direction=="right":
        snake_head.setx(snake_head.xcor()+20)
def go_up():
    global snake_direction
    if snake_direction!="down":
        snake_direction="up"

def go_down():
    global snake_direction
    if snake_direction!="up":
        snake_direction="down"

def go_left():
    global snake_direction
    if snake_direction!="right":
        snake_direction="left"

def go_right():
    global snake_direction
    if snake_direction!="left":
        snake_direction="right"

screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

while True:
    move()

    if snake_head.distance(food)<20:
        food.goto(random.randint(-290,290), random.randint(-290,290))
        score+=1
        print(f"Score: {score}")
        new_segment=turtle.Turtle()
        new_segment.shape("square")
        new_segment.color=("green")
        new_segment.penup()
        snake_segments.append(new_segment)

    if(
    abs(snake_head.xcor())>290
    or abs(snake_head.ycor())>290
    or snake_head in snake_segments):
     print("Game over! Your score: ",score)
    break
for i in range(len(snake_segments)-1,0,-1):
    x,y=snake_segments[i-1].pos()
    snake_segments[i].goto(x,y)

if len(snake_segments)>0:
    x,y=snake_head.pos()
    snake_segments[0].goto(x,y)

time.sleep(0.1)
screen.bye()