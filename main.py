import random
import turtle as t

t.colormode(255)
# colours =["red", "green", "violet", "purple", "orange", "pink"]
# direction = [90, 180, 270]
timmy = t.Turtle()
timmy.shape('turtle')
# timmy.pensize(15)
timmy.speed("fastest")


# to print dotted lines
# for _ in range(5):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 225)
    color = (r, g, b)
    return color


# To print in colour for triangle to decagon
# def draw_shape(side):
#    angle = 360 / side
#    for _ in range(side):
#        timmy.forward(100)
#        timmy.right(angle)


# for item in range(3, 11):
#    timmy.color(random_color())
#    draw_shape(item)

# To move in Random direction
# for item in range(20):
#    timmy.color(random_color())
#    timmy.forward(100)
#   timmy.right(random.choice(direction))

# Spirograph shape
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
