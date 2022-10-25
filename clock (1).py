import time   #it imports a time from the computer
import turtle
'''this is aprogram designed to show analog clock which reads time from the computer and it is desined by
     Biruk Anley which is designed by python
      '''
     #define a background color
display = turtle.Screen()
display.bgcolor("Moccasin")
display.setup(width=750, height=750)
display.title("simple analog clock by biruk anley")
analog = turtle.Turtle()
turtle.hideturtle()
analog.hideturtle()
       #draw a hanger of the clock:

def clock_hanger():
    analog.pensize(3)
    analog.up()
    analog.goto(-270, 190)
    analog.color("blue")
    analog.pendown()
    analog.right(90)
    analog.forward(470)
    analog.begin_fill()
    analog.right(90)
    analog.forward(40)
    analog.right(90)
    analog.forward(630)
    analog.right(90)
    analog.forward(40)
    analog.end_fill()
    analog.goto(-310,-280)
    analog.begin_fill()
    analog.color("black")
    analog.left(210)
    analog.forward(40)
    analog.left(150)
    analog.forward(110)
    analog.left(150)
    analog.forward(40)
    analog.end_fill()
    analog.penup()
    analog.goto(-270,250)
    analog.pendown()
    analog.begin_fill()
    analog.color("red")
    analog.right(150)
    analog.forward(530)
    analog.right(90)
    analog.forward(30)
    analog.right(90)
    analog.forward(530)
    analog.end_fill()

    analog.penup()
    analog.goto(-120,220)
    analog.color("black")
    analog.write("   CLOCK Made by BIRUK ANLEY" , font=("Calibri" ,18,"bold"))
    analog.penup()
    analog.goto(-10,220)
    analog.pendown()

    analog.color("black")
    analog.right(228)
    analog.forward(180)
    analog.goto(-10,220)
    analog.left(282)
    analog.begin_fill()
    analog.forward(160)
    analog.end_fill()

clock_hanger()
        # usen tracer to turn of animation
display.tracer(0)
analog = turtle.Turtle()
analog.speed(0)
analog.pensize(3)

      # drawing a clock face
def draw_clock(h, m, s, analog):
    analog.up()
    analog.goto(0, 140)
    analog.setheading(180)
    analog.color("green")
    analog.pendown()
    analog.circle(140)
         # draw the lines for  hours
    analog.penup()
    analog.goto(0, 0)
    analog.setheading(90)


    for _ in range(12):
        analog.forward(110)
        analog.pendown()
        analog.fd(30)
        analog.penup()
        analog.goto(0, 0)
        analog.rt(30)

    analog.penup()
    analog.goto(0, 0)
    analog.setheading(90)

    for _ in range(60):
        analog.color("black")
        analog.forward(130)
        analog.pendown()
        analog.fd(10)
        analog.penup()
        analog.goto(0, 0)
        analog.rt(6)

        # draw the hour hand   what we do is we need to send...the turtle pen to center of screeen
    analog.penup()
    analog.goto(0, 0)
    analog.color("red")
    analog.setheading(90)
    angle = (h / 12) * 360
    analog.rt(angle)
    analog.pendown()
    analog.fd(40)
    # drawn the minute hand
    analog.penup()
    analog.goto(0, 0)
    analog.color("blue")
    analog.setheading(90)
    angle = (m / 60) * 360
    analog.rt(angle)
    analog.pendown()
    analog.forward(70)
        # draw the second hand
    analog.penup()
    analog.goto(0, 0)
    analog.color("Darkorange")
    analog.setheading(90)
    angle = (s / 60) * 360
    analog.rt(angle)
    analog.pendown()
    analog.forward(110)


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, analog)
    # updating  drawing int memory ,,,,

    clock = 0
    for i in range(12):
        clock = clock + 1
        analog.penup()
        analog.goto(-80,-75 )
        analog.setheading(-30 * i + 60)
        analog.penup()
        analog.goto(0, -10)
        analog.forward(100)
        analog.write(str(clock), align="center", font="calibri")
    display.update()
    time.sleep(1)
    analog.clear()


turtle.done()