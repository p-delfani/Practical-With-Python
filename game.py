import turtle

wn = turtle.Screen()
wn.title("Pong by gamemaker")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Score 
score_a =0
score_b =0



#paddleA
paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white") 
paddle_a.penup()
paddle_a.goto(-350,0)



#paddleB
paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)




#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =2
ball.dy= -2


#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0   Player B:0",align="center", font=("courier",24,"normal"))

#Function 

#this function are for paddle a

def paddle_a_up():
    #dot y cor method is from the turtle module 
    y = paddle_a.ycor()
    y +=20 #it means to go up about 20 pixel
    paddle_a.sety()

def paddle_a_down():
    #dot y cor method is from the turtle module 
    y  = paddle_a.ycor()
    y -=20  #it means to go down about 20 pixel
    paddle_a.sety()




#this function are for paddle b
def paddle_b_up():
    #dot y cor method is from the turtle module 
    y = paddle_b.ycor()
    y +=20 #it means to go up about 20 pixel
    paddle_b.sety()

def paddle_b_down():
    #dot y cor method is from the turtle module 
    y  = paddle_b.ycor()
    y -=20  #it means to go down about 20 pixel
    paddle_b.sety()



#keyboard binding 
wn.listen()       # -> this line is for listen the key when user touch and click it 
#there are for paddle a:
wn.onkeypress(paddle_a.up,"w")  # -> in here when user click w in keyboard our program use paddle_a.up function            
wn.onkeypress(paddle_a.down,"s")
#there are for paddle b:
wn.onkeypress(paddle_b.up,"Up")  
wn.onkeypress(paddle_b.down,"Down")



#main game loop
while True:
    wn.update()

    
   #Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
     

   #Border checking 
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy*=-1

    if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy*=-1

    if ball.xcor() >390:
     ball.goto(0,0)
     ball.dx *= -1


    if ball.xcor() <-390:
     ball.goto(0,0)
     ball.dx *= -1

     #Paddle and ball collisions 
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor()+350 and ball.ycor() >paddle_b.ycor()+40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() > -340 and (ball.ycor() < paddle_a.ycor()+350 and ball.ycor() >paddle_b.ycor()+40):
        ball.setx(340)
        ball.dx *= -1