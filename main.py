"""Main Module"""
import turtle
import random
import colorgram


direction = [0, 90, 180, 270, ]
tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)
tim.pensize(5)
tim.penup()
tim.hideturtle()
DISTANCE = 20
color_palette =[]


def draw_shape(num_of_sides):
    """Function to Draw Shape"""
    for _ in range(1, num_of_sides + 1):
        tim.forward(100)
        tim.right(360 / num_of_sides)

def extract_color():
    """Function to extract color"""
    color_choices = colorgram.extract('image.jpg', 40)
    r_value = 0
    g_value = 0
    b_value = 0
    col_tup = ()
    list_tuples=[]
    #print(color_choices)
    for extract in color_choices:
        r_value = extract.rgb.r
        g_value = extract.rgb.g
        b_value = extract.rgb.b
        col_tup =(r_value, g_value, b_value)
        list_tuples.append(col_tup)
    print(list_tuples)
    return list_tuples
def randomize_color():
    """Function to randomize Color"""
    #r_value = random.randint(1, 255)
    #g_value = random.randint(1, 255)
    #b_value = random.randint(1, 255)
    #tup_value = (r_value, g_value, b_value)
    tup_value = random.choice(color_palette)
    return tup_value


def random_move(paces):
    """Function to turn and move"""
    tim.setheading(random.choice(direction))
    tim.forward(paces)


def draw_spirograph(num_circles):
    """Function to draw spirograph"""
    spin_amount = int(360 / num_circles)
    for radius in range(0, 360, spin_amount):
        tim.pencolor(randomize_color())
        tim.setheading(radius)
        tim.circle(100)


def start_xpos():
    """Calculation to find the starting X position within the screen"""
    return int(20 - (my_screen.window_width() / 2))


def end_xpos():
    """Calculation to find the starting Y position within the screen"""
    return int((my_screen.window_width() / 2) - 20)


def start_ypos():
    """Calculation to find the starting X position"""
    return int(20 - (my_screen.window_height() / 2 ))


def end_ypos():
    """Calculation to find the starting X position"""
    return int((my_screen.window_height() / 2 ) - 20)


def draw_dot():
    """Draw a dot"""
    #tim.pencolor(randomize_color())
    tim.pendown()
    tim.dot(randomize_color())
    tim.penup()


color_palette = extract_color()
tim.speed("fastest")
for y_value in range (start_ypos(), end_ypos(), DISTANCE):
    tim.sety(y_value)
    for x_value in range (start_xpos(), end_xpos(), DISTANCE):
        tim.setx(x_value)
        draw_dot()

print("It's over")

my_screen.exitonclick()
