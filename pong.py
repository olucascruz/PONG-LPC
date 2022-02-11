import turtle
import winsound
import random

# draw window
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.40
ball.dy = 0.40

# scores
score_1 = 0
score_2 = 0
score_win = 10

# score head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 250)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


# move paddle 1
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)


# move paddle 2
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)


# mapping keys
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with top wall
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        winsound.PlaySound("assets/bounce.wav",  winsound.SND_ASYNC)

    # collision with down wall
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("assets/bounce.wav",  winsound.SND_ASYNC)

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("assets/258020__kodack__arcade-bleep-sound.wav",  winsound.SND_ASYNC)
        ball.goto(0, random.randint(-200,200))
        ball.dx = 0.40

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("assets/258020__kodack__arcade-bleep-sound.wav",  winsound.SND_ASYNC)
        ball.goto(0, random.randint(-200,200))
        ball.dx = -0.40 

    # collision with paddle 1
    if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx = 0.90
        winsound.PlaySound("assets/bounce.wav",  winsound.SND_ASYNC)

    # collision with paddle 2
    if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx = -0.90
        winsound.PlaySound("assets/bounce.wav",  winsound.SND_ASYNC)
        
    # win condition
    if score_1 == score_win or score_2 == score_win:
        score_1 = score_2 = 0
