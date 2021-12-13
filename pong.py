# things to improve
# 1- set different tone for bounce on paddle

# simple pong game
import  turtle
import os # to enable us to use os functions
wn = turtle.Screen()
wn.title("pong by kiarie")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_A = 0
score_B = 0

# paddle a
paddle_1 = turtle.Turtle()
paddle_1.speed(0) # set speed of the paddle to the maximum
paddle_1.shape("square")
paddle_1.color("white") # setting color of the paddle
paddle_1.shapesize(stretch_wid=5, stretch_len=1) # change the default size of the paddle to a usable size
paddle_1.penup() # to avoid leaving trace when moving
paddle_1.goto(-350, 0) # move the starting point of the paddle to the far center right


# paddle b

paddle_2 = turtle.Turtle()
paddle_2.speed(0) # set speed of the paddle to the maximum
paddle_2.shape("square")
paddle_2.color("white") # setting color of the paddle
paddle_2.shapesize(stretch_wid=5, stretch_len=1) # change the default size of the paddle to a usable size
paddle_2.penup() # to avoid leaving trace when moving
paddle_2.goto(350, 0) # move the starting point of the paddle to the far center right


#ball

ball = turtle.Turtle()
ball.speed(0)  # set speed of the paddle to the maximum
ball.shape("square")
ball.color("white")  # setting color of the paddle

ball.penup()  # to avoid leaving trace when moving
ball.goto(0, 0)  # move the starting point of the paddle to the far center right
ball.dx = 2
ball.dy = -2  # move ball along y coordinate

# pen to keep score
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle() # to hide the pen
pen.goto(0, 260)
pen.write("playerA: 0  playerB: 0", align="center", font=("Courier", 25, "normal"))
# main game loop

# functions to move the paddle
# paddle1


def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


# paddle 2

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# keyboard binding


wn.listen() # this tells the app to listen for key press
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
# wn.onkeypress(breakit, "q")
# paddle 2

wn.onkeypress(paddle_2_up, "Up") # to set up arrow key
wn.onkeypress(paddle_2_down, "Down") # to set down arrow key



while True:

    wn.update()


    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # what happens when the ball hits the border
    # top and bottom
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        os.system("afplay bounce.wav&") # added & sign to remove the lag effect when sound is played

    if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            os.system("afplay bounce.wav&")
    # sides
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # registering bounce

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("playerA: {}  playerB: {}".format(score_A, score_B), align="center", font=("Courier", 25, "normal"))
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("playerA: {}  playerB: {}".format(score_A, score_B), align="center", font=("Courier", 25, "normal"))
        os.system("afplay bounce.wav&")





