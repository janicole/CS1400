from turtle import * # This imports all the methods from the turtle module

window = Screen() # Creates a window object so we can see the results
my_turtle = Turtle() # Creates a turtle object to use to draw
my_second_turtle = Turtle() # creates a second turtle object

# Your code to tell turtle what to do to make the drawing goes here!
my_turtle.color('blue')
my_second_turtle.color('red')

def draw_square(x, y, side_size, square_turtle):
    square_turtle.teleport(x, y)
    for side in range(4):
        square_turtle.forward(side_size)
        square_turtle.right(90)

def draw_roof(side_size, roof_turtle):
    roof_turtle.left(60)
    roof_turtle.forward(side_size)
    roof_turtle.right(120)
    roof_turtle.forward(side_size)

def draw_house(x, y, side_size, house_turtle):
    draw_square(x, y, side_size, house_turtle)
    draw_roof(side_size, house_turtle)

draw_house(0, 0, 100, my_turtle)
# This code asks the window to stay up until we click on it
# This makes it so we can actually see our drawing
# exitonclick is a method for the Screen object
window.exitonclick()