import turtle as tur
import time
import random



delay = 0.1
score = 0
high_score = 0
speed= 20

wn = tur.Screen()

wn.title("Snake game")
wn.bgcolor("black")
wn.setup(width= 600, height = 600)

wn.tracer(0)
head = tur.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "Stop"
food = tur.Turtle()

food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)

segments = []

pen = tur.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("Score: 0 High Score: 0", align= "center", font = ("Courier", 24, "normal"))





def go_up():
    if head.direction != "down":
       head.direction = "up"


def go_down():
    if head.direction !="up":
       head.direction ="down"


def go_left():
    if head.direction != "right":
       head.direction = "left" 


def go_right():
    if head.direction != "left":
       head.direction = "right"


def move() :
    if head.direction=="up":
      y = head.ycor()
      head.sety(y+speed)

    if head.direction=="down":
      y = head.ycor()
      head.sety(y-speed)
      
    if head.direction=="left":
      x= head.xcor()
      head.setx(x-speed)

    if head.direction=="right":
      x= head.xcor()
      head.setx(x+speed)

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


while True :

    wn.update()
   


    if (head.ycor() > 290 or 
          head.ycor() < -290 or 
          head.xcor() > 290 or 
          head.xcor() < -290):
          time.sleep(1)
          for segment in segments:
            segment.goto(1000,1000)
          score = 0
          pen.clear()
          pen.write("Scrore :{}  High score: {}".format(score,high_score), align= "center", font = ("Courier", 24, "normal"))
          segments.clear()
          head.direction = "Stop"
          head.goto(0,0)
   
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    

    for segment in segments: 
       if head.distance(segment) < 20 :
          time.sleep(1)
          for segment in segments:
            segment.goto(1000,1000)
          segments.clear()
          score = 0
          pen.clear()
          pen.write("Scrore :{}  High score: {}".format(score,high_score), align= "center", font = ("Courier", 24, "normal"))
          head.goto(0,0)
       
           

          
    if head.distance(food) < 20:
     
     x = random.randint(-290, 290)
     y = random.randint(-290, 290)
     score += 10
     food.goto(x, y)
     if score>= high_score:
        high_score = score
     pen.clear()
     pen.write("Scrore :{}  High score: {}".format(score,high_score), align= "center", font = ("Courier", 24, "normal"))
     


     segment = tur.Turtle()
     segment.speed(0)
     segment.shape("square")
     segment.color("grey")
     segments.append(segment)
     segment.penup()
    
     
     delay =delay-  0.001

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    time.sleep(delay)
    move()
     
     
    























