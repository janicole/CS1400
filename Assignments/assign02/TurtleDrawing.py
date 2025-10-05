from turtle import *

# CS 1400 Assignment 2. Written by CS 1400 Course Staff and JANA JOHNSON
 
# Draw a square with a Python turtle.
# Do not modify this.
def draw_square(square_turtle, x, y, side_length):
    # Position the turtle
    square_turtle.penup()
    square_turtle.setposition(x, y)
    square_turtle.pendown()
    # Make the square
    for side in range(4):
        square_turtle.forward(side_length)
        square_turtle.left(90)

#########################################################

# ------------------------------------------------------------
# draw_wall: Draws a horizontal row of 5 square "blocks"
# using draw_square, with a small gap between each block.
def draw_wall(wall_turtle, x, y, height):
    for block in range(5):
        draw_square(wall_turtle, x, y, height)
        x = x + 100

def jump(drawing_turtle, x, y):
    #Move the turtle to (x,y) without drawing. I got tired of typing it out so it's only used in the last method and function word.
    drawing_turtle.penup()
    drawing_turtle.setposition(x, y)
    drawing_turtle.pendown()

def draw_face(face_turtle, x, y, size):
    radius = int(size) # our overall head radius
    # head
    face_turtle.penup()
    face_turtle.setposition(x, y - radius)
    face_turtle.setheading(0)
    face_turtle.pendown()
    face_turtle.circle(radius)
    face_turtle.penup()

    # eyes(two circles)
    eye_radius = int(radius * 0.15)
    eye_distance_x = int(radius * 0.40)
    eye_distance_y = int(radius * 0.25)

    #left eye
    face_turtle.penup()
    face_turtle.setposition(x - eye_distance_x, y + eye_distance_y - eye_radius)
    face_turtle.setheading(0)
    face_turtle.pendown()
    face_turtle.circle(eye_radius)
    face_turtle.penup()

    #right eye
    face_turtle.penup()
    face_turtle.setposition(x + eye_distance_x, y + eye_distance_y - eye_radius)
    face_turtle.setheading(0)
    face_turtle.pendown()
    face_turtle.circle(eye_radius)
    face_turtle.penup()

    # nose
    face_turtle.setposition(x, y + eye_distance_y - int(radius * 0.30))
    face_turtle.pendown()
    face_turtle.forward(int(radius * 0.18))
    face_turtle.left(135)
    face_turtle.forward(int(radius * 0.12))
    face_turtle.left(90)
    face_turtle.forward(int(radius * 0.12))
    face_turtle.penup()

    # mouth
    mouth_y = y - int(radius * 0.27)
    mouth_radius = int(radius * 0.55)
    face_turtle.setposition(x - int(mouth_radius + 0.5), mouth_y)
    face_turtle.setheading(-60)
    face_turtle.pendown()
    face_turtle.circle(mouth_radius, 120)
    face_turtle.penup()

# Letter functions (each draws a different letter with its own
# color and line width).
# Draws the letter 'U'
def draw_letter_U(word_turtle, x, y, h):
    word_turtle.pencolor("blue")
    word_turtle.pensize(6)
    width = int(0.6 * h)

    # left vertical
    jump(word_turtle, x, y)
    word_turtle.setheading(-90)
    word_turtle.pendown()
    word_turtle.forward(h)
    word_turtle.penup()

    # right vertical
    jump(word_turtle, x + width, y)
    word_turtle.setheading(-90)
    word_turtle.pendown()
    word_turtle.forward(h)
    word_turtle.penup()

    # bottom connector
    jump(word_turtle, x, y - h)
    word_turtle.setheading(0)
    word_turtle.pendown()
    word_turtle.forward(width)
    word_turtle.penup()

# Draws the letter 'T'
def draw_letter_T(word_turtle, x, y, t_height):
    word_turtle.pencolor("orange")
    word_turtle.pensize(3)
    width = int(0.6 * t_height)

    # top bar
    jump(word_turtle, x, y)
    word_turtle.setheading(0)
    word_turtle.pendown()
    word_turtle.forward(width)
    word_turtle.penup()

    # stem
    jump(word_turtle, x + width // 2, y)
    word_turtle.setheading(-90)
    word_turtle.pendown()
    word_turtle.forward(t_height)
    word_turtle.penup()

# Draws the letter 'A'
def draw_letter_A(word_turtle, x, y, a_height):
    word_turtle.pencolor("green")
    word_turtle.pensize(4)
    width = int(0.65 * a_height)

    # left leg
    jump(word_turtle, x, y - a_height)
    word_turtle.setheading(60)
    word_turtle.pendown()
    word_turtle.forward(a_height)  # up-left to apex
    word_turtle.penup()

    # right leg
    jump(word_turtle, x + width * 1.6, y - a_height)
    word_turtle.setheading(120)
    word_turtle.pendown()
    word_turtle.forward(a_height)  # up-right to apex
    word_turtle.penup()

    # crossbar (middle)
    cross_y = y - int(0.8 * a_height)
    jump(word_turtle, x + int(0.2 * width), cross_y)
    word_turtle.setheading(0)
    word_turtle.pendown()
    word_turtle.forward(int(1 * width))
    word_turtle.penup()

# draw_word: Writes a short word ("UTA") at (x,y) top-left,
# by calling three different letter functions with different styles.
def draw_word(word_turtle, x, y, height):
    gap = int(0.2 * height)
    width   = int(0.6 * height)
    # U
    draw_letter_U(word_turtle, x, y, height)
    x += width + gap
    # T
    draw_letter_T(word_turtle, x, y, height)
    x += width + gap
    # A
    draw_letter_A(word_turtle, x, y, height)

#########################################################
# Set up the window and turtle
window = Screen()
drawing_turtle = Turtle()
drawing_turtle.speed(4)

# Call the draw_wall function
draw_wall(drawing_turtle, -250, 0, 90) # -250 sets start position of wall

# Call the draw_face function twice in two different places.
draw_face(drawing_turtle, -300, -200, 100)
draw_face(drawing_turtle, 300, -200, 70)


# Call the draw_word function.
draw_word(drawing_turtle, -180, 250, 80)

# You can uncomment this next line to hide the arrow shape
# when you have all your parts working. While writing your
# functions it can be helpful to see where the turtle ends
# up as you add more parts to your drawing.
# drawing_turtle.hideturtle() # Get rid of the arrow showing the turtle location.

window.exitonclick()
